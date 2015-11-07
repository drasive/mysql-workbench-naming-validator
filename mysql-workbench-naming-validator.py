# MySQL Workbench Plugin "NamingValidator"
# Validates the naming in a model diagram (ERM).
# Created by Dimitri Vranken <me@dimitrivranken.com>
# Written and tested in MySQL Workbench 6.2.4, should work with versions 6.x.
# -*- coding: utf-8 -*-

from wb import *
import datetime
import grt
import mforms
import string
import sys
import traceback

ModuleInfo = DefineModule(name="NamingValidator",
  author="Dimitri Vranken <me@dimitrivranken.com>",
  version="1.0.0",
  description="MySQL Workbench plugin to validate the naming in a model diagram (ERM).")
@ModuleInfo.plugin("dimitri_vranken.naming_validator",
  caption="Naming Validator",
  description="Validates the naming in a model diagram (ERM).",
  input=[wbinputs.currentDiagram()],
  pluginMenu="Utilities")


@ModuleInfo.export(grt.INT, grt.classes.model_Diagram)
def validate_names(diagram):
    try:
        set_status("Analyzing names...")
        
        output = ""
        for figure in diagram.figures:
            if hasattr(figure, "table") and figure.table:
                output += validate_table(figure.table)
        
        if len(output) > 0:
            output = "# Naming convention violations report\n" + \
                     "Time: "+ datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n\n" + \
                     output.rstrip("\n") + "\n"
            set_clipboard_text(output)
            
            set_status("Naming convention violations found. "
                       "A report has been copied into the clipboard.")
        else:
            set_status("No naming convention violations found.")
        
        return 0
    except Exception as e:
        set_clipboard_text("{}\n" + \
                           "Python version: {}".format(
                           traceback.format_exc(), str(sys.version)))
        set_status("Sorry, an error occured while validating the names. "
                   "The error message has been copied into the clipboard.")
        return 1

allowed_characters = set(string.ascii_lowercase + string.digits + '$' + '_')
table_prefix = "tbl_"
def validate_table(table):
    output = ""
    
    # Validate table name
    if not table.name.startswith(table_prefix):
        output += "Table name should start with `{}`  \n".format(table_prefix)
    
    # TODO: Output invalid characters as utf-8 (issue #4)
    if not set(table.name).issubset(allowed_characters):
        output += "Table name contains invalid characters: {}  \n".format(
                  ", ".join(set(table.name).difference(allowed_characters)))
    
    # Validate columns
    for column in table.columns:
        output += validate_column(column, table)
    
    # Validate indices
    index_prefix = "idx_"
    
    for index in table.indices:
        if index.indexType == "PRIMARY" and index.name != "PRIMARY":
            output += "Index `{}` should be called `PRIMARY`  \n".format(index.name)
        elif index.indexType != "PRIMARY" and \
          index.name != index_prefix + index.columns[0].referencedColumn.name :
            output += "Index `{}` should be called `{}`  \n".format(
                       index.name, index_prefix + index.columns[0].referencedColumn.name)
            # more than one indexed column is not possible for non-primary indices
    
    # Validate foreign keys
    for foreign_key in table.foreignKeys:
        if len(foreign_key.columns) == 1 and foreign_key.name != foreign_key.columns[0].name:
            output += "Foreign key `{}` should be called `{}`  \n".format(
                       foreign_key.name, foreign_key.columns[0].name)
        elif len(foreign_key.columns) == 0:
            output += "Foreign key `{}` must belong a column (or be deleted)  \n".format(
                       foreign_key.name)
        elif len(foreign_key.columns) > 1:
            # TODO: Implement validation for foreign keys belonging to multiple columns (issue #1)
            output += "Foreign key `{}` belongs to multiple columns and " + \
                      "can't be validated yet (plugin limitation)  \n".format(
                      foreign_key.name)
    
    # TODO: Add validation for triggers (issue #3)
    
    if len(output) > 0:
        output = "## Table `" + table.name + "`\n" + \
                 output + "\n"
    
    return output

def validate_column(column, table):
    output = ""
    primary_key_name = "id"
    foreign_key_prefix = "fk_"
    primary_foreign_key_prefix = "idfk_"
    
    # TODO: Output invalid characters as utf-8 (issue #4)
    if not set(column.name).issubset(allowed_characters):
        output += "Column `{}` contains invalid characters: {}  \n".format(
                  column.name, ", ".join(set(column.name).difference(allowed_characters)))
    
    isPrimaryKey = False
    isForeignKey = False
    foreignKeyTable = ""
    foreignKeyTableReferences = 0
    for index in table.indices:
        if index.indexType == "PRIMARY":
            for index_column in index.columns:
                if index_column.referencedColumn.name == column.name:
                    isPrimaryKey = True
                    break
    for foreign_key in table.foreignKeys:
        if foreign_key.columns[0].name == column.name:
            isForeignKey = True
            foreignKeyTable = foreign_key.referencedColumns[0].owner.name
            break
    if isForeignKey:
        for foreign_key in table.foreignKeys:
            if foreign_key.referencedColumns[0].owner.name == foreignKeyTable:
                foreignKeyTableReferences += 1
    
    foreignKeyTableWithoutPrefix = foreignKeyTable[len(table_prefix):]
    if isPrimaryKey and isForeignKey:
        if foreignKeyTableReferences == 1 and \
          column.name != primary_foreign_key_prefix + foreignKeyTableWithoutPrefix:
            output += "Column `{}` should be called `{}`  \n".format(
                       column.name, primary_foreign_key_prefix + foreignKeyTableWithoutPrefix)
        elif foreignKeyTableReferences > 1 and \
          not column.name.startswith(primary_foreign_key_prefix + foreignKeyTableWithoutPrefix + "_"):
            output += "Column `{}` should start with `{}`  \n".format(
                       column.name, primary_foreign_key_prefix + foreignKeyTableWithoutPrefix + "_")
    elif isPrimaryKey and column.name != primary_key_name:
        # TODO: Implement validation for multiple primary key only columns in a table (issue #2)
        output += "Column `{}` should be called `{}`  \n".format(
                  column.name, primary_key_name)
    elif isForeignKey:
        if foreignKeyTableReferences == 1 and \
          column.name != foreign_key_prefix + foreignKeyTableWithoutPrefix:
            output += "Column `{}` should be called `{}`  \n".format(
                       column.name, foreign_key_prefix + foreignKeyTableWithoutPrefix)
        elif foreignKeyTableReferences > 1 and \
          not column.name.startswith(foreign_key_prefix + foreignKeyTableWithoutPrefix + "_"):
            output += "Column `{}` should start with `{}`  \n".format(
                       column.name, foreign_key_prefix + foreignKeyTableWithoutPrefix + "_")
    
    return output

def set_status(status):
    mforms.App.get().set_status_text(status)

def set_clipboard_text(text):
    mforms.Utilities.set_clipboard_text(text)

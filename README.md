# mysql-workbench-naming-validator

A MySQL Workbench plugin to validate the naming in a model diagram (ERM).  
Should work in MySQL Workbench versions 6.x.

## Features
- Validates naming of tables, columns, indices and foreign keys
- Generated report is formatted as Markdown (see [`sample-output.md`](sample-output.md))
- Does not fix naming convention violations, only points them out

## Installation
1. Download the latest [release](releases/)
2. Open MySQL Worbench
3. Navigate to `Scripting` > `Install Plugin/Module...`
4. Browse and select the downloaded file `mysql-workbench-naming-validator.py`

## Usage
### Validate a model diagram (ERM)
1. Open the Model Diagram
2. Navigate to `Tools` > `Utilities` > `Validate Naming`
3. The status bar will contain the status of the analysis.
   If there are any naming violations, paste the generated report from your clipboard into an editor.

### Validate an existing database
This plugin can only validate model diagrams, not existing databases.
To validate the naming in an existing database, you have to generate an ERM for it first.
This can be done through the MySQL Worbench and is called "[Reverse Engineering](https://dev.mysql.com/doc/workbench/en/wb-reverse-engineer-live.html)".

1. Open MySQL Workbench
2. Navigate to `Database` > `Reverse Engineer`
3. Follow the dialog steps
4. An ERM for the selected database will be generated
5. Follow the steps described in "Validate a model diagram (ERM)" above.

## Validation rules
At the time, only the following set of validation rules is available.  
There may be a few situations in which some rules don't make sense or can't be satisfied.
If you encounter such a situation, please create an [issue](issues/).

### Tables
- Must start with `tbl_`
- Must only contain the characters `A-Z`, `a-z`, `0-9`, `$`  and `_`

### Columns
- Must only contain the characters `A-Z`, `a-z`, `0-9`, `$`  and `_`
- Is primary key only:
    - Is the only primary key only column (in table):
        - Must be called `id`
    - There are other primary key only columns (in table):
        - Can't be validated properly yet (plugin limitation)
- Is foreign key only:
    - Is the only foreign key referencing the reference table (in table):
        - Must be called `fk_` + referenced table without `tbl_` prefix
    - There are other foreign keys referencing the reference table (in table):
        - Must start with `fk_` + referenced table w/o `tbl_` prefix + `_`
- Is primary key and foreign key:
    - Is the only foreign key referencing the reference table (in table):
        - Must be called `idfk_` + referenced table without `tbl_` prefix
    - There are other foreign keys referencing the reference table (in table):
        - Must start with `idfk_` + referenced table w/o `tbl_` prefix + `_`

### Indices
- Primary indices must be called `PRIMARY`
- Non-primary indices must be called `idx_` + the indexed column

### Foreign keys
- Must belong to at least one column
- Belongs to a single column:
    - Must be called like the belonging column
- Belongs to more than one column:
    - Can't be validated yet (plugin limitation)

## License
This repository is released under the GPLv3 license.  
Please see the [license file](LICENSE) for further information.

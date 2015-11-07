# Naming convention violations report
Time: 2015-11-07 14:58:04

## Table `actor`
Table name should start with `tbl_`  
Column `actor_id` should be called `id`  
Index `idx_actor_last_name` should be called `idx_last_name`  

## Table `address`
Table name should start with `tbl_`  
Column `address_id` should be called `id`  
Column `city_id` should be called `fk_`  
Index `idx_fk_city_id` should be called `idx_city_id`  
Foreign key `fk_address_city` should be called `city_id`  

## Table `category`
Table name should start with `tbl_`  
Column `category_id` should be called `id`  

## Table `city`
Table name should start with `tbl_`  
Column `city_id` should be called `id`  
Column `country_id` should be called `fk_try`  
Index `idx_fk_country_id` should be called `idx_country_id`  
Foreign key `fk_city_country` should be called `country_id`  

## Table `country`
Table name should start with `tbl_`  
Column `country_id` should be called `id`  

## Table `customer`
Table name should start with `tbl_`  
Column `customer_id` should be called `id`  
Column `store_id` should be called `fk_e`  
Column `address_id` should be called `fk_ess`  
Index `idx_fk_store_id` should be called `idx_store_id`  
Index `idx_fk_address_id` should be called `idx_address_id`  
Foreign key `fk_customer_address` should be called `address_id`  
Foreign key `fk_customer_store` should be called `store_id`  

## Table `film`
Table name should start with `tbl_`  
Column `film_id` should be called `id`  
Column `language_id` should start with `fk_uage_`  
Column `original_language_id` should start with `fk_uage_`  
Index `idx_fk_language_id` should be called `idx_language_id`  
Index `idx_fk_original_language_id` should be called `idx_original_language_id`  
Foreign key `fk_film_language` should be called `language_id`  
Foreign key `fk_film_language_original` should be called `original_language_id`  

## Table `film_actor`
Table name should start with `tbl_`  
Column `actor_id` should be called `idfk_r`  
Column `film_id` should be called `idfk_`  
Index `idx_fk_film_id` should be called `idx_film_id`  
Foreign key `fk_film_actor_actor` should be called `actor_id`  
Foreign key `fk_film_actor_film` should be called `film_id`  

## Table `film_category`
Table name should start with `tbl_`  
Column `film_id` should be called `idfk_`  
Column `category_id` should be called `idfk_gory`  
Index `fk_film_category_category` should be called `idx_category_id`  
Foreign key `fk_film_category_category` should be called `category_id`  
Foreign key `fk_film_category_film` should be called `film_id`  

## Table `film_text`
Table name should start with `tbl_`  
Column `film_id` should be called `id`  
Index `idx_title_description` should be called `idx_title`  

## Table `inventory`
Table name should start with `tbl_`  
Column `inventory_id` should be called `id`  
Column `film_id` should be called `fk_`  
Column `store_id` should be called `fk_e`  
Index `idx_fk_film_id` should be called `idx_film_id`  
Index `idx_store_id_film_id` should be called `idx_store_id`  
Foreign key `fk_inventory_film` should be called `film_id`  
Foreign key `fk_inventory_store` should be called `store_id`  

## Table `language`
Table name should start with `tbl_`  
Column `language_id` should be called `id`  

## Table `payment`
Table name should start with `tbl_`  
Column `payment_id` should be called `id`  
Column `customer_id` should be called `fk_omer`  
Column `staff_id` should be called `fk_f`  
Column `rental_id` should be called `fk_al`  
Index `idx_fk_staff_id` should be called `idx_staff_id`  
Index `idx_fk_customer_id` should be called `idx_customer_id`  
Index `fk_payment_rental` should be called `idx_rental_id`  
Foreign key `fk_payment_customer` should be called `customer_id`  
Foreign key `fk_payment_rental` should be called `rental_id`  
Foreign key `fk_payment_staff` should be called `staff_id`  

## Table `rental`
Table name should start with `tbl_`  
Column `rental_id` should be called `id`  
Column `inventory_id` should be called `fk_ntory`  
Column `customer_id` should be called `fk_omer`  
Column `staff_id` should be called `fk_f`  
Index `rental_date` should be called `idx_rental_date`  
Index `idx_fk_inventory_id` should be called `idx_inventory_id`  
Index `idx_fk_customer_id` should be called `idx_customer_id`  
Index `idx_fk_staff_id` should be called `idx_staff_id`  
Foreign key `fk_rental_customer` should be called `customer_id`  
Foreign key `fk_rental_inventory` should be called `inventory_id`  
Foreign key `fk_rental_staff` should be called `staff_id`  

## Table `staff`
Table name should start with `tbl_`  
Column `staff_id` should be called `id`  
Column `address_id` should be called `fk_ess`  
Column `store_id` should be called `fk_e`  
Index `idx_fk_store_id` should be called `idx_store_id`  
Index `idx_fk_address_id` should be called `idx_address_id`  
Foreign key `fk_staff_address` should be called `address_id`  
Foreign key `fk_staff_store` should be called `store_id`  

## Table `store`
Table name should start with `tbl_`  
Column `store_id` should be called `id`  
Column `manager_staff_id` should be called `fk_f`  
Column `address_id` should be called `fk_ess`  
Index `idx_unique_manager` should be called `idx_manager_staff_id`  
Index `idx_fk_address_id` should be called `idx_address_id`  
Foreign key `fk_store_address` should be called `address_id`  
Foreign key `fk_store_staff` should be called `manager_staff_id`  

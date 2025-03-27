-- Backticks (`): These are used in MySQL to escape column names that contain spaces or special characters.
create database solar_power;
use solar_power;

show global variables like 'local_infile';
set global local_infile=1;
grant file on  *.* to 'root'@'localhost';
show variables like "secure_file_priv";

-- INVERTER dataset -------------------------------------------------
create table inverter
(
  date_time datetime, 
  unit1_inv1 float, 
  unit1_inv2 float, 
  unit2_inv1 float, 
  unit2_inv2 float
);
SELECT LOAD_FILE('C:/inverter_numeric.csv');
SHOW WARNINGS;

load data infile 'C:\Program Files\MySQL\MySQL Server 8.0\uploads\inverter_numeric.csv'
into table inverter
fields terminated by ','
enclosed by '"'
lines terminated by '\n'
ignore 1 rows;

select * from inverter;
select count(*) from inverter;
select * from inverter limit 10;
describe inverter;

-------------------------- EXPLORATORY DATA ANALYSIS ---------------------------------------------
-- First Business Moments----------------------------------------------------------------
-- MEAN
select avg(coalesce(`Unit 1_INV1`, 0)) as mean_unit1_inv1 from inverter;                 -- as the column name has space
select avg(coalesce(`Unit 1_INV2`, 0)) as mean_unit1_inv2 from inverter;                 -- generally we dont use ''
select avg(coalesce(`Unit 2_INV1`, 0)) as mean_unit2_inv1 from inverter;                 -- If you find any non-numeric or NULL values, you can handle them in the query by using COALESCE to replace NULL with 0:
select avg(coalesce(`Unit 2_INV2`, 0)) as mean_unit2_inv2 from inverter; 

----------------------------------------- MEDIAN
select `Unit 1_INV1` as median_unit1_inv1
from (
    select `Unit 1_INV1`, row_number() 
    over (order by `Unit 1_INV1`) as row_num,
	count(*) over () as total_count
    from inverter
) as subquery
where row_num = (total_count + 1) / 2 or row_num = (total_count + 2) / 2;   

select `Unit 1_INV2` as median_unit1_inv2
from (
    select `Unit 1_INV2`, row_number() 
    over (order by `Unit 1_INV2`) as row_num,
	count(*) over () as total_count
    from inverter
) as subquery
where row_num = (total_count + 1) / 2 or row_num = (total_count + 2) / 2;   

select `Unit 2_INV1` as median_unit2_inv1
from (
    select `Unit 2_INV1`, row_number() 
    over (order by `Unit 2_INV1`) as row_num,
	count(*) over () as total_count
    from inverter
) as subquery
where row_num = (total_count + 1) / 2 or row_num = (total_count + 2) / 2;   

select `Unit 2_INV2` as median_unit2_inv2
from (
    select `Unit 2_INV2`, row_number() 
    over (order by `Unit 2_INV2`) as row_num,
	count(*) over () as total_count
    from inverter
) as subquery
where row_num = (total_count + 1) / 2 or row_num = (total_count + 2) / 2;   

----------------------------------------------- MODE
select `Unit 1_INV1`, count(`Unit 1_INV1`) 
as freq_unit1_inv1 
from inverter 
group by `Unit 1_INV1`
order by freq_unit1_inv1 
desc limit 1;

select `Unit 1_INV2`, count(`Unit 1_INV2`) 
as freq_unit1_inv2 
from inverter 
group by `Unit 1_INV2`
order by freq_unit1_inv2 
desc limit 1;

select `Unit 2_INV1`, count(`Unit 2_INV1`) 
as freq_unit2_inv1 
from inverter 
group by `Unit 2_INV1`
order by freq_unit2_inv1 
desc limit 1;

select `Unit 2_INV2`, count(`Unit 2_INV2`) 
as freq_unit2_inv2 
from inverter 
group by `Unit 2_INV2`
order by freq_unit2_inv2 
desc limit 1;

-- Second Business Moments -----------------------------------------------------------------------------------
-- STANDARD DEVIATION
select stddev(cast(`Unit 1_INV1` as double)) as std_unit1_inv1
from inverter;

select stddev(cast(`Unit 1_INV2` as double)) as std_unit1_inv2
from inverter;

select stddev(cast(`Unit 2_INV1` as double)) as std_unit2_inv1
from inverter;

select stddev(cast(`Unit 2_INV2` as double)) as stddev_unit2_inv2
from inverter;


-------------------------------------------- VARIANCE
select variance(`Unit 1_INV1`) as var_unit1_inv1
from inverter;

select variance(`Unit 1_INV2`) as var_unit1_inv2
from inverter;

select variance(`Unit 2_INV1`) as var_unit2_inv1
from inverter;

select variance(`Unit 2_INV2`) as var_unit2_inv2
from inverter;

----------------------------------------------- RANGE
select max(`Unit 1_INV1`) - min(`Unit 1_INV1`) as range_unit1_inv1
from inverter;

select max(`Unit 1_INV2`) - min(`Unit 1_INV2`) as range_unit1_inv2
from inverter;

select max(`Unit 2_INV1`) - min(`Unit 2_INV1`) as range_unit2_inv1
from inverter;

select max(`Unit 2_INV2`) - min(`Unit 2_INV2`) as range_unit2_inv2
from inverter;


-- Third Business Moment------------------------------------------------------------------------
-- SKEWNESS
select
    (
        sum(power(`Unit 1_INV1` - (select avg(`Unit 1_INV1`) 
        from inverter), 3)) / 
        (count(*) * power((select stddev(`Unit 1_INV1`) 
        from inverter), 3))
    ) 
        as skew_unit1_inv1
        from inverter;
        
select
    (
        sum(power(`Unit 1_INV2` - (select avg(`Unit 1_INV2`) 
        from inverter), 3)) / 
        (count(*) * power((select stddev(`Unit 1_INV2`) 
        from inverter), 3))
    ) 
        as skew_unit1_inv2
        from inverter;
        
select
    (
        sum(power(`Unit 2_INV1` - (select avg(`Unit 2_INV1`) 
        from inverter), 3)) / 
        (count(*) * power((select stddev(`Unit 2_INV1`) 
        from inverter), 3))
    ) 
        as skew_unit2_inv1
        from inverter;
        
select
    (
        sum(power(`Unit 2_INV2` - (select avg(`Unit 2_INV2`) 
        from inverter), 3)) / 
        (count(*) * power((select stddev(`Unit 2_INV2`) 
        from inverter), 3))
    ) 
        as skew_unit2_inv2
        from inverter;
        
-- Fourth Business Moment ----------------------------------------------------------------------------
-- KURTOSIS
select 
    (
	      (sum(power(`Unit 1_INV1` - (select avg(`Unit 1_INV1`) from inverter), 4)) / 
	      (count(*) * power((select stddev(`Unit 1_INV1`) from inverter), 4))) - 3
    )     
		    as kurt_unit1_inv1
		    from inverter;
            
select 
    (
	      (sum(power(`Unit 1_INV2` - (select avg(`Unit 1_INV2`) from inverter), 4)) / 
	      (count(*) * power((select stddev(`Unit 1_INV2`) from inverter), 4))) - 3
    )     
		    as kurt_unit1_inv2
		    from inverter;
            
select 
    (
	      (sum(power(`Unit 2_INV1` - (select avg(`Unit 2_INV1`) from inverter), 4)) / 
	      (count(*) * power((select stddev(`Unit 2_INV1`) from inverter), 4))) - 3
    )     
		    as kurt_unit2_inv1
		    from inverter;
            
select 
    (
	      (sum(power(`Unit 2_INV2` - (select avg(`Unit 2_INV2`) from inverter), 4)) / 
	      (count(*) * power((select stddev(`Unit 2_INV2`) from inverter), 4))) - 3
    )     
		    as kurt_unit2_inv2
		    from inverter;
            
-------------------------------------- DATA PREPROCESSING INVERTER DATASET ---------------------------------------------------------------------------
----------------------------- TYPECASTING
use solar_power;
select * from inverter;
describe inverter;

update inverter
set `DATE/TIME` = trim(`DATE/TIME`)                                    -- remove trailing spaces for conversion
where `DATE/TIME` is not null;

update inverter
set `DATE/TIME` = str_to_date(`DATE/TIME`, '%d-%m-%Y %H:%i')           -- converting to a valid format
where str_to_date(`DATE/TIME`, '%d-%m-%Y %H:%i') is not null;

alter table inverter
modify `DATE/TIME` datetime;

alter table inverter
modify `Unit 1_INV1` decimal(10,2),
modify `Unit 1_INV2` decimal(10,2),
modify `Unit 2_INV1` decimal(10,2),
modify `Unit 2_INV2` decimal(10,2);


----------------------- Find Duplicate records
select `Unit 1_INV1`, count(*) as duplicate_count                          -- duplicates found
from inverter                                                              -- no need to remove duplicates
group by `Unit 1_INV1`
having count(*) > 1;

select `Unit 1_INV2`, count(*) as duplicate_count
from inverter
group by `Unit 1_INV2`
having count(*) > 1;

select `Unit 2_INV1`, count(*) as duplicate_count
from inverter
group by `Unit 2_INV1`
having count(*) > 1;

select `Unit 2_INV2`, count(*) as duplicate_count
from inverter
group by `Unit 1_INV1`
having count(*) > 1;

----------------------------------- Check for NULL or 0 values
select count(*) as total_values,                                                          -- no null values
sum(case when `Unit 1_INV1` is null then 1 else 0 end) AS unit1_inv1_null_count,
sum(case when `Unit 1_INV2` is null then 1 else 0 end) AS unit1_inv2_null_count,
sum(case when `Unit 2_INV1` is null then 1 else 0 end) AS unit2_inv1_null_count,
sum(case when `Unit 2_INV2` is null then 1 else 0 end) AS unit2_inv2_null_count
from inverter;

-------------------------------- VARIANCE & ZERO VARIANCE
select
variance(`Unit 1_INV1`) as variance_unit1_inv1,                       -- its quite high in every column
variance(`Unit 1_INV2`) as variance_unit1_inv2,
variance(`Unit 2_INV1`) as variance_unit2_inv1,
variance(`Unit 2_INV2`) as variance_unit2_inv2
from inverter;


-------------------------------- OUTLIER DETECTION
select * from inverter;
select `Unit 1_INV1`, `Unit 1_INV2`, `Unit 2_INV1`, `Unit 2_INV2`,                   -- performance based analysis
ntile(4) over (order by `Unit 1_INV1` desc) 
as performance_quartile
from inverter;

select `Unit 1_INV1`, `Unit 1_INV2`, `Unit 2_INV1`, `Unit 2_INV2`,                   -- time based analysis
ntile(4) over (order by `DATE/TIME` asc) 
as time_quartile
from inverter;

-------------------------------- OUTLIER TREATMENT (Replacing with Mean)
set sql_safe_updates = 0;
set global innodb_lock_wait_timeout = 120;

-- Calculate the quartiles in a temporary table to avoid recalculating ntile(4) repeatedly.
create temporary table temp_quartiles as                        
select `Unit 1_INV1`, `Unit 1_INV2`, `Unit 2_INV1`, `Unit 2_INV2`,
ntile(4) over (order by `Unit 1_INV1`) as performance_quartile
from inverter;

-- Calculate the average value of Unit 1_INV1 for each quartile and store it in another temporary table
create temporary table temp_quartile_averages as                       
select 
    performance_quartile, 
    avg(`Unit 1_INV1`) as avg_unit1_inv1
from temp_quartiles
group by performance_quartile;

-- Join the temporary tables and update rows where the quartile is either 1 or 4.
update inverter as i
join temp_quartiles as tq on i.`Unit 1_INV1` = tq.`Unit 1_INV1`
join temp_quartile_averages as tqa on tq.performance_quartile = tqa.performance_quartile
set i.`Unit 1_INV1` = tqa.avg_unit1_inv1
where tq.performance_quartile in (1, 4);

drop temporary table if exists temp_quartiles;
drop temporary table if exists temp_quartile_averages;

----------------------------- Verify the updated records
select * from inverter;

/*
update inverter as i
join (
       select `Unit 1_INV1`, `Unit 1_INV2`, `Unit 2_INV1`, `Unit 2_INV2`,
	   ntile(4) over (order by `Unit 1_INV1`) as performance_quartile
       from inverter
)      as subquery on i.`Unit 1_INV1` = subquery.`Unit 1_INV1`
       set i.`Unit 1_INV1`= (
       select avg(`Unit 1_INV1`)
from (
		select `Unit 1_INV1`, `Unit 1_INV2`, `Unit 2_INV1`, `Unit 2_INV2`,
	    ntile(4) over (order by `Unit 1_INV1`) as performance_quartile
        from inverter
    )   as temp
where performance_quartile = subquery.performance_quartile
)
where subquery.performance_quartile in (1, 4);
*/


----------------------------------------------- TRANSFORMATION
select * from inverter;

create table inverter_transformed as
select `Unit 1_INV1`, `Unit 1_INV2`, `Unit 2_INV1`, `Unit 2_INV2`, 
    log(`Unit 1_INV1` + 1) as unit1_inv1_log,                         -- Added +1 to handle potential zeros or negative values.
    sqrt(`Unit 1_INV1`) as unit1_inv1_sqrt, 
    log(`Unit 1_INV2` + 1) as unit1_inv2_log, 
    sqrt(`Unit 1_INV2`) as unit1_inv2_sqrt,
    log(`Unit 2_INV1` + 1) as unit2_inv1_log, 
    sqrt(`Unit 2_INV1`) as unit2_inv1_sqrt, 
    log(`Unit 2_INV2` + 1) as unit2_inv2_log, 
    sqrt(`Unit 2_INV2`) as unit2_inv2_sqrt
from inverter;
select * from inverter_transformed;


-------------------------------------------- SCALING
create table inverter_scaled as
select 
    (`Unit 1_INV1` - unit1_inv1_min) / (unit1_inv1_max - unit1_inv1_min) as scaled_unit1_inv1,
    (`Unit 1_INV2` - unit1_inv2_min) / (unit1_inv2_max - unit1_inv2_min) as scaled_unit1_inv2,
    (`Unit 2_INV1` - unit2_inv1_min) / (unit2_inv1_max - unit2_inv1_min) as scaled_unit2_inv1,
    (`Unit 2_INV2` - unit2_inv2_min) / (unit2_inv2_max - unit2_inv2_min) as scaled_unit2_inv2
from (
    select `Unit 1_INV1`, `Unit 1_INV2`, `Unit 2_INV1`, `Unit 2_INV2`, 
        (select min(`Unit 1_INV1`) from inverter) as unit1_inv1_min,
        (select max(`Unit 1_INV1`) from inverter) as unit1_inv1_max,
        (select min(`Unit 1_INV2`) from inverter) as unit1_inv2_min,
        (select max(`Unit 1_INV2`) from inverter) as unit1_inv2_max,
        (select min(`Unit 2_INV1`) from inverter) as unit2_inv1_min,
        (select max(`Unit 2_INV1`) from inverter) as unit2_inv1_max,
        (select min(`Unit 2_INV2`) from inverter) as unit2_inv2_min,
        (select max(`Unit 2_INV2`) from inverter) as unit2_inv2_max
    from inverter
) as scaled_data;

select * from inverter_scaled;




            
           
--------------------------------------------  WEATHER dataset -----------------------------------------------------------------------------------------------------
create table weather
(
  date_time datetime, 
  gii float, 
  module_temp float, 
  rain float, 
  ambient_temp float
);

load data infile 'C:\Program Files\MySQL\MySQL Server 8.0\uploads\WMS Report.csv'
into table weather
fields terminated by ','
enclosed by '"'
lines terminated by '\n'
ignore 1 rows;

select * from weather;
select count(*) from weather;
select * from weather limit 10;
describe weather;

-------------------------- EXPLORATORY DATA ANALYSIS --------------------------------------------- 
-- First Business Moments------------------------------------------------------------------------------
-- MEAN
select avg(GII) as mean_gii from weather;
select avg(RAIN) as mean_rain from weather;
select avg(`MODULE TEMP.1`) as mean_module_temp from weather;                     --  MODULE TEMP.1   ------------
select avg(`AMBIENT TEMPRETURE`) as mean_amb_temp from weather;                   -- AMBIENT TEMPRETURE  ----------

-------------------------------------- MEDIAN
select RAIN as median_rain
from (
    select RAIN, row_number() 
    over (order by RAIN) as row_num,
	count(*) over () as total_count
    from weather
) as subquery
where row_num = (total_count + 1) / 2 or row_num = (total_count + 2) / 2;   

select `MODULE TEMP.1` as median_module_temp
from (
    select `MODULE TEMP.1`, row_number() 
    over (order by `MODULE TEMP.1`) as row_num,
	count(*) over () as total_count
    from weather
) as subquery
where row_num = (total_count + 1) / 2 or row_num = (total_count + 2) / 2;  

select `AMBIENT TEMPRETURE` as median_amb_temp
from (
    select `AMBIENT TEMPRETURE`, row_number() 
    over (order by `AMBIENT TEMPRETURE`) as row_num,
	count(*) over () as total_count
    from weather
) as subquery
where row_num = (total_count + 1) / 2 or row_num = (total_count + 2) / 2;  

-------------------------------------------- MODE
select GII, count(GII)                       
as freq_gii 
from weather 
group by GII
order by freq_gii 
desc limit 1;

select RAIN, count(RAIN) 
as freq_rain 
from weather 
group by RAIN
order by freq_rain 
desc limit 1;

select `MODULE TEMP.1`, count(`MODULE TEMP.1`) 
as freq_module_temp 
from weather 
group by `MODULE TEMP.1`
order by freq_module_temp 
desc limit 1;

select `AMBIENT TEMPRETURE`, count(`AMBIENT TEMPRETURE`) 
as freq_amb_temp 
from weather 
group by `AMBIENT TEMPRETURE`
order by freq_amb_temp 
desc limit 1;


-- Second Business Moments -----------------------------------------------------------------------------------
-- STANDARD DEVIATION
select stddev(GII) as std_gii
from weather;

select stddev(RAIN) as std_rain
from weather;

select stddev(cast(`MODULE TEMP.1` as double)) as std_module_temp
from weather;

select stddev(cast(`AMBIENT TEMPRETURE` as double)) as std_amb_temp
from weather;

----------------------------- VARIANCE
select variance(GII) as var_gii
from weather;

select variance(RAIN) as var_rain
from weather;

select variance(`MODULE TEMP.1`) as var_unit1_inv1
from weather;

select variance(`AMBIENT TEMPRETURE`) as var_unit1_inv1
from weather;

------------------------------ RANGE
select max(GII) - min(GII) as range_gii
from weather;

select max(RAIN) - min(RAIN) as range_gii
from weather;

select max(`MODULE TEMP.1`) - min(`MODULE TEMP.1`) as range_module_temp
from weather;

select max(`AMBIENT TEMPRETURE`) - min(`AMBIENT TEMPRETURE`) as range_module_temp
from weather;

-- Third Business Moment------------------------------------------------------------------------
-- SKEWNESS
select
    (
        sum(power(GII - (select avg(GII) 
        from weather), 3)) / 
        (count(*) * power((select stddev(GII) 
        from weather), 3))
    ) 
        as skew_gii
        from weather;
        
select
    (
        sum(power(RAIN - (select avg(RAIN) 
        from weather), 3)) / 
        (count(*) * power((select stddev(RAIN) 
        from weather), 3))
    ) 
        as skew_rain
        from weather;
        
select
    (
        sum(power(`MODULE TEMP.1` - (select avg(`MODULE TEMP.1`) 
        from weather), 3)) / 
        (count(*) * power((select stddev(`MODULE TEMP.1`) 
        from weather), 3))
    ) 
        as skew_module_temp
        from weather;
        
select
    (
        sum(power(`AMBIENT TEMPRETURE` - (select avg(`AMBIENT TEMPRETURE`) 
        from weather), 3)) / 
        (count(*) * power((select stddev(`AMBIENT TEMPRETURE`) 
        from weather), 3))
    ) 
        as skew_amb_temp
        from weather;
        

-- Fourth Business Moment ----------------------------------------------------------------------------
-- KURTOSIS
select 
    (
	      (sum(power(GII - (select avg(GII) from weather), 4)) / 
	      (count(*) * power((select stddev(GII) from weather), 4))) - 3
    )     
		    as kurt_gii
		    from weather;
            
select 
    (
	      (sum(power(RAIN - (select avg(RAIN) from weather), 4)) / 
	      (count(*) * power((select stddev(RAIN) from weather), 4))) - 3
    )     
		    as kurt_rain
		    from weather;
            
select 
    (
	      (sum(power(`MODULE TEMP.1` - (select avg(`MODULE TEMP.1`) from weather), 4)) / 
	      (count(*) * power((select stddev(`MODULE TEMP.1`) from weather), 4))) - 3
    )     
		    as kurt_module_temp
		    from weather;
            
select 
    (
	      (sum(power(`AMBIENT TEMPRETURE`- (select avg(`AMBIENT TEMPRETURE`) from weather), 4)) / 
	      (count(*) * power((select stddev(`AMBIENT TEMPRETURE`) from weather), 4))) - 3
    )     
		    as kurt_amb_temp
		    from weather;

-------------------------------------- DATA PREPROCESSING WEATHER DATASET ---------------------------------------------------------------------------
----------------------------- TYPECASTING
use solar_power;
select * from weather;
describe weather;

update weather
set `DATE/TIME` = trim(`DATE/TIME`)                                    -- remove trailing spaces for conversion
where `DATE/TIME` is not null;

update weather
set `DATE/TIME` = str_to_date(`DATE/TIME`, '%d-%m-%Y %H:%i')           -- converting to a valid format
where str_to_date(`DATE/TIME`, '%d-%m-%Y %H:%i') is not null;

alter table weather
modify `DATE/TIME` datetime;

alter table weather
modify GII int,
modify RAIN float,
modify `MODULE TEMP.1` decimal(10,2),
modify `AMBIENT TEMPRETURE` decimal(10,2);


----------------------- Find Duplicate records
select GII, count(*) as duplicate_count                          -- duplicates found
from weather                                                     -- no need to remove duplicates
group by GII
having count(*) > 1;

select RAIN, count(*) as duplicate_count
from weather
group by RAIN
having count(*) > 1;

select `MODULE TEMP.1`, count(*) as duplicate_count
from weather
group by `MODULE TEMP.1`
having count(*) > 1;

select `AMBIENT TEMPRETURE`, count(*) as duplicate_count
from weather
group by `AMBIENT TEMPRETURE`
having count(*) > 1;

----------------------------------- Check for NULL or 0 values
select count(*) as total_values,                                                          -- no null values
sum(case when GII is null then 1 else 0 end) AS gii_null_count,
sum(case when RAIN is null then 1 else 0 end) AS rain_null_count,
sum(case when `MODULE TEMP.1` is null then 1 else 0 end) AS module_temp_null_count,
sum(case when `AMBIENT TEMPRETURE` is null then 1 else 0 end) AS amb_temp_null_count
from weather;

-------------------------------- VARIANCE & ZERO VARIANCE
select
variance(GII) as variance_gii,                               -- its quite high in GII and less in others
variance(RAIN) as variance_rain,
variance(`MODULE TEMP.1`) as variance_module_temp,
variance(`AMBIENT TEMPRETURE`) as variance_amb_temp
from weather;

-------------------------------- OUTLIER DETECTION
select * from weather;
select GII, RAIN, `MODULE TEMP.1`, `AMBIENT TEMPRETURE`,                  -- performance based analysis
ntile(4) over (order by GII desc) 
as performance_quartile
from weather;

select GII, RAIN, `MODULE TEMP.1`, `AMBIENT TEMPRETURE`,                   -- time based analysis
ntile(4) over (order by `DATE/TIME` asc) 
as time_quartile
from weather;

-------------------------------- OUTLIER TREATMENT (Replacing with Mean)
set sql_safe_updates = 0;
set global innodb_lock_wait_timeout = 120;

-- Calculate the quartiles in a temporary table to avoid recalculating ntile(4) repeatedly.
create temporary table temp_quartiles as                        
select GII, RAIN, `MODULE TEMP.1`, `AMBIENT TEMPRETURE`,
ntile(4) over (order by GII) as performance_quartile
from weather;

-- Calculate the average value of Unit 1_INV1 for each quartile and store it in another temporary table
create temporary table temp_quartile_averages as                       
select 
    performance_quartile, 
    avg(GII) as avg_gii
from temp_quartiles
group by performance_quartile;

-- Join the temporary tables and update rows where the quartile is either 1 or 4.
update weather as w
join temp_quartiles as tq on w.GII = tq.GII
join temp_quartile_averages as tqa on tq.performance_quartile = tqa.performance_quartile
set w.GII = tqa.avg_gii
where tq.performance_quartile in (1, 4);

drop temporary table if exists temp_quartiles;
drop temporary table if exists temp_quartile_averages;


----------------------------------------------- TRANSFORMATION
select * from weather;

create table weather_transformed as
select GII, RAIN, `MODULE TEMP.1`, `AMBIENT TEMPRETURE`, 
    log(GII + 1) as gii_log,                                   -- Added +1 to handle potential zeros or negative values.
    sqrt(GII) as gii_sqrt, 
    log(RAIN + 1) as rain_log, 
    sqrt(RAIN) as rain_sqrt,
    log(`MODULE TEMP.1` + 1) as module_temp_log, 
    sqrt(`MODULE TEMP.1`) as module_temp_sqrt, 
    log(`AMBIENT TEMPRETURE` + 1) as amb_temp_log, 
    sqrt(`AMBIENT TEMPRETURE`) as amb_temp_sqrt
from weather;
select * from weather_transformed;


-------------------------------------------- SCALING
create table weather_scaled as
select 
    (GII - gii_min) / (gii_max - gii_min) as scaled_gii,
    (RAIN - rain_min) / (rain_max - rain_min) as scaled_rain,
    (`MODULE TEMP.1` - module_temp_min) / (module_temp_max - module_temp_min) as scaled_module_temp,
    (`AMBIENT TEMPRETURE` - amb_temp_min) / (amb_temp_max - amb_temp_min) as scaled_amb_temp
from (
    select GII, RAIN, `MODULE TEMP.1`, `AMBIENT TEMPRETURE`, 
        (select min(GII) from weather) as gii_min,
        (select max(GII) from weather) as gii_max,
        (select min(RAIN) from weather) as rain_min,
        (select max(RAIN) from weather) as rain_max,
        (select min(`MODULE TEMP.1`) from weather) as module_temp_min,
        (select max(`MODULE TEMP.1`) from weather) as module_temp_max,
        (select min(`AMBIENT TEMPRETURE`) from weather) as amb_temp_min,
        (select max(`AMBIENT TEMPRETURE`) from weather) as amb_temp_max
    from weather
) as scaled_data;

select * from weather_scaled;

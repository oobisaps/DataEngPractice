-- CREATE EXTERNAL TABLE
CREATE OR REPLACE EXTERNAL TABLE `green_taxi.external_green_taxi_2022`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://dataeng-zoomcamp-demo-bucket/green_taxi_data_2022/*']
);

-- CREATE MATERIALIZED TABLE FROM EXTERNAL
CREATE OR REPLACE TABLE `green_taxi.green_taxi_2022` AS
SELECT * FROM `green_taxi.external_green_taxi_2022`;

-- QUESTION 1
SELECT COUNT(*) FROM `green_taxi.green_taxi_2022`;

-- QUESTION 2
SELECT DISTINCT(pulocation_id) FROM `green_taxi.external_green_taxi_2022`;

SELECT DISTINCT(pulocation_id) FROM `green_taxi.green_taxi_2022`;

-- QUESTION 3
SELECT COUNT(*) FROM `green_taxi.green_taxi_2022` WHERE fare_amount = 0;

-- QUESTION 4
CREATE OR REPLACE TABLE `green_taxi.partitioned_clustered_green_taxi_2022`
PARTITION BY DATE(lpep_pickup_datetime)
CLUSTER BY pulocation_id AS
SELECT * FROM `green_taxi.green_taxi_2022`;

-- QUESTION 5
SELECT 
    DISTINCT(pulocation_id) 
FROM 
    `green_taxi.partitioned_clustered_green_taxi_2022` 
WHERE 
    DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-07-01'

SELECT 
    DISTINCT(pulocation_id) 
FROM 
    `green_taxi.green_taxi_2022` 
WHERE 
    DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-07-01';
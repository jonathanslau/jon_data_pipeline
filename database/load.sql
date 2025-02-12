-- clear tables
truncate table staging.car_price_dataset;
truncate table staging.cpi_gasoline;

-- load data into tables
copy staging.car_price_dataset from 'storage\raw\car-prices-dataset.csv';
copy staging.staging.cpi_gasoline from 'storage\raw\cpi_gasoline.csv';

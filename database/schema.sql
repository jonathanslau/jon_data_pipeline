-- create schemas

create schema if not exists staging;
create schema if not exists analysis;

-- table definitions

create table if not exists staging.car_price_dataset (
    brand varchar,
    model varchar,
    "year" int,
    engine_size decimal(3,1),
    fuel_type varchar,
    transmission varchar,
    mileage integer,
    doors tinyint,
    owner_count tinyint,
    price smallint
);


create table if not exists staging.cpi_gasoline (
    realtime_start date,
    realtime_end date,
    "date" date,
    "value" decimal(6,3),
    primary key ("date")
);

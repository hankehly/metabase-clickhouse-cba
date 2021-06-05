CREATE DATABASE IF NOT EXISTS coronavirus_cases_and_vaccinations;

-- Sample data: Coronavirus (COVID-19) Cases and Vaccinations
-- area_name,            area_code, date,       dose,     age_band,      age_higher, age_lower, cum_doses, new_doses, population, new_prop,            cum_prop
-- Barking and Dagenham, E09000002, 2020-12-08, 1st dose, 18 - 24 years, 24,         18,        0,         0,         18002,      0,                   0
-- Westminster         , E09000033, 2021-06-02, 2nd dose, 80+ years,     90,         80,        5260,      4,         9004,       4.44247001332741e-4, 0.5841848067525545

CREATE TABLE IF NOT EXISTS coronavirus_cases_and_vaccinations.phe_vaccines_age_london_boroughs
(
    area_name  String,
    area_code  String,
    date       Date,
    dose       String,
    age_band   String,
    age_higher Int64,
    age_lower  Int64,
    cum_doses  Int64,
    new_doses  Int64,
    population Int64,
    new_prop   Float64,
    cum_prop   Float64
)
    ENGINE = MergeTree()
        PARTITION BY toYYYYMM(date)
        ORDER BY (area_code, date)
AS
SELECT *
FROM file('/var/lib/clickhouse/user_files/phe_vaccines_age_london_boroughs.csv', 'CSV',
          'area_name String, area_code String, date Date, dose String, age_band String, age_higher Int64, age_lower Int64, cum_doses Int64, new_doses Int64, population Int64, new_prop Float64, cum_prop Float64')

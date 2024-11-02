CREATE SCHEMA IF NOT EXISTS public;

CREATE TABLE public.users (
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    user_email VARCHAR(255) NOT NULL,
    user_password VARCHAR(255) NOT NULL
);

CREATE TABLE public.properties (
    property_id SERIAL PRIMARY KEY,
    property_owner INT,
    street_name VARCHAR(255),
    street_number FLOAT,
    city VARCHAR(255),
    state VARCHAR(255),
    zipcode INT,
    property_type VARCHAR(255),
    FOREIGN KEY (property_owner) REFERENCES users(user_id)
);

CREATE TABLE public.multi_unit (
    property_id INT PRIMARY KEY,
    num_units INT,
    num_units_occupied INT,
    avg_rent FLOAT,
    overhead_monthly_cost FLOAT,
    FOREIGN KEY (property_id) REFERENCES properties(property_id)
);

CREATE TABLE public.single_family (
    property_id INT PRIMARY KEY,
    rent FLOAT,
    overhead_monthly_cost FLOAT,
    occupied BOOLEAN,
    FOREIGN KEY (property_id) REFERENCES properties(property_id)
);

CREATE TABLE public.duplex (
    property_id INT PRIMARY KEY,
    rent FLOAT,
    overhead_monthly_cost FLOAT,
    unit_1_occupied BOOLEAN,
    unit_2_occupied BOOLEAN,
    FOREIGN KEY (property_id) REFERENCES properties(property_id)
);
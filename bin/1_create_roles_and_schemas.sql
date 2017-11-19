-- This must be executed from the `marmot` database
CREATE ROLE marmot_admin WITH NOLOGIN;
CREATE ROLE marmot_app WITH LOGIN IN ROLE marmot_admin PASSWORD 'devPass789';

SET ROLE marmot_app;
CREATE SCHEMA resources;

GRANT ALL ON SCHEMA resources TO marmot_admin;

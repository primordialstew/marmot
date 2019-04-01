-- Before we can begin using Alembic, we must create the roles and database

CREATE ROLE marmot_admin WITH SUPERUSER;
CREATE ROLE marmot_alembic WITH LOGIN ROLE marmot_admin;
CREATE DATABASE marmot WITH OWNER marmot_alembic;
ALTER SCHEMA public OWNER TO marmot_alembic;

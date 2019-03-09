DROP DATABASE marmot;
DROP ROLE marmot_alembic;
DROP ROLE marmot_admin;


CREATE ROLE marmot_admin WITH SUPERUSER;
CREATE ROLE marmot_alembic WITH LOGIN ROLE marmot_admin;
CREATE DATABASE marmot WITH OWNER marmot_alembic;

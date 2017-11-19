-- return the `marmot` database state to baseline
DROP TABLE public.schemas CASCADE;
DROP SCHEMA resources CASCADE;

CREATE SCHEMA resources;
GRANT ALL ON SCHEMA resources TO marmot_admin;

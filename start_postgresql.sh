#!/bin/bash
sudo apt-get update
sudo apt-get install -y postgresql postgresql-contrib
sudo service postgresql start

# Switch to the postgres user and run psql commands
sudo su - postgres -c "psql -c \"DO \$\$ BEGIN IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = 'gitpod') THEN CREATE ROLE gitpod WITH LOGIN PASSWORD 'JimmyJam'; END IF; END \$\$;\""

sudo su - postgres -c "psql -c \"GRANT ALL PRIVILEGES ON DATABASE chinook TO gitpod;\""
sudo su - postgres -c "psql -c \"GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO gitpod;\""

# Create the database and import the SQL file
sudo su - postgres -c "createdb chinook"
sudo su - postgres -c "psql chinook < /workspace/SQL-/Chinook_PostgreSql.sql"

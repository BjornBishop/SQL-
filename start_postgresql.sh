#!/bin/bash
sudo apt-get update
sudo apt-get install -y postgresql postgresql-contrib
sudo service postgresql start

sudo -i -u postgres psql << EOF
DO \$\$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = 'gitpod') THEN
        CREATE ROLE gitpod WITH LOGIN PASSWORD 'JimmyJam';
        GRANT ALL PRIVILEGES ON DATABASE chinook TO gitpod;
        GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO gitpod;
    END IF;
END
\$\$;
EOF

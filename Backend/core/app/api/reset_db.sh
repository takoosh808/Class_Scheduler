#!/bin/bash

echo "Resetting PostgreSQL database: courseapp"
psql -U postgres <<EOF
DROP DATABASE IF EXISTS courseapp;
CREATE DATABASE courseapp WITH OWNER = admin ENCODING = 'UTF8';
\c courseapp
ALTER SCHEMA public OWNER TO admin;
GRANT ALL PRIVILEGES ON DATABASE courseapp TO admin;
GRANT ALL PRIVILEGES ON SCHEMA public TO admin;
EOF

echo "Done. Now run: python manage.py migrate"
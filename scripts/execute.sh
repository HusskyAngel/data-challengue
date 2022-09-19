#! /usr/bin/bash

docker cp  $1 some-postgres:punto_uno.sql
docker exec -u postgres some-postgres psql data postgres -f $1 

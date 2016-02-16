#!/bin/bash
python /app/marketplace/manage.py migrate

mod_wsgi-express start-server --working-directory /app/marketplace /app/marketplace/marketplace_of_ideas/wsgi.py &
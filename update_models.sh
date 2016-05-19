#!/bin/bash
rm *.db
rm -rf migrations
python manager.py db init
python manager.py db migrate -m 'modelos actualizado'
python manager.py db upgrade
python manager.py populate
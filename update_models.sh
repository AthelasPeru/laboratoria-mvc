#!/bin/bash
python manager.py db migrate -m 'modificacion'
python manager.py db upgrade
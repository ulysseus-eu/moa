#!/bin/bash
cd /home/app/moa
source /home/app/moa/.venv/bin/activate
MOA_CONFIG=ProductionConfig pipenv run python -m moa.models
chown app:app data/moa.db
deactivate
cd -
#!/bin/bash
sleep 30
cd /home/app/moa
source /home/app/moa/.venv/bin/activate
MOA_CONFIG=ProductionConfig pipenv run python -m moa.worker
deactivate
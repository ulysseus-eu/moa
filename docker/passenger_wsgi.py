import sys, os
from app import app as application

VENV = '/home/app/moa/.venv'
PYTHON_BIN = VENV + '/bin/python3'

if sys.executable != PYTHON_BIN:
    os.execl(PYTHON_BIN, PYTHON_BIN, *sys.argv)

sys.path.insert(0, VENV + '/lib/python3.8/site-packages')

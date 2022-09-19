from sqlalchemy import  text

import os 
from decouple import config

import re

from .connection import conn,logger_db


def start_execution():
    logger_db.info("ejecutando sql scripts")
    os.chdir(config('SCRIPTS_FOLDER'))
    for file in os.listdir():
        if re.search(r"*.sql",file) != None: 
            with open(file,'r') as f:
                conn.execute(text(f))

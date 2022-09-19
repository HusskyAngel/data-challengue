from sqlalchemy import create_engine
from sqlalchemy.engine import Engine 
from sqlalchemy.exc import SQLAlchemyError

from decouple import config

import logging

#logging config 
logger_db = logging.getLogger("db")
ch = logging.StreamHandler()
formatter = logging.Formatter( '%(name)s: %(levelname)s: %(message)s')
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
logger_db.addHandler(ch)


class _Conn():
    """
        create connection with the database, with .env file configuration  
    """
    def __init__(self):
        host=str(config('DB_HOST'))
        port=str(config('DB_PORT'))
        name=str(config('DB_NAME'))
        password=str(config('DB_PASSWORD'))
        user=str(config('DB_USER'))

        url='postgresql://{}:{}@{}:{}/{}'.format(user,password,host,port,name)
        self.engine= create_engine(url) 

        try:
            self.engine.connect()
            logger_db.info("Conexión creadada a la base de datos")
        except SQLAlchemyError as err:
            logger_db.error("error conectandose a la base de datos: "+str(err.__cause__))

    def conn_engine(self)->Engine:
        """
            return connection 
        """
        return  self.engine 

conn=_Conn().conn_engine()




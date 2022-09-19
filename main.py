import logging
from db.execute_sql import start_execution
from utils.get_data import  download_data

logging.basicConfig(filename='logs.log',filemode='w', encoding='utf-8', level=logging.DEBUG)



download_data("cines") 
start_execution()

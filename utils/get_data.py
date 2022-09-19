from datetime import date 
import os 
import requests
import logging
from decouple import config

#logging config
logger_data=logging.getLogger("csv data")
formatter = logging.Formatter( '%(name)s: %(levelname)s: %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
ch.setLevel(logging.INFO)
logger_data.addHandler(ch)


def download_data(data:str):
    """
    download data from env urls.  
    data-> str  -> {museos, cines, bibliotecas}  
    """
    #load urls 
    urls: dict
    try: 
        urls={  "museos": str(config('MUSEOS_URL')),
                "cines":str(config('CINES_URL')),
                "bibliotecas":str(config('BIBLIOTECAS_URL')),} 
    except ValueError: 
        logger_data.error('error cargando las urls desde el env')
        return None
    #get current date 
    today=date.today()
    month=today.strftime("%B")
    year=today.year
    path=os.path.join("data",data,str(year)+"-"+month)
    #test if the data already exists
    if os.path.isfile(os.path.join(path, data+"-"+today.strftime("%b-%d-%Y")+".csv")):  
        logger_data.debug ("Ya hay un archivo con la misma fecha, voy a eliminar el archivo.")
        os.remove(os.path.join(path, data+"-"+today.strftime("%b-%d-%Y")+".csv"))
    elif not os.path.isdir(path): 
        logger_data.debug ("creando path") 
        os.makedirs(path)
    #download and write data
    w=open(os.path.join(path,data+"-"+today.strftime("%b-%d-%Y")+".csv"),"bw+")
    logger_data.debug ("descargando la información de "+ urls[data])
    try:
        r=requests.get(urls[data],allow_redirects=True)
        w.write(r.content)
        w.close()
        logger_data.info("información descargada o actualizada")
    except ValueError:
        logger_data.error("error descargando el archivo")
        return None






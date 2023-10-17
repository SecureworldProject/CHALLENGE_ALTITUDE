from math import log10, sqrt
import cv2
# para instalar la libreria openCV simplemente:
# pip3 install opencv-python
# o bien py -m pip install opencv-python
# para aprender opencv https://www.geeksforgeeks.org/opencv-python-tutorial
import numpy as np
import os
from pathlib import Path
import time
#para instalar el modulo easygui simplemente:
#pip3 install easygui
# o bien py -m pip install easygui
#import easygui
from tkinter import messagebox
import lock
import json

# variables globales
# ------------------
props_dict={}
DEBUG_MODE=True

def init(props):
    global props_dict
    print("Python: Enter in init")
    
    #props es un diccionario
    props_dict= props
    
    # retornamos un cero como si fuese ok, porque
    # no vamos a ejecutar ahora el challenge
    return 0 # si init va mal retorna -1 else retorna 0
    

def executeChallenge():
    print("Starting execute")
    #for key in os.environ: print(key,':',os.environ[key]) # es para ver variables entorno
    folder=os.environ['SECUREMIRROR_CAPTURES']
    print ("storage folder is :",folder)
    
    # mecanismo de lock BEGIN
    # -----------------------
    lock.lockIN("GPS")

    # pregunta si el usuario tiene movil con capacidad GPS
    # -----------------------------------------------------
    #textos en español, aunque podrian ser parametros adicionales del challenge
    #conexion=easygui.ynbox(msg='¿Tienes un movil con bluetooth activo y emparejado con tu PC con capacidad GPS?', choices=("Yes","Not"))
    conexion=messagebox.askyesno('challenge MM: GPS','¿Tienes un movil con bluetooth activo emparejado a tu PC con capacidad GPS?')
    print (conexion)

    if (conexion==False):
        lock.lockOUT("GPS")
        print ("return key zero and long zero")
        key=0
        key_size=0
        result =(key,key_size)
        print ("result:",result)
        return result # clave cero, longitud cero

    #popup msgbox pidiendo interaccion
    #---------------------------------
    output = messagebox.showinfo("challenge MM: GPS",props_dict["interactionText"])
    # lectura del fichero capture.gps
    #-------------------------------
    # se supone que el usuario ha depositado un .gps usando bluetooth
    # el nombre del fichero puede ser siempre el mismo, fijado por el proxy bluetooth.
    # aqui vamos a "forzar" el nombre del fichero para pruebas
    filename="capture.gps"
    if (DEBUG_MODE==True):
        filename="test.gps"

    if os.path.exists(folder+"/"+filename):    
        with open(folder+"/"+filename) as cosa:
            geodata=json.load(cosa)
            print ("Geolocation data")
            print ("  Version:",geodata["version"])
            print ("  GPS:\t",geodata["gps"][0],"\n\t",geodata["gps"][1])
            print ("  Orientation:\t",geodata["orientation"][0],"\n\t\t",geodata["orientation"][1])
    else:
        print ("ERROR: el fichero de captura",filename," no existe")
        key=0
        key_size=0
        result =(key,key_size)
        print ("result:",result)
        lock.lockOUT("GPS")
        return result # clave cero, longitud cero  
   
    
    # una vez consumida, podemos borrar la captura (fichero "capture.gps")
    if (DEBUG_MODE==False):
        if os.path.exists(folder+"/"+filename):    
            os.remove(folder+"/"+filename)        
    
    
    #mecanismo de lock END
    #-----------------------
    lock.lockOUT("GPS")
    
    #procesamiento
    lon=geodata["gps"][0]["lon"] # primera toma de GPS, componente longitud
    lat=geodata["gps"][0]["lat"] # primera toma de GPS, componente latitud
    alt=geodata["gps"][0]["alt"] # primera toma de GPS, componente altura
    cuantized_lon=float(lon)
    cuantized_lon=int(lon/10.0)
    cuantized_lat=float(lat)
    cuantized_lat=int(lat/10.0)
    cuantized_alt=float(alt)
    cuantized_alt=int(alt/10.0)
    
    y=geodata["orientation"][0]["y"]
    cuantized_orient=int(float(y/45.0)) 

    print ("lon es ", cuantized_lon)
    print ("lat es ", cuantized_lat)
    print ("alt es ", cuantized_alt)
    print ("orient es ", cuantized_orient)

    #construccion de la respuesta
    cad="%d%d%d"%(cuantized_lon, cuantized_lat, cuantized_alt)
    key = bytes(cad,'utf-8')
    key_size = len(key)
    result =(key, key_size)
    print ("result:",result)
    return result


if __name__ == "__main__":
    midict={"interactionText": "Por favor haz una captura de datos de geolocalización.", "param2":3}
    init(midict)
    executeChallenge()


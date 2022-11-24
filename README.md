# ChallengeMM_GPS
este challenge cuantiza la altitud obtenida en tramos de 100 metros y tambien cuantiza la orientacion


# DESCRIPCION y FIABILIDAD
GPS es un challenge que piden al usuario hacer una captura de tipo geolocation para comprobar que se encuentra en un lugar concreto
el challenge obtiene la altitud de la primera medida que contiene el geolocation y la cuantiza en tramos de 100 m
el challenge tiene una fiabilidad media porque el usuario puede saber a que altura esta el emplazamiento "correcto", pero es muy dificil forzar el resultado GPS del altimetro. Es facil forzar la orientacion colocando el movil en la posicion esperada, pero no la altura

# FUNCIONAMIENTO:
si estas a 666 metros, retorna un "6" en altitud ( aprox 10 valores posibles)
en cuanto la orientacion cuantiza en tramos de 45 grados ( 8 valores posibles)


# requisitos:
la variable de entorno **SECUREMIRROR_CAPTURES** debe existir y apuntar al path donde el server bluetooth deposita las capturas
el fichero de captura se debe llamar "capture.geo".

Hay una variable en el challenge  llamada **"DEBUG_MODE"** que la puedes cambiar a True o False. En caso True en lugar del fichero capture.geo se usa test.geo y ademas no se borra el fichero capture.geo despues de procesar. 

ejemplo de configuracion json:
``` 
{
"FileName": "challenge_loader_python.dll",
"Description": "check location",
"Props": {
  "module_python": "GPS",
  "validity_time": 3600,
  "refresh_time": 10,
  "interactionText": "Por favor haz una captura de datos de geolocation",
  },
"Requirements": "location sensors" 
}
```


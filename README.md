# CHALLENGE_ALTITUDE
este challenge cuantiza la altitud obtenida en tramos de 100 metros


# DESCRIPCION y FIABILIDAD
ALTITUDE es un challenge que piden al usuario hacer una captura de tipo geolocation para comprobar que se encuentra en un lugar concreto
el challenge obtiene la altitud de la primera medida que contiene el geolocation y la cuantiza en tramos de 100 m
el challenge tiene una fiabilidad baja porque el usuario puede saber a que altura esta el emplazamiento "correcto"

# FUNCIONAMIENTO:
si estas a 666 metros, retorna un "600"
la clave son 3 digitos en general de modo que hablamos de unas 1000 posibilidades


# requisitos:
la variable de entorno **SECUREMIRROR_CAPTURES** debe existir y apuntar al path donde el server bluetooth deposita las capturas
el fichero de captura se debe llamar "capture.geo".

Hay una variable en el challenge  llamada **"DEBUG_MODE"** que la puedes cambiar a True o False. En caso True en lugar del fichero capture.geo se usa test.geo y ademas no se borra el fichero capture.geo despues de procesar. 


Lanzada por el usuario admin
Running as SYSTEM
Ejecutando. en el espacio de trabajo C:\ProgramData\Jenkins\.jenkins\workspace\PruebaGET_RestAPI
[PruebaGET_RestAPI] $ "C:\Program Files\Git\bin\bash.exe" -xe C:\Windows\TEMP\jenkins18337379759920674411.sh
++ curl -s -X GET http://localhost:5000/alumnos
+ response='[
  {
    "domicilio": "Calle Falsa",
    "edad": 20,
    "nombre": "Juan",
    "telefono": "1234567890"
  }
]'
+ echo '[
  {
    "domicilio": "Calle Falsa",
    "edad": 20,
    "nombre": "Juan",
    "telefono": "1234567890"
  }
]'
+ grep -q '"nombre": "Juan"'
+ echo 'Prueba GET exitosa: Lista de alumnos obtenida correctamente'
Prueba GET exitosa: Lista de alumnos obtenida correctamente
+ exit 0
Finished: SUCCESS

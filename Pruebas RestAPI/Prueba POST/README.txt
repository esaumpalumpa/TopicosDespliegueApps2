Lanzada por el usuario admin
Running as SYSTEM
Ejecutando. en el espacio de trabajo C:\ProgramData\Jenkins\.jenkins\workspace\PruebaPOST_RestAPI
[PruebaPOST_RestAPI] $ "C:\Program Files\Git\bin\bash.exe" -xe C:\Windows\TEMP\jenkins12146355085324788026.sh
++ curl -s -X POST -H 'Content-Type: application/json' -d '{"nombre": "Juan", "edad": 20, "domicilio": "Calle Falsa", "telefono": "1234567890"}' http://localhost:5000/alumnos
+ response='{
  "alumno": {
    "domicilio": "Calle Falsa",
    "edad": 20,
    "nombre": "Juan",
    "telefono": "1234567890"
  },
  "mensaje": "Alumno agregado"
}'
+ echo '{
  "alumno": {
    "domicilio": "Calle Falsa",
    "edad": 20,
    "nombre": "Juan",
    "telefono": "1234567890"
  },
  "mensaje": "Alumno agregado"
}'
+ grep -q 'Alumno agregado'
+ echo 'Alumno agregado correctamente'
Alumno agregado correctamente
+ exit 0
Finished: SUCCESS

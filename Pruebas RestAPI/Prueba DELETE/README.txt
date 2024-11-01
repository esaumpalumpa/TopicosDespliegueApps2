Lanzada por el usuario admin

Running as SYSTEM
Ejecutando. en el espacio de trabajo C:\ProgramData\Jenkins\.jenkins\workspace\PruebaDELETE_RestAPI
[PruebaDELETE_RestAPI] $ "C:\Program Files\Git\bin\bash.exe" -xe C:\Windows\TEMP\jenkins7349141975445449886.sh
++ curl -s -X DELETE http://localhost:5000/alumnos/0
+ response='{
  "alumno": {
    "domicilio": "Calle Nueva 456",
    "edad": 21,
    "nombre": "Juan Actualizado",
    "telefono": "9876543210"
  },
  "mensaje": "Alumno eliminado"
}'
+ echo '{
  "alumno": {
    "domicilio": "Calle Nueva 456",
    "edad": 21,
    "nombre": "Juan Actualizado",
    "telefono": "9876543210"
  },
  "mensaje": "Alumno eliminado"
}'
+ grep -q 'Alumno eliminado'
+ echo 'Prueba DELETE exitosa'
Prueba DELETE exitosa
+ exit 0
Finished: SUCCESS

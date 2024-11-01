Lanzada por el usuario admin

Running as SYSTEM
Ejecutando. en el espacio de trabajo C:\ProgramData\Jenkins\.jenkins\workspace\PruebaPUT_RestAPI
[PruebaPUT_RestAPI] $ "C:\Program Files\Git\bin\bash.exe" -xe C:\Windows\TEMP\jenkins5245349439386714687.sh
++ curl -s -X PUT -H 'Content-Type: application/json' -d '{"nombre": "Juan Actualizado", "edad": 21, "domicilio": "Calle Nueva 456", "telefono": "9876543210"}' http://localhost:5000/alumnos/0
+ response='{
  "alumno": {
    "domicilio": "Calle Nueva 456",
    "edad": 21,
    "nombre": "Juan Actualizado",
    "telefono": "9876543210"
  },
  "mensaje": "Alumno actualizado"
}'
+ echo '{
  "alumno": {
    "domicilio": "Calle Nueva 456",
    "edad": 21,
    "nombre": "Juan Actualizado",
    "telefono": "9876543210"
  },
  "mensaje": "Alumno actualizado"
}'
+ grep -q 'Alumno actualizado'
+ echo 'Prueba PUT exitosa: Alumno actualizado correctamente'
Prueba PUT exitosa: Alumno actualizado correctamente
+ exit 0
Finished: SUCCESS


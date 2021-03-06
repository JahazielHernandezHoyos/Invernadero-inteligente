#actualizar datos con pyt request python
import requests
import time

#el numero 200 en la terminal es que fue exitoso
#obtiene los datos de la pagina y los imprime en consola tanto si tuvo exito en la peticion como si no como tambien su contenido
obtener = requests.get('http://localhost:4000/numerosRaspberry')
print(obtener.status_code)
print(obtener.content)

#datos que se van a pasar para enviar
nivelDeHumedad = 10
nivelLuz = "100%"
nivelTemperatura = "100°C"

#envios y actualizaciones de los datos

#envio de datos de nivel de humedad
response = requests.put("http://localhost:4000/numerosRaspberry/1", data = {"id": 1,  "nivel": nivelDeHumedad, "area": "Nivel Humedad"})
print(response.status_code)
        
#envio de datos de nivel de luz
response = requests.put("http://localhost:4000/numerosRaspberry/2", data = {"id": 2,  "nivel": nivelLuz, "area": "Nivel Luz"})
print(response.status_code)

#envio de datos de nivel de area
response = requests.put("http://localhost:4000/numerosRaspberry/3", data = {"id": 3,  "nivel": nivelTemperatura, "area": "Nivel Temperatura"})
print(response.status_code)

obtener = requests.get('http://localhost:4000/numerosRaspberry')
print(obtener.content)



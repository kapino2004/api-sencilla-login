Bueno, aquí presento mi proyecto. Básicamente, armé una API REST sencilla usando FastAPI y SQLModel para gestionar usuarios (CRUD: crear, leer, actualizar y borrar).

 Arme también un pequeño script en Python (atacante.py). Este amiguito usa la magia de la librería itertools para lanzar un ataque de fuerza bruta directo a la puerta del login.

Como empezar?
Es fácil, solo hay que seguir estos pasos en la terminal:

Primero, creamos nuestra caja aislada (el entorno virtual):
python -m venv venv

La encendemos:
.\venv\Scripts\activate

Instalamos las herramientas que necesitamos:
pip install -r requirements.txt

Despertamos a la API:
uvicorn main:app --reload

Y ahora abrimos una terminal nueva (sin cerrar la anterior) y lanzamos el ataque:
python atacante.py

Lo que aprendí de todo este desastre (Análisis y Mitigación) 
El tiempo y los recursos de la compu:  El script que ataca va a toda máquina, prueba cientos de combinaciones por segundo gracias a lo optimizado que está itertools para las matemáticas. Descubrir una clave devil de 3 letras (como eco) le toma literal un par de segundos.
Pero me di cuenta de algo muy interesante al hacer esto: procesar toda esa lluvia de peticiones falsas hace que el procesador de mi máquina empiece a sudar. Así que, sin querer queriendo, terminé demostrando cómo funciona un ataque de Denegación de Servicio (DoS) colateral. ¡El servidor se ahoga intentando rechazar a tantos intrusos!

¿Cómo nos protegemos de esto en la vida real?
Viendo lo increíblemente fácil que fue entrar, yo aplicaría sí o sí estas cuatro medidas para no dejarle la puerta abierta a nadie:

Rate Limiting (o sea, calmar un poco a la gente): Bloquear temporalmente a cualquier IP que intente hacer login más de 10 veces por minuto. Nadie normal se equivoca tantas veces tan rápido.

Bloqueo de cuentas: Congelar la cuenta del usuario "admin" si vemos que metió mal la contraseña 5 veces seguidas.

Cifrado de verdad: Guardar las claves en texto plano en la base de datos es un suicidio. Hay que usar librerías como Passlib (con algoritmos pesados como Bcrypt) para que, si alguien logra robar la base de datos, solo vea un revoltijo de letras sin sentido.

Claves más difíciles, por favor: Poner una regla en el registro (POST /users) que obligue a crear contraseñas de al menos 8 caracteres. Con eso, a mi pobre script de fuerza bruta le tomaría años adivinarla.

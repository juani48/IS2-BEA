# IS2-BEA
## Instalar python
Ve a python.org/downloads.

Haz clic en "Download Python 3.x.x" (la versión más reciente).

Verificala la instalacion abriendo la terminal (cmd o PowerShell) y escribe:: `python --version`.

## Crear entrono virtual

En la terminal usar `python -m venv ".venv"`

## Activar entorno virtual
Desde VSCODE usar `Ctrl`+`Shift`+`P` para abrir la paleta de comandos y seleccionar el interprete (buscar opcion `Python: Seleccionar interprete`) `./venv/bin/python3`.

> En linux tuve que instalar `python3-venv` y `python3-pip`, y usar el comando `source ./.venv/bin/activate`. Capa a alguno le sirve.

## Instalar paquetes al entorno
```bash
pip3 install package_name
```
## Paquetes del proyecto

Puedes generar este archivo desde los paquetes ya instalados en tu entorno virtual ejecutando el comando `pip freeze > requirements.txt`.

Una vez creado el archivo `requirements.txt`, puedes instalar todos los paquetes necesarios en un nuevo entorno virtual ejecutando `pip install -r requirements.txt`.

# Framework
Deje un archivo `app.py` con un ejemplo de como funciona `flask`.

Flask es un Microframeworks flexible, sin dependencias externas obligatorias. Vi que es ideal para aplicaciones pequeñas. 

Para bases de datos necesitariasmos instalar `Flask-SQLAlchemy` por ejemplo.

Con `flask run` o `python app.py` deberia iniciarse el programa (hay que estar parado en la carpeta del proyecto y con el entorno virtual activado) y salir un mensaje por termina `* Running on http://127.0.0.1:5000/`.

Si se ingresa es url se accede a la pagina.

Para frenar la ejecucion se tiene que usar la combinaicon de teclas: `Ctrl`+`C`.
## Bases de datos
### Paquete
```bash
pip install flask-sqlalchemy
```
### [Go to README data ](data/README.md) 

## HTML
### Paquete
```bash
pip install flask
```
### Estructura de archivos
```
tu_proyecto/
├── app.py
├── templates/
│   ├── index.html
│   ├── usuario.html
│   └── base.html (opcional)
└── static/ (para CSS/JS)
```
### Uso
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Busca en la carpeta 'templates'

@app.route('/usuario/<nombre>')
def usuario(nombre):
    return render_template('usuario.html', nombre_usuario=nombre)  # Pasar variables
```
### Usar Variables
```html
<!DOCTYPE html>
<html>
<head>
    <title>Usuario</title>
</head>
<body>
    <h1>Hola {{ nombre_usuario }}</h1>
    
    <!-- Condicionales -->
    {% if nombre_usuario == 'Admin' %}
        <p>Tienes privilegios de administrador.</p>
    {% else %}
        <p>Eres un usuario normal.</p>
    {% endif %}

    <!-- Bucles -->
    <ul>
    {% for item in ['Python', 'Flask', 'HTML'] %}
        <li>{{ item }}</li>
    {% endfor %}
    </ul>
</body>
</html>
```
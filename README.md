# IS2-BEA
## Instalar python
Ve a python.org/downloads.

Haz clic en "Download Python 3.x.x" (la versión más reciente).

Verificala la instalacion abriendo la terminal (cmd o PowerShell) y escribe:: `python --version`.

## Activar entorno virtual
Desde VSCODE usar `Ctrl`+`Shift`+`P` para abrir la paleta de comandos y seleccionar el interprete (buscar opcion `Python: Seleccionar interprete`) `./venv/bin/python3`.
## Instalar paquetes al entorno
```bash
pip3 install package_name
```
## Framework
Deje un archivo `app.py` con un ejemplo de como funciona `flask`.

Flask es un Microframeworks flexible, sin dependencias externas obligatorias. Vi que es ideal para aplicaciones pequeñas. 

Para bases de datos necesitariasmos instalar `Flask-SQLAlchemy` por ejemplo.

Con `flask run` o `python app.py` deberia iniciarse el programa (hay que estar parado en la carpeta del proyecto y con el entorno virtual activado) y salir un mensaje por termina `* Running on http://127.0.0.1:5000/`.

Si se ingresa es url se accede a la pagina.

Para frenar la ejecucion se tiene que usar la combinaicon de teclas: `Ctrl`+`C`.
# POST
Para el envio de datos desde la UI (un archivo html), usaremos archivos `.json` y codigo JavaScript. Para esto debemos declarar una seccion de `<script>` dentro del archivo `.html` o en su defecto tener un script aparte `.js` que sea invocado en esta seccion.

Nuestro objetivo es tener funciones en JavaScript que nos permitan enviar datos entre el front y el back, para esto debemos usar `fetch` de la siguiente forma:

```html
<!DOCTYPE html>
<html>
    <body> 
        <input type= "text" id= "id">
        <button onclick="modulo()">Boton</button>
    </body>

    <script>
        function modulo(){
            // Obtener el dato
            var variable = document.getElementById("id").value;

            // Realizar el envio de datos
            fetch("/url", // url del metodo de python
                {
                    method: "POST", // tipo de conexion
                    headers: { "Content-Type": "application/json" }, // formato
                    body: JSON.stringify( { variable: variable} ) // enviaremos un .json
                }
            )
            .then(response => response.json())
        }
    </script>
</html>
```

`<button>` sera el encargado de iniciar la cadena de eventos de nuestro codigo, ya que al ser presionado llamara a la funcion `modulo()`. La cual sera encargada de enviar los datos.

Con `document.getElementById("id").value;` obtendermos el valor ingresado en `<input>` y lo almacenaremos en una variable.

Para realizar el envio de los datos usaremos la instruccion `fetch(...)` que utiliza varios parametros:
1. `"/url"`: Es la url del metodo en el archivo Python que se encargara de realizar las operaciones de procesamiento.
2. `{ ... }`: Es una especie de json en la que debemos respetar en siguiente formato:
  - `method: "POST"`: Establece el tipo de conexion, veremos que la funcion de Python a la que nos conectaremos debe definir lo mismo.
  -  `headers: { "Content-Type": "application/json" }`: Es el formato de envio, debe ser el mismo para todas las conexiones.
  -  `body: JSON.stringify( { variable: variable} )`: Es el envio del json como tal. Dentor de `stringify(...)` armaremos el json con las variables y datos que necesitemos.
3. `.then(response => response.json())`: No es un parametro como tal. Es la respuesta que debe enviar la funcion de Python con la que nos conectamos, se puede recibir un `.json` o un `.html` como respuesta.

# Archivo .py
La configuracion necesaria para la recepcion de datos desde la UI en un metodo de Pthon es la siguiente:

```python
from flask import jsonify, request

@app.route("/url", methods=["GET", "POST"])
def login():
    request_value = request.get_json("variable") # obtener dato
    # procesamiento de datos
    return jsonify({"response": response}), 200
```

Observar que en el encabezado del metodo definir la url y el timpo de metodo, `POST` es necesario para la recepcion de datos desde la UI y `GET` se utiliza para enviar una respuesta.

Con `request.get_json("variable")` recivimos el dato enviado desde el script de JavaScript (el nombre de `"variable"` debe ser el mismo que el de la variable envia desde el script)

Luego de procesar el dato, usaremos `return jsonify({"response": response}), 200` para enviar una respuesta, en este caso en formato `.json`, pero podriamos enviar un archivo `.html`, un texto o directamente un numero. El entero `200` inidica que la conexion fue exitosa y que se envian datos de respuesta, en caso de respuesta exitosa sin datos de retorno, el `return` seria el siguiente:
```python
return "", 204
```
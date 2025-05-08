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
    request_value = request.get_json() # obtener dato
    # procesamiento de datos
    return jsonify({"response": response}), 200
```

Observar que en el encabezado del metodo definir la url y el timpo de metodo, `POST` es necesario para la recepcion de datos desde la UI y `GET` se utiliza para enviar una respuesta.

Con `request.get_json()` recivimos el dato enviado desde el script de JavaScript. Para acceder a los datos enviados en el `.json`, simplemente usaremos `request_value.get("variable")` de esta forma accederemos a la informacion de un campo del `.json`

Luego de procesar el dato, usaremos `return jsonify({"response": response}), 200` para enviar una respuesta, en este caso en formato `.json`, pero podriamos enviar un archivo `.html`, un texto o directamente un numero. El entero `200` inidica que la conexion fue exitosa y que se envian datos de respuesta, en caso de respuesta exitosa sin datos de retorno, el `return` seria el siguiente:
```python
return "", 204
```

# Envio de datos 
Es posible enviar datos a archivos `.html` por medio de las url, existen dos formas, con parametros o url:

## Parametros
Dentro de nuestro archivo `.py` debemos tener a siguiente extructura:
```python
@app.route('/url')
def function():
    return render_template('archivo.html', variable="62")
```
Y en uestro archivo `.html`:
```html
<!DOCTYPE html>
<html>
<body>
    <h1>Archivo con variable</h1>
    <p>La variable es: {{variable}}</p>
</body>
</html>
```

Si dentro de un archivo `.html` ponemos `{{ ... }}`, lo tomara como codigo Python. El nombre `{{variable}}` debe coincidir con el parametro `variable=62` del metodo `render_template(...)`, mientras que el primer parametro debe inidicar el nombre del archivo `.html` que se debe cargar.

## URL
Para este envio de datos necesitamos la siguiente configuracion:
```python
@app.route('/url/<var>') # La url deberia ser: '/url/62'
def function(var):
    return render_template('archivo.html', variable=var)
```
El archivo `.html` debe mantenerse igual. En este caso, el valor sera enviado mediante la url, siendo ingresado por el navegador; se debe tener en cuenta que el nombre de la url (`<var>`) debe coincidir con el del parametro de la funcion, el resto de la configuracion es igual al caso anterior.

> Creo que hay forma de enviar por url desde codigo.

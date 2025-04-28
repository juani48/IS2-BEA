# Crear el Engine
Lo primero que hay que hacer para trabajar con SQLAlchemy es crear un `engine`. El `engine` es el punto de entrada a la base de datos, es decir, el que permite a SQLAlchemy comunicarse con esta.

El motor se usa principalmente para manejar dos elementos: los pools de conexiones y el dialecto a utilizar.

Para esto, dentro de nuestro archivo `config.py`:
```python
import os	
from sqlalchemy import create_engine

DB_PATH = os.path.abspath(os.path.dirname(__file__))
DB_FILE = "database.db"
engine = create_engine(f"sqlite:///{os.path.join(DB_PATH, 'db', DB_FILE)}")
```
Como puedes observar, a la función `create_engine()` se le pasa la cadena de conexión a la base de datos. En este caso, la cadena de conexión a la base de datos SQLite es `"sqlite:///{os.path.join(DB_PATH, 'db', DB_FILE)}"`.

Crear el `engine` no hace que la aplicación se conecte a la base de datos inmediatamente, este hecho se pospone para cuando es necesario.

# Sesiones
Una vez creado el `engine`, lo siguiente que debes hacer para trabajar con SQLAlchemy es crear una sesión. Una sesión viene a ser como una transacción, es decir, un conjunto de operaciones de base de datos que, bien se ejecutan todas de forma atómica, bien no se ejecuta ninguna (si ocurre un fallo en alguna de las operaciones).

Desde el punto de vista de SQLAlchemy, una sesión registra una lista de objetos creados, modificados o eliminados dentro de una misma transacción, de manera que, cuando se confirma la transacción, se reflejan en base de datos todas la operaciones involucradas (o ninguna si ocurre cualquier error).

Para esto, dentro de nuestro archivo `config.py` agregamos:
```python
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()
```
Para crear una sesión se utiliza el método factoría `sessionmaker()` asociado a un `engine`. Después de crear la factoría, objeto `Session`, hay que hacer llamadas a la misma para obtener las sesiones, objeto `session`.

# Crear los modelos
En este punto, ya tiene casi todo listo para interactuar con el ORM. Ahora le voy a conocer donde realmente ocurre la magia: los modelos.

Los modelos son las clases que representan las tablas de base de datos. Por tanto, dado que esta usando un ORM, tiene que crear el modelo (o clase) equivalente a las u objetos a representar.

Para que se pueda realizar el mapeo de forma automática de una clase a una tabla, y viceversa, vamos a utilizar una clase base en los modelos que implementa toda esta lógica.

Para esto, dentro de nuestro archivo `config.py` agregamos:
```python
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
```
Al final del mismo hemos creado una clase llamada `Base` con el método `declarative_base()`. Esta clase será de la que hereden todos los modelos y tiene la capacidad de realizar el mapeo correspondiente a partir de la meta información (atributos de clase, nombre de la clase, etc.) que encuentre, precisamente, en cada uno de los modelos.

# config.py
```python
# Crear el Engine
import os	
from sqlalchemy import create_engine

DB_PATH = os.path.abspath(os.path.dirname(__file__))
DB_FILE = "database.db"
engine = create_engine(f"sqlite:///{os.path.join(DB_PATH, 'db', DB_FILE)}")

# Sesiones
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

# Crear los modelos
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
```

# Gestion de base de datos
## Crear tablas
Una vez definidos los modelos, hay que crear las tablas correspondientes.

En nuestro caso usaremos el archivo `AppDataBase.py`. En este archivo será donde escribas el código para gestionar la base de datos.
```python
from config import Base, engine
from Model import ClassModel

if __name__ == "__main__":
    Base.metadata.create_all(engine)
```
Lo importante en este punto es la línea `Base.metadata.create_all(engine)`. En ella estamos indicando a SQLAlchemy que cree, si no existen, las tablas de todos los modelos que encuentre en la aplicación. Sin embargo, para que esto ocurra es necesario que cualquier modelo se haya importado previamente antes de llamar a la `función create_all()`.
> ClassModel representa la clase implementada que es mappeada a su respectiva tabla de la base de datos

## Insertar registros
```python
from config import Base, engine, session
from Model import ClassModel

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    new_instance = ClassModel(variable = valor, ...)
    session.add(new_instance)
    session.commit()
```
Tambien es posible usar `session.add_all([])` y enviar por parametro una lista (`[]`) de los elementos a insertar.

`session.commit()` se utiliza para cerrar la sesion y guardar los datos en la base de datos.

## Consultar registros
Las consultas devuelven modelos

Una vez que te he mostrado cómo guardar datos en la base de datos usando el ORM de SQLAlchemy, en esta última parte del tutorial vas a descubrir cómo hacer los principales tipos de consultas.

Las consultas a la base de datos se realizan fundamentalmente a través de la función `query` del objeto `session`. Esta función recibe como parámetro el nombre de la clase sobre la que realizar las consultas y devuelve un objeto `Query` con la consulta a realizar.
```python
session.query(ClassModel)
```
### Obtener un objeto a partir de su primary_key
```python
session.query(ClassModel).get(1) # 1 es el valor del atributo definido como primary_key
```
El método `get()` devuelve un objeto del tipo indicado en la `Query` a partir de su `primary_key`. Si no encuentra el objeto, devuelve `None`.

### Obtener los objetos de una consulta
Para obtener todos los objetos de un tabla o consulta, simplemente hay que llamar al método `all()`. Este método devuelve una lista con los objetos devueltos por la consulta:
```python
session.query(ClassModel).all()
```
También puedes llamar al método `first()`. El método `first()` devuelve el primer objeto encontrado por la consulta. Es útil si sabes que solo existe un elemento que cumpla una determinada condición.

### Contar el número de elementos devueltos por una consulta
Si quieres contar el número de elementos que devuelve una consulta, utiliza el método `count()`:
```python
session.query(ClassModel).count()
```

### Aplicar filtros a una consulta
Para aplicar un filtro a una consulta, lo que sería la cláusula `WHERE` de SQL, puedes llamar al método `filter_by(keyword)`:
```python
session.query(ClassModel).filter_by(variable = valor).first()
```
Para aplicar un filtro a una consulta, lo que sería la cláusula `WHERE` de SQL, puedes llamar al método `filter()`:
```python
session.query(ClassModel).filter(ClassModel.variable < valor).all()
```
## Actualizar registros
El método `update()` le permite actualizar la fila del registro, tratando las columnas como un tipo diccionario:
```python
session.query(ClassModel).filter(ClassModel.variable == valor).update({ClassModel.varaible: valor})
session.commit()
```

## Eliminar registros
El método `delete()` le permite eliminar el registro en base a la clave primaria:
El método `update()` le permite actualizar la fila del registro, tratando las columnas como un tipo diccionario:
```python
session.query(ClassModel).filter(ClassModel.variable == valor).delete()
session.commit()
```

# Relaciones entre modelos con SQLAlchemy
## Relación uno a uno
Este tipo de relación ocurre cuando un solo registro de una tabla se relaciona con un solo registro de otra tabla. En el siguiente ejemplo se tiene una tabla persona que guardará los datos personales y dos tablas, `profesor` y `alumno` cada una de las cuales está asociada a la tabla persona a través de la
clave foránea `personaId`.

Para representar esta relación primero es necesario definir la columna `personaId` correspondiente a la clave foránea en la tabla `alumno`:
```python
class Alumno(db.Model):
    alumnoId = db.Column(db.Integer, primary_key=True)
    personaId = db.Column(db.Integer, db.ForeignKey('persona.personaId'), nullable=False) #Definición de clave foranea
    plan = db.Column(db.Integer, nullable=False)
```
En este caso creamos una columna tipo entero a la que le especificamos su naturaleza de clave foránea mediante la clase `ForeingKey`. A esta clase se le pasa por parámetro en nombre de la tabla con la que se relaciona seguida por la clave primaria de dicha tabla. Repetimos dicho proceso en la tabla profesor:
```python
class Profesor(db.Model):
    profesorId = db.Column(db.Integer, primary_key=True)
    personaId = db.Column(db.Integer, db.ForeignKey('persona.personaId'), nullable=False) #Definición de clave foranea
    numEmpleado = db.Column(db.Integer, nullable=False)
```
Esto ha definido las columnas correspondientes a la clave foránea entre las tablas pero no ha definido la relación entre ambas tablas para poder relacionar los objetos en nuestro código. Para ello es necesario especificar estas relaciones en todas las tablas.

Para el modelo correspondiente a la tabla `persona` es necesario cargar dos relaciones utilizando la función `relationship`, la que especifica la relación con la clase `Alumno` y la que especifica la relación con la clase `Profesor`:
```python
class Persona(db.Model):
    personaId = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable=False)
 
    # Relaciones
    profesor = db.relationship('Profesor',uselist=False,
    back_populates="persona",cascade="all, delete-orphan",single_parent=True)
    alumno = db.relationship('Alumno',uselist=False,
    back_populates="persona",cascade="all, delete-orphan",single_parent=True)

```
El primer parámetro de la función `relationship` representa la clase con la que se está creando en la relación.

El parámetro `uselist` es un valor booleano que indica si se quiere que el valor obtenido de la relación sea una lista. En este caso, como la relación es uno a uno y al cargar una persona se traerá solo un profesor o un alumno este valor es configurado como `False`.

El parámetro `back_populates` indica el nombre de la relación en la dirección inversa. Es decir, el modelo `Persona` se relaciona con `Profesor` a través del atributo llamado `profesor` y a su vez el modelo `Profesor` se relacionará con el modelo `Persona` a través de un atributo llamado `persona`.

El parámetro `cascade` define el comportamiento en cascada de las tablas con respecto a sus relaciones. Se especifica como una lista de reglas separadas por coma, las reglas disponibles son `save-update`, `merge`, `expunge`, `delete`, `delete-orphan` y `refresh-expire`. Una manera de aplicar todas estas reglas de una manera más reducida es colocar la regla all que incluye a todas las nombradas anteriormente excepto `delete-orphan` que debe colocarse por separado. Una descripción más completa de la funcionalidad `cascade` puede encontrarse en la documentación oficial.



# El encargado de las consultas SQL
from config import Base, engine, session
from UserModel import UserModel

if __name__ == "__main__":
    #Base.metadata.create_all(engine)
    #print("¡Creación exitosa de la tabla productos!\n")
    nuevo_usuario = UserModel(dni = 4, email='juanB@ejemplo.com', name='Juan Pérez')
    session.add(nuevo_usuario)
    session.commit()
    print(session.query(UserModel).all())
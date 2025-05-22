import bcrypt

## Contraseña introducida por el usuario
password = "2323"
print(password)
password_encode= password.encode('utf-8')

##genera salt y crea el hash
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password_encode, salt)
#hashed_password lista para almacenar
print("Hash generado:", hashed_password)

if bcrypt.checkpw(password_encode, hashed_password):
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")

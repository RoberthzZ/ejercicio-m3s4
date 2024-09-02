lista_contactos = [("juan perez", "juanperez@gmail.com"), ("maria cortes", "mariacortes@gmail.com"), ("roberto maya","robertomaya@gmail.com"),] # tuplas

def agregar_contacto(nombre, email): # definir la funcion para almacenar nombre y correo
    nuevo_contacto = (nombre, email) # variable que almacena la informacion
    lista_contactos.append(nuevo_contacto) # agrega la informacion al final de la tupla
    print(f"contacto agregado: {nuevo_contacto}") # incrusta expresiones en una cadena de texto
    print(lista_contactos) # imprime la lista de contactos
from .gestion import lista_contactos # se agrega un punto para inf que esta en la misma carpeta

def buscar_contacto(nombre): # define la funcion para la busqueda
    resultados =[contacto for contacto in lista_contactos if nombre in contacto[0]] #crea una lista basada en una existente para encomntrar los nombres que coincidan
    
    return resultados #devuelve el valor

if __name__ == "__main__": # name es una variable que tiene el valor de main
    nombre_a_buscar = input() # captura y almacena lo ingresado
    contactos_encontrados = buscar_contacto(nombre_a_buscar) #llama la funcion buscar_contacto y almacena lo encontrado en la var contactos_encontrados
    
    if contactos_encontrados: # sentencia condicional
        print("contactos_encontrados:") # var
        for contacto in contactos_encontrados: # bucle de iteracion sobre la lista
            print(contacto) # imprime el valor de contacto
            
    else:
        print("no se encontraron contactos") # idem
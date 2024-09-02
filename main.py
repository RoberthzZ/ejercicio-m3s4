from contactos import gestion # del paquete (carpeta) contactos importe el archivo gestion
from contactos import busqueda

def mostrar_contactos(): # define la funcion
    print("todos los contactos:") # imprime todos los contactos
    for contacto in gestion.lista_contactos: # bucle que itera sobre lista_contactos
        print(contacto) # idem
        
def main(): # funcion llamada main (se utiliza para la funcion principal de muchos programas Python)
    mostrar_contactos() # funcion que muestra lista de contactos
    
    nombre = input("\nIngrese el nombre del nuevo contacto: ") # captura la entrada y la almacena en la var nombre
    email = input("\nIngrese el email del nuevo contacto: ") #idem
    gestion.agregar_contacto(nombre, email) # llama la funcion agregar contacto del archivo gestion.py y le pasa los argumentos
    print("\ncontacto agregado exitosamente") # idem
    print("\ncontactos actualizados:") # idem
    mostrar_contactos() # muestra los contactos de la lista
    
    nombre_a_buscar = input("\ningrese el nombre a buscar: ") # var, que almacena la captura de datos
    contactos_encontrados = busqueda.buscar_contacto(nombre_a_buscar) # llama la funcion buscar contacto del archivo busqueda.py, y almacena lo encontrado en la var contactos_encontrados
    
    if contactos_encontrados: # sentencia condicional
        print("\ncontactos encontrados:") # var
        for contacto in contactos_encontrados: # bucle de iteracion sobre la lista
            print(contacto) # imprime el valor de contacto
    
    else:
        print("no se encontraron contactos.") # idem

if __name__ == "__main__": # var especial de python que representa el nombre de modulo actual, main cadena de texto que indica que el script esta siendo ejecutado directamente
    main()
    
#main de la linea 30, es la fun princ del prog, contiene el flujo principal, se ejecuta directamente y no cuando se importa como modulo
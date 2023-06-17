"""
Programa: proyecto_Final.py
Autores: Abad Ramírez Gamaliel 
         Cadena Garcilazo Angel Josue
         Arreola Garcia José Eduardo

Este programa fue diseñado para que una compañía de streming pueda manipular el
catalogo. 
Se tomaron en cuenta las siguientes necesidades para implementar al programa: 
    Agregar un producto.
    Buscar producto.
    Eliminar un producto.
    Mostrar el catálogo.
    Cargar catálogo.
    Guardar catálogo.
    Salir del programa.
    
Toda nuestro catalogo será manejada por un diccionario de diccionarios.
Dicho catalogo será asignado en la variable base_de_Datos.
"""

"""Importamos tres módulos necesarios para el correcto funcionamiento del 
   programa"""

"""El módulo Validar_datos.py contiene funciones que validan múltiples tipos de datos.
   El módulo fue diseñado prioritariamente para el programa proyecto_Final.py."""

import Validar_datos

"""Importamos el módulo json para leer y escribir archivos del tipo '.json'.
   Con este tipo de archivo guardaremos y cargaremos los catálogos.
   Los archivos .json se caracterizan para almacenar diccionarios dentro de Python."""
   
import json

def seleccion_menu():
    
    """La función menú muestra al usuario la variedad de acciones que puede 
       realizar dentro del programa.
       A cada acción le corresponde un número.
       Esta función retorna la opción del menú seleccionada."""
       
    print("Menú principal \n\n" 
          "1. Agregar un producto \n" 
          "2. Buscar producto \n"
          "3. Eliminar un producto \n"
          "4. Mostrar el catálogo \n" 
          "5. Cargar catálogo \n" 
          "6. Guardar catálogo \n"
          "7. Salir")
    
    """Utilizamos la función validar_numero_rango() del módulo Validar_datos
       para validar que la variable x esté dentro del rango asignado."""
    
    x = Validar_datos.validar_numero_rango(0, 8)
    
    # Asignamos a la variable Opcion_menú el valor de la variable x.
    
    Opcion_Menu = int(x)
    
    return Opcion_Menu
    
def tipo_de_producto_a_ingresar(base_de_Datos):
    
    """Esta función muestra al usuario un 'submenú' para ingresar un producto al catálogo.
       Dependerá de la necesidad del usuario el producto que deseé agregar.
       Esta función utiliza como argumento la variable base_de_Datos
       para ejecutar la opción número 5 del menú.
       la Función retorna la Opcion_entrada"""
    
    print("Menú agregar producto \n\n" 
          "1. Película \n" 
          "2. Series \n"
          "3. Documental \n"
          "4. Evento deportivo en vivo \n" 
          "5. Regresar \n")

    # Utilizamos la función validar_numero_rango() del módulo Validar_datos
    # para validar que la variable x esté dentro del rango asignado.
    
    x = Validar_datos.validar_numero_rango(0, 6)
    
    """Opcion_a_ingresar el nombre de la categoría del producto. 
       Dichos nombres ya están definidas en la base de datos como claves.
       Recordemos que la variable base_de_Datos es un diccionario de diccionarios.
       Utilizaremos la variable Opcion_a_ingresar como clave para entrar al diccionario."""
    
    # Por medio de condicionales if, elif y else asignamos a la variable
   
    if x == 1:
        Opcion_a_ingresar = 'Peliculas'
    elif x == 2:
        Opcion_a_ingresar = 'Series'
    elif x == 3:
        Opcion_a_ingresar = 'Documentales'
    elif x == 4:
        Opcion_a_ingresar = 'Evento_deportivo_en_vivo'
    else:
        ejecucion_programa(base_de_Datos)
        
    return Opcion_a_ingresar

def ingresa_datos(Opcion_a_ingresar, base_de_Datos):
    
    """Esta función utiliza como argumentos a las variables Opcion_a_ingresar y 
       base_de_Datos.
       El titulo ingresado será la clave de un diccionario único correspondiente al producto.
       Todos los productos tienen datos exclusivos conforme a su categoría.
       La función asignará al diccionario del producto otro diccionario con los
       datos exclusivos de cada producto.
       Cada característica será asignada a la clave del diccionario antes mencionados
       correspondiente al tipo de característica.
       La función retorna la variable base_de_Datos."""
       
    """Utilizando condicionales if, elif y else se determinará el tipo de producto
       en el que se almacenara el diccionario único para cada producto.
       Para todos los títulos utilizamos la función .strip() para así eliminar 
       espacios al principio y final, con el propósito de optimizar su búsqueda. 
    
       Cuando se requiere ingresar un año el programa utiliza la función .validar_año() del 
       modulo Validar_datos para validar el año.
    
    Cuando se requiere ingresar un precio de venta o renta el programa utiliza 
    la función .validar_año() del módulo Validar_datos para validar el precio."""
    
    # Ingresa películas.
    
    if Opcion_a_ingresar == 'Peliculas':
        titulo = input('Nombre de la pelicula: ')
        titulo = titulo.strip()
        año = Validar_datos.validar_año()
        director = input('Director@: ')
        precio = Validar_datos.validar_venta_renta()
        y = {'año':año, 'director':director, 'precio':precio}
        base_de_Datos[Opcion_a_ingresar][titulo] = y
       
   # Ingresar series.
   
    elif Opcion_a_ingresar == 'Series':
        titulo = input('Nombre de la serie: ')
        titulo = titulo.strip()
        base_de_Datos[Opcion_a_ingresar][titulo] = {}
        año = Validar_datos.validar_año()
        director = input('Director@: ')
        temporadas = input('Temporadas: ')
        precio = Validar_datos.validar_venta_renta()
        y = {'año':año, 'director':director, 'temporadas':temporadas, 'precio':precio}
        base_de_Datos[Opcion_a_ingresar][titulo] = y
        
    # Ingresar documentales.
    
    elif Opcion_a_ingresar == 'Documentales':
        titulo = input('Nombre del documental: ')
        titulo = titulo.strip()
        base_de_Datos[Opcion_a_ingresar][titulo] = {}
        director = input('Director@: ')
        tema = input('Tema: ')
        año = Validar_datos.validar_año()
        precio = Validar_datos.validar_venta_renta()
        y = {'director':director, 'tema':tema, 'año':año, 'precio':precio}
        base_de_Datos[Opcion_a_ingresar][titulo] = y
        
    # Ingresa eventos deportivos en vivo.
    
    else:
        titulo = input('Nombre del evento en vivo: ')
        titulo = titulo.strip()
        base_de_Datos[Opcion_a_ingresar][titulo] = {}
        deporte = input('Deporte: ')
        fecha = input('Fecha: ')
        hora = input('Hora: ')
        lugar = input('Lugar: ')
        precio = input('Venta: ')
        y = {'deporte':deporte, 'fecha':fecha, 'hora':hora, 'lugar':lugar, 'precio':precio}
        base_de_Datos[Opcion_a_ingresar][titulo] = y
    
    return base_de_Datos

def buscar_producto(base_de_Datos):
    
    """Esta función utiliza como argumento la variable base_de_Datos.
       El usuario ingresa cualquier cadena de tipo alfanumérico 
       y la función retorna todos los productos con dichos caracteres dentro de su título.
       En caso de existir coincidencia también mostrará el tipo de producto que sea."""
       
    """Primero asignamos a la variable No_encontrado el valor de True.
       Dicha variable la utilizaremos dentro de una condicional if y 
       tener un operador lógico que indique si la
       búsqueda está dentro del catálogo o no."""
    
    No_encontrado = True
   
    producto_a_buscar = input('¿Qué desea buscar? ') 
   
    """A la variable búsqueda le asignaremos una lista vacía en la que añadiremos todas las 
    opciones que coincidan con la búsqueda"""
   
    busqueda = []
    
    """Utilizamos una estructura de control for, en la que en cada bucle,
       a 'i' se le asignaran todas las claves de los productos 
       dentro de la varable base_de_Datos."""
    
    # Primer estructura de control for.
    
    for i in ('Peliculas', 'Series', 'Documentales', 'Evento_deportivo_en_vivo'):
            
        """Asignamos a la variable claves una lista con todas las claves dentro 
           del tipo de claves.
           Esto lo hacemos para comparar de manera más eficiente la coincidencia entre
           el producto a buscar y las claves dentro del tipo de producto."""
            
        claves = list(base_de_Datos[i].keys())
        
        """Utilizamos nuevamente una estructura de control for, en la que en cada bucle 
           a 'j' se le asignarán el rango de 0 a el número de claves dentro del tipo 
           de producto.
           Lo mencionado anteriormente se realiza para evaluar cada uno de 
           los productos dentro del tipo de producto."""
         
        # Segunda estructura de control for.
         
        for j in range(0, len(claves)):
            
            """Con la condicional if comparamos si el producto a buscar está dentro de 
               las claves del tipo de producto. 
               Utilizamos la función .lower() para que todos los caracteres 
               sean letras minúsculas. Dicha función la utilizamos para
               la variable producto_a_buscar y también para el elemento de la lista claves[j]."""
            
            if producto_a_buscar.lower() in claves[j].lower():
                
                """Si la condicional if es verdadera utilizaremos la variable .append 
                   para añadir al final de la lista búsqueda el nombre del producto concatenado 
                   con el tipo de producto y a la variable No_encontrado se le asignará 
                   el valor de Falso."""
                  
                busqueda.append(claves[j] + str(' Tipo: ') + str(i)) 
                
                No_encontrado = False
    
    """Utilizando una condicional if evaluaremos el valor de la variable No_enocntrado.
       Si la variable es de valor Falso se utilizará una estructura de control for 
       en la cual a cada 'i' de le asignara el rango de 0 a la longitud de elementos de la lista 
       de búsqueda.
       Entre cada bucle se mostrará el elemento busqueda[i] de la lista búsqueda.
       En caso de que la variable No_encontrado tenga valor verdadero, se mostrara el mensaje 
       'Producto no encontrado'"""
    
    if No_encontrado == False:
       for i in range(0, len(busqueda)):
           print('\n'+ busqueda[i] + '\t')
    else:
        print('\nProducto no encontrado.')

def Eliminar_un_producto(base_de_Datos):
   
    """Esta función utiliza como argumentos la variable base_de_Datos. 
       Esta función elimina un producto dentro del catálogo (una clave del diccionario)"""
       
    """Primero asignamos a la variable No_encontrado el valor de True.
       Dicha variable la utilizaremos para dentro 
       de una condicional if y tener un operador lógico que indique si el 
       producto a eliminar está dentro del catálogo o no."""
       
    No_encontrado = True 
    
    print('\nEscribe el nombre preciso del producto que deseas eliminar')
    
    # Ingresar el nombre del producto a eliminar
    
    Producto_a_eliminar = input('Nombre del producto que quieres eliminar: ')
    
    """Utilizamos la función .strip para eliminar los espacios antes y después de la cadena 
       contenida en la variable Producto a eliminar. Hacemos lo anterior para optimizar la 
       búsqueda del producto a eliminar."""
    
    Producto_a_eliminar = Producto_a_eliminar.strip()
   
    """Utilizamos una estructura de cotrol for, el la que en cada bucle,
      a 'i' se le asignaran todas las claves de los productos 
      dentro de la varable base_de_Datos."""
    
    # Primer ciclo for.
    
    for i in ('Peliculas', 'Series','Documentales', 'Evento_deportivo_en_vivo'):
        
        """Asignamos a la variable lista_de_productos_en_categoria una lista con todas los productos dentro 
           del tipo de Productos.
           Esto lo hacemos para comparar de manera más eficiente la coincidencia entre
           el producto para eliminar y las claves dentro del tipo de producto."""
        
        lista_de_productos_en_categoria = list(base_de_Datos[i].keys())
        
        """Utilizamos nuevamente una estructura de control for, en la que en cada bucle 
           a 'l' se le asignará el rango de 0 a el número de elementos de la lista
           lista_de_productos_en_categoria."""
        
        # Segundo ciclo for.
        
        for l in range(0, len(lista_de_productos_en_categoria)):
            
            """Es necesario que el usuario Introduzca de manera correcta el nombre completo 
               del producto pues la condición if compara que el producto a eliminar 
               sea totalmente igual a el elemento de la lista lista_de_productos_en_categoria"""
            
            if Producto_a_eliminar == lista_de_productos_en_categoria[l]:
                
                """En caso de ser cierta la condición if anterior, asignaremos a la variable 
                   No_encontrado el valor de falso"""
                
                No_encontrado = False
                
                """Mostraremos al usuario el elemento que desea eliminar y utilizando la función 
                   .validar_s_n() del módulo Validar_datos, se determinará si la condición 
                   será verdadera o falsa.
                   En caso de ser verdadera con la función ,pop() se eliminará la clave.
                   En caso de ser falsa se mostrará el mensaje 'Producto no eliminado'"""
                                                        
                 
                Producto_valido_para_eliminar = lista_de_productos_en_categoria[l]
                print(lista_de_productos_en_categoria[l] + str(base_de_Datos[i][lista_de_productos_en_categoria[l]]))
                if Validar_datos.validar_s_n():
                   base_de_Datos[i].pop(Producto_valido_para_eliminar)
                   print('\nEl producto fue eliminado con exito.\n')
                else: 
                    print('\nProducto no eliminado.\n')
    
    
    """Si la variable No_encotrado tiene asignado el valor True 
       se mostrará el siguiente mensaje."""
    
    if No_encontrado == True:
        print('\nEl producto no existe o ingresa de manera correcta el nombre. \n')
       
def Menu_mostrar_catalogo():
    
    """La función muestra al usuario la variedad de acciones que puede 
       realizar para mostrar el catálogo.
       A cada acción le corresponde el nombre de la categoría o instrucción que desea.
       Esta función retorna la opción para mostrar el catálogo."""
    
    print('Menú mostrar catálogo \n'
          '1. Películas \n'
          '2. Series \n' 
          '3. Documentales \n' 
          '4. Eventos deportivos \n' 
          '5. Todo \n'
          '6. Regresar')
    
    """Utilizamos la función validar_numero_rango() del módulo Validar_datos
       para validar que la variable x esté dentro del rango asignado."""
    
    
    x = Validar_datos.validar_numero_rango(0, 7)
   
    # Condicional if.
    
    x = int(x)
    
    if x == 1:
        opcion_mostrar_catalogo = 'Peliculas'
    elif x == 2:
        opcion_mostrar_catalogo = 'Series'
    elif x == 3:
        opcion_mostrar_catalogo = 'Documentales'
    elif x == 4:
        opcion_mostrar_catalogo = 'Evento_deportivo_en_vivo'
    elif x == 5:
        opcion_mostrar_catalogo = 'Todo'
    else:
        opcion_mostrar_catalogo = 'Regresar'
   
    return opcion_mostrar_catalogo
       
def Mostrar_catalogo(base_de_Datos, opcion_mostrar_catalogo):
    
    """Esta función utiliza como argumentos las variables base_de_Datos y opcion_mostrar_catalogo.
       Esta función muestra el catálogo en función a la opción requerida por el usuario.
       Para todas las opciones se asigna a una variable lista_(tipo de producto)
       una lista con todas las claves (nombres) de los productos.
       Después, por medio de una estructura de control for se le asigna a 'i' el rango de 0 a
       la longitud de la lista(tipo de producto) para así recorrer por cada una de las 
       claves contenidas en el diccionario.
       Cada tipo de producto tiene elementos característicos los cuales se asignarán 
       a las variables correspondientes por medio de sus claves.
       Al final, se mostrará la concatenación del nombre del producto con todos sus elementos 
       característicos."""
    
    """Para mostrar todo el catálogo, realizamos todas los ciclos anteriores contenidos en
       una condicional"""
       
    # Para mostrar las peliculas.
    
    if opcion_mostrar_catalogo == 'Peliculas':
        lista_peliculas = list((base_de_Datos['Peliculas'].keys()))
        for i in range(0, len(lista_peliculas)):
            nombre_Pelicula = lista_peliculas[i]
            año = str(base_de_Datos['Peliculas'][nombre_Pelicula]['año'])
            director = str(base_de_Datos['Peliculas'][nombre_Pelicula]['director'])
            precio = str(base_de_Datos['Peliculas'][nombre_Pelicula]['precio'])
            print('\n' + nombre_Pelicula + '  Año: ' + año + ',   Director@: ' + director + ',   Precio: ' + precio + '\n')
    
    # Para mostrar las series.
    
    elif opcion_mostrar_catalogo == 'Series':
        lista_series = list((base_de_Datos['Series'].keys()))
        for i in range(0, len(lista_series)):
            nombre_serie = str(lista_series[i])
            año = str(base_de_Datos['Series'][nombre_serie]['año'])
            director = str(base_de_Datos['Series'][nombre_serie]['director'])
            temporadas = str(base_de_Datos['Series'][nombre_serie]['temporadas'])
            precio = str(base_de_Datos['Series'][nombre_serie]['precio'])
            print('\n' + nombre_serie + '    Año: ' + año + '  Director: ' + director + '  Temporadas: ' + temporadas + ',   Precio: ' + precio + '\n')
            
    # Para mostrar los documentales.
    
    elif opcion_mostrar_catalogo == 'Documentales':
        lista_documentales = list((base_de_Datos['Documentales'].keys()))
        for i in range(0, len(lista_documentales)):
            nombre_documental = lista_documentales[i]
            director = str(base_de_Datos['Documentales'][nombre_documental]['director'])
            tema = str(base_de_Datos['Documentales'][nombre_documental]['tema'])
            año = str(base_de_Datos['Documentales'][nombre_documental]['año'])
            precio = str(base_de_Datos['Documentales'][nombre_documental]['precio'])
            print('\n' + nombre_documental + '    Director@: ' + director + '  Tema: ' + tema + '  Año:  ' + año + ',   Precio: ' + precio + '\n')
    
    # Para mostrar los eventos en vivo.
    
    elif opcion_mostrar_catalogo == 'Evento_deportivo_en_vivo':
        lista_evento_deportivo = list((base_de_Datos['Evento_deportivo_en_vivo'].keys()))
        for i in range(0, len(lista_evento_deportivo)):
            nombre_evento_deportivo = lista_evento_deportivo[i]
            deporte = str(base_de_Datos['Evento_deportivo_en_vivo'][nombre_evento_deportivo]['deporte'])
            fecha = str(base_de_Datos['Evento_deportivo_en_vivo'][nombre_evento_deportivo]['fecha'])
            hora = str(base_de_Datos['Evento_deportivo_en_vivo'][nombre_evento_deportivo]['hora'])
            lugar = str(base_de_Datos['Evento_deportivo_en_vivo'][nombre_evento_deportivo]['lugar'])
            precio = str(base_de_Datos['Evento_deportivo_en_vivo'][nombre_evento_deportivo]['precio'])
            print('\n' + nombre_evento_deportivo + '   Deporte: ' + deporte + '   Fecha: ' + fecha + '   Hora: ' + hora + '   Lugar: ' + lugar + ',   Precio: ' + precio + '\n')
    
    # Para mostrar todo el catálogo.
    
    elif opcion_mostrar_catalogo == 'Todo':
        lista_peliculas = list((base_de_Datos['Peliculas'].keys()))
        for i in range(0, len(lista_peliculas)):
            nombre_Pelicula = lista_peliculas[i]
            año = str(base_de_Datos['Peliculas'][nombre_Pelicula]['año'])
            director = str(base_de_Datos['Peliculas'][nombre_Pelicula]['director'])
            precio = str(base_de_Datos['Peliculas'][nombre_Pelicula]['precio'])
            print('\n' + nombre_Pelicula + '  Año: ' + año + ',   Director@: ' + director + ',   Precio: ' + precio + '\n')
        
        lista_series = list((base_de_Datos['Series'].keys()))
        for i in range(0, len(lista_series)):
            nombre_serie = lista_series[i]
            año = str(base_de_Datos['Series'][nombre_serie]['año'])
            director = str(base_de_Datos['Series'][nombre_serie]['director'])
            temporadas = str(base_de_Datos['Series'][nombre_serie]['temporadas'])
            precio = str(base_de_Datos['Peliculas'][nombre_serie]['precio'])
            print('\n' + nombre_serie + '    Año: ' + año + '  Director: ' + director + '  Temporadas: ' + temporadas + ',   Precio: ' + precio + '\n')
        
        lista_documentales = list((base_de_Datos['Documentales'].keys()))
        for i in range(0, len(lista_documentales)):
            nombre_documental = lista_documentales[i]
            director = str(base_de_Datos['Documentales'][nombre_documental]['director'])
            tema = str(base_de_Datos['Documentales'][nombre_documental]['tema'])
            año = str(base_de_Datos['Documentales'][nombre_documental]['año'])
            precio = str(base_de_Datos['Peliculas'][nombre_documental]['precio'])
            print('\n' + nombre_documental + '    Director@: ' + director + '  Tema: ' + tema + '  Año:  ' + año + ',   Precio: ' + precio + '\n')
        
        lista_evento_deportivo = list((base_de_Datos['Evento_deportivo_en_vivo'].keys()))
        for i in range(0, len(lista_evento_deportivo)):
            nombre_evento_deportivo = lista_evento_deportivo[i]
            deporte = str(base_de_Datos['Evento_deportivo_en_vivo'][nombre_evento_deportivo]['deporte'])
            fecha = str(base_de_Datos['Evento_deportivo_en_vivo'][nombre_evento_deportivo]['fecha'])
            hora = str(base_de_Datos['Evento_deportivo_en_vivo'][nombre_evento_deportivo]['hora'])
            lugar = str(base_de_Datos['Evento_deportivo_en_vivo'][nombre_evento_deportivo]['lugar'])
            precio = str(base_de_Datos['Evento_deportivo_en_vivo':][nombre_evento_deportivo]['precio'])
            print('\n' + nombre_Pelicula + '   Deporte: ' + deporte + '   Fecha: ' + fecha + '   Hora: ' + hora + '   Lugar: ' + lugar + ',   Precio: ' + precio + '\n')
        
    else:
        ejecucion_programa(base_de_Datos)

def cargar_base_de_Datos():
    
    """Esta función carga el catálogo.
       Para cargar el catálogo utilizamos la función .load() del módulo json.
       Con el formato .json podremos cargar el diccionario de diccionarios.
       Retorna la variable base_de_Datos."""
       
    g = open(input('Ingresa el nombre del archivo .json:  '))
    base_de_Datos = json.load(g)

    return base_de_Datos
    
def Guardar_catalogo(base_de_Datos):
    
    """Esta función guarda el catálogo.
       Para guardar el catálogo utilizamos la función .load() del módulo json.
       Con el formato .json podremos guardar el diccionario de diccionarios."""

    f = open(input('Ingresar el nombre del archivo .json:  '), 'w') 
    base_de_Datos = json.dump(base_de_Datos, f)
    
def ejecucion_programa (base_de_Datos):
    
    """Esta función realiza el funcionamiento de todo el programa a excepción de 
       la variable base_de_Datos, pues esta será proporcionada por la función main().
       Así logramos que la variable de datos no se 'reinicie' y el diccionario de diccionarios 
       que está contenido en la variable base_de_Datos pueda posteriormente seguir siendo manipulada."""
    
    """A la variable Ejecutar se le asigna el valor de True y utilizando 
       la condicional while el programa se ejecutará hasta que dicha variable
       cambie de valor a False"""
       
    Ejecutar = True
    
    while Ejecutar == True:
         
        
         Opcion_Menu = seleccion_menu()
        
         """Si el valor de la variable Opcion_menu es igual a 1 
            se agregará un producto al catalogo utilizando las funciones tipo_de_producto()
            e ingresa_datos()"""        
        
         if Opcion_Menu == 1:
             opcion_a_ingresar = tipo_de_producto_a_ingresar(base_de_Datos)
             ingresa_datos(opcion_a_ingresar, base_de_Datos)
            
             """Si el valor de la variable Opcion_menu es igual a 2
                se buscará un producto en el catálogo utilizando la función buscar_producto()."""
             
         elif Opcion_Menu == 2:
             buscar_producto(base_de_Datos)
         
             """Si el valor de la variable Opcion_menu es igual a 3
                se eliminará un producto al catálogo utilizando
                la función Eliminar_un_producto."""
                
         elif Opcion_Menu == 3:
             Eliminar_un_producto(base_de_Datos)
             
             """Si el valor de la variable Opcion_menu es igual a 4 
                se mostrará el catálogo utilizando las funciones Mostrar_catalogo
                y Menu_mostrar_catalogo()."""
                
         elif Opcion_Menu == 4:
             
             opcion_mostrar_catalogo = Menu_mostrar_catalogo()
             Mostrar_catalogo(base_de_Datos, opcion_mostrar_catalogo)
             
             """Si el valor de la variable Opcion_menu es igual a 5
                se cargará el  catálogo. utilizando la función cargar base de datos().
                a la variable base_de_Datos se le asignara el valor de la función antes mencionada."""
         
         elif Opcion_Menu == 5:
             base_de_Datos = cargar_base_de_Datos()
             
             """Si el valor de la variable Opcion_menu es igual a 6
             se guardará el catálogo utilizando la función Guardar_catalogo()."""
             
         elif Opcion_Menu == 6:
             Guardar_catalogo(base_de_Datos)
             
             """Si el valor de la variable Opcion_menu es igual a 7
                a la variable Ejecutar se le asigna el valor False para así 
                interrumpir la ejecución del programa.
                Se muestra el mensaje 'Exit'."""
         
         elif Opcion_Menu == 7:
             print('\nExit')
             Ejecutar = False
             
def main ():
   
   """La función main ejecuta el programa."""
   
   """A la variable base_de_Datos le será asignado un diccionario de diccionarios y conforme 
      el programa manipule el diccionario éste irá cambiando."""
    
   base_de_Datos = {"Peliculas": {}, "Series": {}, "Documentales": {}, "Evento_deportivo_en_vivo": {}}
   
   ejecucion_programa(base_de_Datos)
    

main()

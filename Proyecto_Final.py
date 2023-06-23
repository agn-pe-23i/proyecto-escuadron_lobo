"""
Programa: proyecto_Final.py
Autores: Abad Ramírez Gamaliel 
         Cadena Garcilazo Angel Josue
         Arreola Garcia José Eduardo

Este programa fue diseñado para que una compañía de streaming pueda manipular el
catalogo. 
Se tomaron en cuenta las siguientes necesidades para implementar al programa: 
    Agregar un producto.
    Buscar producto.
    Eliminar un producto.
    Mostrar el catálogo.
    Cargar catálogo.
    Guardar catálogo.
    Salir del programa.
    
Todo nuestro catálogo será manejada por un diccionario de diccionarios.
Dicho catalogo será asignado a la variable base_de_Datos.
"""

"""Importamos cuatro módulos necesarios para el correcto funcionamiento del 
   programa"""

"""Importamos el módulo sys. Utilizaremos el módulo sys 
   para cerrar el programa utilizando la función  .exit()"""

import sys

"""Importamos el módulo ingresar_datos_multimedia.py 
   Este módulo cuenta con funciones para agregar y validar 
   elementos relacionados con archivos multimedia.
   Considerando que en este problema trabajamos con películas y series y otros 
   productos del tipo multimedia este módulo será de gran utilidad"""

import ingresar_datos_multimedia

"""Importamos el módulo json para leer y escribir archivos del tipo '.json'.
   Con este tipo de archivo guardaremos y cargaremos los catálogos.
   Los archivos .json se caracterizan para almacenar diccionarios dentro de Python."""
   
import json

"""Para el inicio de nuestro programa requerimos un diccionario de diccionarios en blanco.
   En la variable base_de_Datos almacenaremos dicho diccionario de diciionarios ""en blanco"
   (Sin ningun producto)."""
   
base_de_Datos = {"Peliculas": {}, "Series": {}, "Documentales": {}, "Evento_deportivo_en_vivo": {}}

    
def agrega_un_producto(base_de_Datos):
    
    """Esta función muestra al usuario un 'submenú' para ingresar un producto al catálogo.
       Dependerá de la necesidad del usuario el producto que deseé agregar.
       Esta función utiliza como argumento la variable base_de_Datos para almacenar en ella
       los productos requeridos por el usuario. 
       La Función retorna la variable Opcion_entrada"""
    
    print("Menú agregar producto: \n\n" 
          "1. Película \n" 
          "2. Series \n"
          "3. Documental \n"
          "4. Evento deportivo en vivo \n" 
          "5. Regresar \n")

    # Utilizamos una estructura de control while
    # para validar que la variable x esté dentro del rango asignado.
    #  El ciclo se ejecuta mientras Validar sea igual a False, lo que significa 
    # que se seguirá pidiendo al usuario que ingrese el número de su preferencia
    # hasta que se cumpla la condición especificada.
    
    Validar = False
    while Validar == False:
        x = input('Ingresa el número de tu preferencia: ')
        if x.isdigit() and int(x) > 0 and int(x) < 6:
            Validar = True
        else:
            print('Ingresa un número valido.')
   
    x = int(x)
    
    """Deacuerdo a el número asignada a x, por medio de condicionales if 
       se asignará que función realizar.
       
       Si x es igual a 1 se realiza la función ingresa_pelicula().
         
       Si x es igual a 2 se realiza la función ingresa_serie():
  
       Si x es igual a 3 se realiza la función ingresa_documental(): 
  
       Si x es igual a 4 se realiza la función ingresa_evento_dportivo():
        
       Si x es igual a 5 se  realiza la función menu():
    
       """
    
    # Por medio de condicionales if, elif y else asignamos a la variable.
    

    if x == 1:
        ingresa_pelicula(base_de_Datos)
    elif x == 2:
        ingresa_serie(base_de_Datos)
    elif x == 3:
        ingresa_documental(base_de_Datos)
    elif x == 4:
        ingresa_evento_dportivo(base_de_Datos)
    else:
        main(base_de_Datos)
        
def ingresa_pelicula(base_de_Datos):
    
    """Esta función ingresa un producto tipo pelicula con sus caracteristicas 
       correspondientes utilizando el modulo ingresar_datos_multimeedia.
       Dichas caracteristicas se asigan a un diccionario cuya variable es y."""
    
    titulo = input('Nombre de la pelicula: ')
    titulo = titulo.strip()
    año = ingresar_datos_multimedia.ingresa_año()
    director = ingresar_datos_multimedia.ingresa_nombre('Director@: ')
    precio = ingresar_datos_multimedia.ingresa_venta_renta()
    y = {'año':año, 'director':director, 'precio':precio}
    base_de_Datos['Peliculas'][titulo] = y
   
def ingresa_serie(base_de_Datos):
    
    """Esta función ingresa un producto tipo serie con sus caracteristicas 
       correspondientes utilizando el modulo ingresar_datos_multimeedia.
       Dichas caracteristicas se asigan a un diccionario cuya variable es y."""
       
    titulo = input('Nombre de la serie: ')
    titulo = titulo.strip()
    base_de_Datos['Series'][titulo] = {}
    año = ingresar_datos_multimedia.ingresa_año()
    director = ingresar_datos_multimedia.ingresa_nombre('Director@: ')
    temporadas = ingresar_datos_multimedia.ingresar_numero('Temporadas: ')
    precio = ingresar_datos_multimedia.ingresa_venta_renta()
    y = {'año':año, 'director':director, 'temporadas':temporadas, 'precio':precio}
    base_de_Datos['Series'][titulo] = y
        
def ingresa_documental(base_de_Datos):
    
    """Esta función ingresa un producto tipo documental con sus caracteristicas 
       correspondientes utilizando el modulo ingresar_datos_multimeedia.
       Dichas caracteristicas se asigan a un diccionario cuya variable es y."""
       
    titulo = input('Nombre del documental: ')
    titulo = titulo.strip()
    base_de_Datos['Documentales'][titulo] = {}
    director = ingresar_datos_multimedia.ingresa_director()
    tema = ingresar_datos_multimedia.ingresa_nombre('Tema: ')
    año = ingresar_datos_multimedia.ingresa_año()
    precio = ingresar_datos_multimedia.ingresa_venta_renta()
    y = {'director':director, 'tema':tema, 'año':año, 'precio':precio}
    base_de_Datos['Documentales'][titulo] = y
   
def ingresa_evento_dportivo(base_de_Datos):
    
    """Esta función ingresa un producto tipo evento deportivo con sus caracteristicas 
       correspondientes utilizando el modulo ingresar_datos_multimeedia.
       Dichas caracteristicas se asigan a un diccionario cuya variable es y."""
       
    titulo = input('Nombre del evento en vivo: ')
    titulo = titulo.strip()
    base_de_Datos['Evento_deportivo_en_vivo'][titulo] = {}
    deporte = ingresar_datos_multimedia.ingresa_nombre('Deporte: ')
    fecha = input('Fecha: ')
    hora = input('Hora: ')
    lugar = input('Lugar: ')
    precio = ingresar_datos_multimedia.ingresa_precio()
    y = {'deporte':deporte, 'fecha':fecha, 'hora':hora, 'lugar':lugar, 'precio':precio}
    base_de_Datos['Evento_deportivo_en_vivo'][titulo] = y

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

def seguro_de_eliminacion():
 
    """ Esta función valida la opcion entre 'S' = Si, 'N' = No.
    Esta desañado para validar la eliminación de un preducto dentro del catalogo.
    Retorna un valor booleano."""
    Validar = True 
    
    # Utilizando una condicional while, validamos el dato de entrada. 
    # La entrada debe ser una "N" o una "S". Todo elemento que no sea una "N" o "S" 
    # será no valido
   
    while Validar == True:
        Seguro_de_Eliminacion = input('¿Estás seguro de eliminar el elemento?  [S/N]   ')
        if len(Seguro_de_Eliminacion) == 1 and  Seguro_de_Eliminacion.isalpha() and (Seguro_de_Eliminacion.lower() == 's' or Seguro_de_Eliminacion.lower() == 'n'):
            Validar = False 
        else:
            print('Ingresa "S" para si o "N" para no') 
    
    if Seguro_de_Eliminacion.lower() == 's':
        Eliminacion_Validada = True
    else:
        Eliminacion_Validada = False
    
    return Eliminacion_Validada

def eliminar_un_producto(base_de_Datos):
   
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
                if seguro_de_eliminacion():
                   base_de_Datos[i].pop(Producto_valido_para_eliminar)
                   print('\nEl producto fue eliminado con exito.\n')
                else: 
                    print('\nProducto no eliminado.\n')
    
    
    """Si la variable No_encotrado tiene asignado el valor True 
       se mostrará el siguiente mensaje."""
    
    if No_encontrado == True:
        print('\nEl producto no existe o ingresa de manera correcta el nombre. \n')
       
def mostrar_catalogo(base_de_Datos):
    
    """La función muestra al usuario la variedad de acciones que puede 
       realizar para mostrar el catálogo.
       Despues asigna a la variale x el numero deacuerdo a la opcion seleccionada 
       por el usuario.
       Por ultimo, por meido de condicionales if se determina que función realizará 
       el programa en relación con la variable x."""
    
    print('Menú mostrar catálogo \n'
          '1. Películas \n'
          '2. Series \n' 
          '3. Documentales \n' 
          '4. Eventos deportivos \n' 
          '5. Todo \n'
          '6. Regresar')
    
    """Utilizamos la función validar_numero_rango() del módulo Validar_datos
       para validar que la variable x esté dentro del rango asignado."""
    
    
    Validar = False
    while Validar == False:
        x = input('Ingresa el número de tu preferencia: ')
        if x.isdigit() and int(x) > 0 and int(x) < 7:
            Validar = True
        else:
            print('Ingresa un número valido.')
   
    x = int(x)
   
    # Condicional if.
    
    if x == 1:
        mostrar_peliculas(base_de_Datos)
    elif x == 2:
        mostrar_series(base_de_Datos)
    elif x == 3:
        mostrar_documentales(base_de_Datos)
    elif x == 4:
        mostrar_eventos_deportivos(base_de_Datos)
    elif x == 5:
        mostrar_todo(base_de_Datos)
    else:
        main(base_de_Datos)
       
def mostrar_peliculas(base_de_Datos):
       
    # Para mostrar las peliculas.
    
    """Esta función recorre dentro de la variable base_de_Datos
       todas las  películas y, por medio de cada bucle de la estructura
       de control while, almacena la información de cada película en la lista 
       lista_peliculas.
       En cada bucle almacea el nombre, año, director y precio, todo concatenado-"""
    
    lista_peliculas = list((base_de_Datos['Peliculas'].keys()))
    for i in range(0, len(lista_peliculas)):
        nombre_Pelicula = lista_peliculas[i]
        año = str(base_de_Datos['Peliculas'][nombre_Pelicula]['año'])
        director = str(base_de_Datos['Peliculas'][nombre_Pelicula]['director'])
        precio = str(base_de_Datos['Peliculas'][nombre_Pelicula]['precio'])
        print('\n' + nombre_Pelicula + '  Año: ' + año + ',   Director@: ' + director + ',   Precio: ' + precio + '\n')
    
def mostrar_series(base_de_Datos):
    
    # Para mostrar las series.
    
    """Esta función recorre dentro de la variable base_de_Datos
       todas las  series y, por medio de cada bucle de la estructura
       de control while, almacena la información de cada serie en la lista 
       lista_series.
       En cada bucle almacea el nombre, año, director, temporadas y precio, todo concatenado-"""
    
    lista_series = list((base_de_Datos['Series'].keys()))
    for i in range(0, len(lista_series)):
        nombre_serie = str(lista_series[i])
        año = str(base_de_Datos['Series'][nombre_serie]['año'])
        director = str(base_de_Datos['Series'][nombre_serie]['director'])
        temporadas = str(base_de_Datos['Series'][nombre_serie]['temporadas'])
        precio = str(base_de_Datos['Series'][nombre_serie]['precio'])
        print('\n' + nombre_serie + '    Año: ' + año + '  Director: ' + director + '  Temporadas: ' + temporadas + ',   Precio: ' + precio + '\n')
          
def mostrar_documentales(base_de_Datos):
    
    # Para mostrar los documentales.
    
    """Esta función recorre dentro de la variable base_de_Datos
       todos los documentales y, por medio de cada bucle de la estructura
       de control while, almacena la información de cada documental en la lista 
       lista_documentales.
       En cada bucle almacea el nombre, director, tema, año y precio, todo concatenado."""
        
    lista_documentales = list((base_de_Datos['Documentales'].keys()))
    for i in range(0, len(lista_documentales)):
        nombre_documental = lista_documentales[i]
        director = str(base_de_Datos['Documentales'][nombre_documental]['director'])
        tema = str(base_de_Datos['Documentales'][nombre_documental]['tema'])
        año = str(base_de_Datos['Documentales'][nombre_documental]['año'])
        precio = str(base_de_Datos['Documentales'][nombre_documental]['precio'])
        print('\n' + nombre_documental + '    Director@: ' + director + '  Tema: ' + tema + '  Año:  ' + año + ',   Precio: ' + precio + '\n')
    
def mostrar_eventos_deportivos(base_de_Datos):
    
    """Esta función recorre dentro de la variable base_de_Datos
       todas los eventos deportivos y, por medio de cada bucle de la estructura
       de control while, almacena la información de cada evento deportivo en la lista 
       lista_evento_deportivo.
       En cada bucle almacea el nombre, deporte, fecha, hora, lugar y precio, todo concatenado."""
    
    # Para mostrar eventos deportivos.
    
    lista_evento_deportivo = list((base_de_Datos['Evento_deportivo_en_vivo'].keys()))
    for i in range(0, len(lista_evento_deportivo)):
        nombre_evento_deportivo = lista_evento_deportivo[i]
        deporte = str(base_de_Datos['Evento_deportivo_en_vivo'][nombre_evento_deportivo]['deporte'])
        fecha = str(base_de_Datos['Evento_deportivo_en_vivo'][nombre_evento_deportivo]['fecha'])
        hora = str(base_de_Datos['Evento_deportivo_en_vivo'][nombre_evento_deportivo]['hora'])
        lugar = str(base_de_Datos['Evento_deportivo_en_vivo'][nombre_evento_deportivo]['lugar'])
        precio = str(base_de_Datos['Evento_deportivo_en_vivo'][nombre_evento_deportivo]['precio'])
        print('\n' + nombre_evento_deportivo + '   Deporte: ' + deporte + '   Fecha: ' + fecha + '   Hora: ' + hora + '   Lugar: ' + lugar + ',   Precio: ' + precio + '$\n')
    
def mostrar_todo(base_de_Datos):
    
    """En esta función, se muestra todo el catalogo, utilizando las funciones anteriores 
    funcionales para mostrar el catalogo deacuerdo a el tipo de producto."""
    # Para mostrar todo.
    
    mostrar_peliculas(base_de_Datos)
    mostrar_series(base_de_Datos)
    mostrar_documentales(base_de_Datos)
    mostrar_eventos_deportivos(base_de_Datos)

def cargar_catalogo():
    
    """Esta función carga el catálogo.
       Para cargar el catálogo utilizamos la función .load() del módulo json.
       Con el formato .json podremos cargar el diccionario de diccionarios.
       Retorna la variable base_de_Datos."""
       
    g = open(input('Ingresa el nombre del archivo .json:  '))
    base_de_Datos = json.load(g)

    return base_de_Datos
    
def guardar_catalogo(base_de_Datos):
    
    """Esta función guarda el catálogo.
       Para guardar el catálogo utilizamos la función .load() del módulo json.
       Con el formato .json podremos guardar el diccionario de diccionarios."""

    f = open(input('Ingresar el nombre del archivo .json:  '), 'w') 
    base_de_Datos = json.dump(base_de_Datos, f)
    
def main(base_de_Datos):
    
    """Esta función realiza el funcionamiento de todo el programa."""
       
    """A la variable Ejecutar se le asigna el valor de True y utilizando 
       la condicional while el programa se ejecutará indefinidamente hasta que 
       el usuario ingrese la opción numero 7 (Salir). """
       
    """Se muestra todas las opciones del menu. Deacuerdo con la opción seleccionada
       Se ejecutará la funcion correspondiente a la opcion seleccionada"""
       
    Ejecutar = True
    
    while Ejecutar == True:
        
        print("Menú principal \n\n" 
            "1. Agregar un producto \n" 
            "2. Buscar producto \n"
            "3. Eliminar un producto \n"
            "4. Mostrar el catálogo \n" 
            "5. Cargar catálogo \n" 
            "6. Guardar catálogo \n"
            "7. Salir")
        
        
        # Utilizamos una estructura de control while
        # para validar que la variable x esté dentro del rango asignado.
        #  El ciclo se ejecuta mientras Validar sea igual a False, lo que significa 
        # que se seguirá pidiendo al usuario que ingrese el número de su preferencia
        # hasta que se cumpla la condición especificada.
        
        Validar = False
        while Validar == False:
            Opcion_Menu = input('Ingresa el número de tu preferencia: ')
            if Opcion_Menu.isdigit() and int(Opcion_Menu) > 0 and int(Opcion_Menu) < 8:
                Validar = True
            else:
                print('Ingresa un número valido.')
          
        
        Opcion_Menu = int(Opcion_Menu)
        
        """Si el valor de la variable Opcion_menu es igual a 1
            Se realizará la función agregar_un_producto()"""
        
        
        if Opcion_Menu == 1:
            agrega_un_producto(base_de_Datos)
            
            """Si el valor de la variable Opcion_menu es igual a 2
                se buscará un producto en el catálogo utilizando la función buscar_producto()."""
             
        elif Opcion_Menu == 2:
             buscar_producto(base_de_Datos)
         
             """Si el valor de la variable Opcion_menu es igual a 3
                se eliminará un producto al catálogo utilizando
                la función Eliminar_un_producto."""
                
        elif Opcion_Menu == 3:
             eliminar_un_producto(base_de_Datos)
             
             """Si el valor de la variable Opcion_menu es igual a 4 
                se mostrará el catálogo utilizando las funciones mostrar_catalogo"""
                
        elif Opcion_Menu == 4:
             
             mostrar_catalogo(base_de_Datos)
             
             """Si el valor de la variable Opcion_menu es igual a 5
                se cargará el  catálogo. utilizando la función cargar base de datos().
                a la variable base_de_Datos se le asignara el valor resultante de la función antes mencionada."""
         
        elif Opcion_Menu == 5:
             base_de_Datos = cargar_catalogo()
             
             """Si el valor de la variable Opcion_menu es igual a 6
             se guardará el catálogo utilizando la función Guardar_catalogo()."""
             
        elif Opcion_Menu == 6:
             guardar_catalogo(base_de_Datos)
             
             """Si el valor de la variable Opcion_menu es igual a 7 utilizamos la función .exit() del 
                 modulo sys para cerrar el programa. Se muestra el mensaje 'Exit'"""
         
        elif Opcion_Menu == 7:
             print('\nExit')
             """Utilizamos la función .exit() del 
                modulo sys para cerrar el programa."""
            
             sys.exit()
             
    
main(base_de_Datos)

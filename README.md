[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/LCXMIOgt)

**Proyecto**
 
**Diagrama estructural:**

[![Proyecto-Final-page-0001.jpg](https://i.postimg.cc/nzM7mM37/Proyecto-Final-page-0001.jpg)](https://postimg.cc/phbpbVbX)



**Descripción del diagrama estructural y funcionamiento del programa:**

En el bloque main se seleccionará que bloque del programa se ejecutará.
El bloque main se ejecutará en bucle hasta que se seleccione el bloque de Salir.

Para el bloque de Agregar_producto requieren de dos entradas:
- El tipo Int que determina que función voy a tomar dentro del bloque Agregar_producto.
- El tipo Str para agregar toda la información del producto.
Ese bloque tiene como salida el catálogo con el producto ya asignado al catálogo.

El bloque Buscar_producto requieren como entrada una cadena tipo Str para buscar dentro del catálogo todos.
los productos semejantes a la búsqueda. Este bloque da como salida datos tipo Str con los productos semejantes a la búsqueda.

Para el bloque Mostrar_catalogo se requieren como entrada un dato tipo Int que determinará que función 
se deberá realizar dentro del bloque Mostrar_catalogo. Este bloque da como salida el resultado de la función seleccionada mostrando  así el catálogo o parte de él.

Para el bloque Eliminar_un_producto se requiere como entrada una cadena tipo Str para identificar de manera única el producto a eliminar. En caso de que dicha búsqueda coincida con un producto del catálogo, se hace uso de la función Seguro_eliminar para confirmar la eliminación del producto seleccionado.

Para el bloque Cargar_catalogo se requiere una entrada tipo Str para identificar el archivo a cargar.
Este programa funciona con archivos terminación .json. Si no se encuentra el archivo de dicho nombre 
o que dicho archivo no sea .json el programa tendrá un error. En completamente obligatorio utilizar archivos .json para este bloque. En caso de que dicho archivo si existe y sea tipo .json se asignara al catálogo toda la información contenida en dicho archivo.

Para el bloque Guardar_catalogo se requiere una entrada tipo Str para nombrar el archivo a guardar.

El bloque Salir ejecuta el fin del programa y del ciclo while del bloque main. Da como salida el fin del programa.

El diagrama desarrollado permitió llevar a cabo la implementación en Python sin dificultades en cuanto a la estructura general del programa.

**Documentación del módulo ingresar_datos_multimedia.py** 

Este módulo contiene funciones que son útiles para ingresar y validar datos descriptivos de productos multimedia en diferentes contextos, como servicios de streaming, bibliotecas de canciones, audiolibros u otras colecciones multimedia.

A continuacion se muestra la documentación de cada función:

Función ingresar_numero(tipo)
Esta función permite ingresar y validar un número mediante la interacción con el usuario. Recibe como parámetro tipo, que indica el tipo de dato descriptivo que se va a ingresar y validar. La función solicita al usuario que ingrese un número válido, y continúa solicitándolo hasta que se cumpla la condición. Luego, retorna el número validado.

Función ingresa_año()
Esta función valida y retorna un año ingresado por el usuario. Solicita al usuario que ingrese un número de 4 dígitos que represente un año válido. Continúa solicitando la entrada hasta que se cumplan las condiciones establecidas. Finalmente, convierte la entrada en un entero y lo retorna como el año validado.

Función ingresa_precio()
Esta función valida y retorna un precio ingresado por el usuario. Solicita al usuario que ingrese un número que represente un precio válido. Continúa solicitando la entrada hasta que se ingrese un número válido. Finalmente, retorna el precio validado.

Función ingresa_venta_renta()
Esta función asigna y valida el precio de un producto según la preferencia del usuario entre venta, renta o ambas opciones. Muestra un menú con las opciones disponibles y solicita al usuario que ingrese un número correspondiente a su preferencia. Valida la entrada y, dependiendo de la opción elegida, solicita y valida el precio de venta, el precio de renta o ambos precios. Finalmente, retorna una cadena que representa el precio validado, incluyendo la información de venta y/o renta según corresponda.

Función ingresa_nombre(tipo)
Esta función permite ingresar y validar un nombre mediante la interacción con el usuario. Recibe como parámetro tipo, que indica el tipo de producto multimedia que se va a nombrar. La función solicita al usuario que ingrese un nombre válido, que consiste en una cadena de caracteres que no contenga números. Continúa solicitando la entrada hasta que se ingrese un nombre válido, y luego lo retorna.


**Documentación del programa Proyecto_final.py:**

El programa requiere tres módulos para su correcto funcionamiento. 
Dichos módulos son: 

- sys: Se utiliza el módulo sys  para cerrar el programa utilizando la función  .exit()

- json: Se utiliza el módulo json para leer y escribir archivos del tipo '.json'.
Con este tipo de archivo guardaremos y cargaremos los catálogos. Los archivos .json se caracterizan para almacenar diccionarios dentro de Python.

- ingresar_datos_multimedia: Contiene funciones que  son útiles para ingresar y validar datos descriptivos de productos multimedia en diferentes contextos, como servicios de streaming, bibliotecas de canciones, audiolibros u otras colecciones multimedia.

Documentación de uso de cada función del programa Proyecto_final.py:

Función agrega_un_producto(base_de_Datos):
Sirve para agregar un producto al catálogo. Esta función muestra un submenú al usuario donde puede seleccionar el tipo de producto que desea agregar (pelicula, serie, documental o evento deportivo en vivo). Luego, redirige al usuario a la función correspondiente para ingresar los datos específicos del producto seleccionado.

Función ingresa_pelicula(base_de_Datos): 
Sirve para ingresar los datos de una película. Esta función solicita al usuario que ingrese el título, el director, el año de lanzamiento y precio. 
Luego, utiliza estos datos para crear un nuevo diccionario que representa la película y lo agrega a la base de datos existente.

Función ingresa_seriea(base_de_Datos): 
Sirve para ingresar los datos de una serie. Esta función solicita al usuario que ingrese el título, el director, el año de lanzamiento y precio. 
Luego, utiliza estos datos para crear un nuevo diccionario que representa la serie y la agrega a la base de datos existente.


Función ingresa_documental(base_de_Datos): 
Sirve para ingresar los datos de un documental. Esta función solicita al usuario que ingrese el título, el director, el tema, el año de lanzamiento, y precio. Luego, utiliza estos datos para crear un nuevo diccionario que representa el documental y lo agrega a la base de datos existente

Función Función ingresa_evento_deportivo(base_de_Datos): 
Sirve para ingresar los datos de un evento deportivo. Esta función solicita al usuario que ingrese el título, deporte, fecha, hora y lugar.. Luego, utiliza estos datos para crear un nuevo diccionario que representa el evento deportivo y lo agrega a la base de datos existente.

Función buscar_producto(base_de_Datos):
Esta función recibe el catálogo de productos como argumento.
Solicita al usuario una cadena de búsqueda y muestra todos los productos cuyos títulos coinciden con la cadena de búsqueda.
Realiza la búsqueda en todas las categorías del catálogo y muestra el tipo de producto al que pertenece cada coincidencia.
Si no se encuentra ningún producto, muestra un mensaje indicando que el producto no fue encontrado.

Función Eliminar_un_producto(base_de_Datos):
Esta función recibe el catálogo de productos como argumento.
Solicita al usuario el nombre exacto del producto que desea eliminar.
Busca el producto en todas las categorías del catálogo y lo elimina si se encuentra.
Si el producto no se encuentra, muestra un mensaje indicando que el producto no fue encontrado.

Función mostrar_catalogo(base_de_Datos):
Se utiliza para mostrar en pantalla el catálogo de productos disponibles en una compañía de streaming. La función recorre la base de datos de productos y muestra información detallada sobre cada uno, como el tipo de producto (película, serie, documental, evento deportivo en vivo), título, características específicas y precio. Esto ayuda a los usuarios a tener una visión general de todos los productos disponibles y les permite tomar decisiones informadas sobre qué productos desean consumir.


Función cargar_catalogo():
Esta función carga un catálogo guardado en un archivo del tipo JSON. 
Retorna el catálogo cargado o mensaje de error si el archivo no existe.

Función Guardar_catalogo(base_de_Datos):
Esta función guarda el catálogo. Para realizar esta acción utilizamos la función .load() del módulo json
En caso de mo existir el archivo, creará uno nuevo donde guardará la información.

Función ejecucion_programa(base_de_Datos):
Esta función ejecuta en bucle todo el funcionamiento del programa, se implementó de esta manera, para no perder los datos de la variable base_de_Datos entre cada opción.

Función main(base_de_Datos):
Es la función principal de un programa que maneja un catálogo de productos. Recibe como argumento base_de_Datos, que es un diccionario de diccionarios que representa el catálogo.

La función main() es responsable de controlar el flujo del programa y llamar a otras funciones según las necesidades del usuario. En este caso, el programa ofrece varias opciones para manipular el catálogo, como agregar un producto, buscar un producto, eliminar un producto, mostrar el catálogo, cargar el catálogo desde un archivo y guardar el catálogo en un archivo.

**Comentarios respecto al diseño y a la implementación del proyecto:**

Antes de empezar a programa, realizamos el esquema estructural utilizando el método top-down. 
Visualizamos la importancia de un módulo que ingresaría y validaría cualquier característica de cualquier tipo de producto multimedia (Para que así fuera de uso general).

Estructuramos los módulos para satisfacer problemas pequeños que a su vez resolvieran el problema principal. 
Definimos nuestra base de datos como un solo diccionario. Llegamos a la conclusión que podríamos aprovechar de mejor manera las características de los diccionarios dentro de Python. Podríamos así buscar, eliminar o agregar productos utilizando las claves de los diccionarios.
Por conclusión nuestro diccionario era un diccionario de diccionarios.
El diccionario vació arrancaría con el programa para un mejor funcionamiento de este.

Teníamos juntas cada tres días para apoyarnos como equipo y así implementar de mejor manera las funciones repartidas por integrante.
Con el diagrama bien estructurado, implementar las funciones resulto más sencillo. Lo último fue depurar los códigos hasta optimizar cada función y así obtener un programa que satisface el problema de manera clara y estructurada.

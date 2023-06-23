[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/LCXMIOgt)
**Proyecto**

**Diagrama de estructura:**

![Screenshot_137](https://github.com/agn-pe-23i/proyecto-escuadron_lobo/assets/125081169/e81cec67-6e82-4165-928f-5d15ff5d5903)

**Documentación del módulo Validar_datos.py**

El módulo "Valdar_datos.py" proporciona una serie de funciones para validar diferentes tipos de datos. Se diseñó prioritariamente para el programa Proyecto_final.py.

Documentación de uso de cada función del módulo Validar_datos.py:

Función validar_numero_rango(a, b):
Esta función valida un número ingresado por el usuario dentro de un rango especificado. Toma dos argumentos: a y b, que representan el número mínimo + 1 y el número máximo - 1 que el usuario puede introducir para que éste sea válido. La función solicita al usuario un número válido hasta que se cumpla la condición establecida. Retorna el número validado ingresado por el usuario.

Función validar_numero():
Esta función valida que la entrada del usuario sea un número entero. Utiliza una condicional while para solicitar al usuario un número válido hasta que se cumpla la condición establecida. Retorna el número validado ingresado por el usuario.

Función validar_año():
Esta función valida que la entrada del usuario sea un año de 4 dígitos. Utiliza una condicional while para solicitar al usuario un número de 4 dígitos válido hasta que se cumpla la condición establecida. Retorna el año validado ingresado por el usuario.

Función validar_precio():
Esta función valida que la entrada del usuario sea un precio válido. Utiliza una condicional while para solicitar al usuario un precio válido hasta que se cumpla la condición establecida. Retorna el precio validado ingresado por el usuario.

Función validar_venta_renta():
Esta función valida y asigna el valor del precio según la opción elegida por el usuario (venta, renta o ambos). Muestra un menú al usuario para que elija una opción y luego utiliza otras funciones de validación para obtener los precios correspondientes. Retorna el precio validado según la opción elegida por el usuario.

Función validar_s_n():
Esta función valida la opción ingresada por el usuario entre 'S' (sí) y 'N' (no). Utiliza una condicional while para solicitar al usuario una opción válida hasta que se cumpla la condición establecida. Retorna un valor booleano True si se elige 'S' (sí) o False si se elige 'N' (no).

Función validar_director():
Esta función valida que la información ingresada por el usuario para el nombre del director sea una cadena de letras. Utiliza una condicional while para solicitar al usuario un nombre válido hasta que se cumpla la condición establecida. Retorna el nombre del director validado ingresado por el usuario.

**Documentación del programa Proyecto_final.py:**

El programa requiere tres módulos para su correcto funcionamiento. 
Dichos módulos son: 

- sys: Se utiliza el módulo sys  para cerrar el programa utilizando la función  .exit()

- json: Se utiliza el módulo json para leer y escribir archivos del tipo '.json'.
Con este tipo de archivo guardaremos y cargaremos los catálogos. Los archivos .json se caracterizan para almacenar diccionarios dentro de Python.

- Validar_Datos: Se utiliza el módulo Validar_datos.py para validar múltiples tipos de datos.
El módulo fue diseñado prioritariamente para el programa proyecto_Final.py. 

Documentación de uso de cada función del programa Proyecto_final.py:

Función seleccion_menu():
Esta función muestra al usuario un menú con varias opciones y solicita al usuario que seleccione una opción.
Utiliza la función validar_numero_rango() del módulo Validar_datos para validar la entrada del usuario y asegurarse de que la opción seleccionada esté dentro del rango válido.
Retorna la opción seleccionada del menú.

Función tipo_de_producto_a_ingresar(base_de_Datos):
Esta función muestra al usuario un submenú para seleccionar el tipo de producto que desea agregar al catálogo.
Utiliza la función validar_numero_rango() del módulo Validar_datos para validar la entrada del usuario y asegurarse de que la opción seleccionada esté dentro del rango válido.
Asigna a la variable Opcion_a_ingresar el nombre de la categoría del producto seleccionado.
Si el usuario selecciona la opción "Regresar", se llama a la función ejecucion_programa(base_de_Datos) para volver al menú principal.
Retorna la opción seleccionada.

Función ingresa_datos(Opcion_a_ingresar, base_de_Datos):
Esta función recibe la opción seleccionada y el catálogo de productos como argumentos.
Dependiendo de la opción seleccionada, solicita al usuario los datos necesarios para agregar un producto al catálogo.
Utiliza las funciones del módulo Validar_datos para validar los datos ingresados por el usuario.
Crea un diccionario con los datos del producto y lo agrega al catálogo bajo la categoría correspondiente.
Retorna el catálogo actualizado.

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

Función Menu_mostrar_catalogo():
Muestra un submenú dentro del programa que muestra las opciones disponibles para mostrar el catálogo. A cada acción le corresponde el nombre de la categoría o instrucción que desea. Dicha correspondencia se asigna por medio de condicionales if, elif y else. Esta función retorna la opción para mostrar el catálogo

Función Mostrar_catalogo(base_de_Datos, opcion_mostrar_catalogo):
Esta función utiliza el catálogo (base_de_Datos) y la opción seleccionada (opcion_mostrar_catalogo) como argumentos. Según la opción seleccionada en la función Menu_mostrar_catalogo(), se realiza la acción correspondiente para mostrar el catálogo.
Cada tipo de producto cuenta con elementos característicos del propio. 
De acuerdo con la opción requerida por el usuario, por medio de citar las claves de dichas características se muestra al usuario la concatenación del nombre del producto con todas las características de dicho producto. 

Función cargar_catalogo():
Esta función carga un catálogo guardado en un archivo del tipo JSON. 
Retorna el catálogo cargado o mensaje de error si el archivo no existe.

Función Guardar_catalogo(base_de_Datos):
Esta función guarda el catálogo. Para realizar esta acción utilizamos la función .load() del módulo json
En caso de mo existir el archivo, creará uno nuevo donde guardará la información.

Función ejecucion_programa(base_de_Datos):
Esta función ejecuta en bucle todo el funcionamiento del programa, se implementó de esta manera, para no perder los datos de la variable base_de_Datos entre cada opción.

Función main():
Esta función inicia nuestro programa con una base de datos sin productos. Esta base de datos la guarda en la variable base_de_Datos para ser utilizada por la funcion ejecucion_programa(base_de_Datos) y dicha infomación ser modificada por el funcionamiento de la función ejecucion_programa(base_de_Datos).

**Comentarios respecto al diseño y a la implementación del proyecto:**

Antes de empezar a programa, realizamos el esquema estructural utilizando el método top-down. Visualizamos la importancia de un módulo el cual validara la información ingresada por el usuario. Dicho modulo seria utilizando por la función que ingresara datos los datos.

Estructuramos los módulos para satisfacer problemas pequeños que a su vez resolvieran el problema principal. 

Decidimos que también usaríamos el módulo para validar datos al momento de validar las opciones entre el menú y los sub-menú.

Tuvimos un error al momento de implementar el esquema estructural el cual fue en no pensar en un módulo que mantuviera en bucle todo el programa. Lo que causaba dicho erro era que el programa se "cerraba" antes de tiempo. Dicho error ya está corregido el esquema estructural mostrado en este archivo.

Definimos nuestra base de datos como un solo diccionario. Llegamos a la conclusión que podríamos aprovechar de mejor manera las características de los diccionarios dentro de Python. Podríamos así buscar, eliminar o agregar productos utilizando las claves de los diccionarios.
Por conclusión nuestro diccionario era un diccionario de diccionarios.
El diccionario vació arrancaría con el programa para un mejor funcionamiento de este.

Teníamos juntas cada tres días para apoyarnos como equipo y así implementar de mejor manera las funciones repartidas por integrante.

Con el diagrama bien estructurado, implementar las funciones resulto más sencillo. Lo último fue depurar los códigos hasta optimizar cada función y así obtener un programa que satisface el problema de manera clara y estructurada.

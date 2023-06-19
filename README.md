[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/LCXMIOgt)
**Proyecto**

**Diagrama de estructura:**

[![Dise-o-sin-t-tulo.jpg](https://i.postimg.cc/CLfXG0H5/Dise-o-sin-t-tulo.jpg)](https://postimg.cc/TpftxZsv)

**Documentación del modulo Validar_datos.py:**

El módulo "Valdar_datos.py" proporciona una serie de funciones para validar diferentes tipos de datos. Se diseñó prioritariamente para el programa Proyecto_final.py.

Función validar_numero_rango(a, b):
Esta función valida un número ingresado por el usuario dentro de un rango especificado. Toma dos argumentos: a y b, que representan el número mínimo + 1 y el número máximo - 1 que el usuario puede introducir para que sea válido. La función solicita al usuario un número válido hasta que se cumpla la condición establecida. Retorna el número validado ingresado por el usuario.

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
Estas son algunas de las funciones del programa. El código también incluye la importación de módulos necesarios, como sys y json, así como el módulo personalizado Validar_datos, que contiene funciones para validar diferentes tipos de datos. Además, hay una breve descripción del programa y se define una variable base_de_Datos como un diccionario de diccionarios para almacenar el catálogo de productos.

**Comentarios respecto al diseño y a la implementación del proyecto:**



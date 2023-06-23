'''
Autor: Abad Ramírez Gamaliel 
Módulo: ingresar_datos_multimedia.py

Este módulo incluye funciones para ingresar y validar datos descriptivos de 
productos multimedia.
Estas funciones se pueden utilizar para ingresar de manera más sencilla 
características de productos para algún servicio
de streaming por ejemplo Netflix, HBO Max, Blim, etc.
'''


def ingresar_numero(tipo):
    
    """Esta función valida que la entrada sea una cadena de números.
    La variable tipo es para que el programador de detalle del dato descriptivo
    a ingresar y validar.
    x es igual a el número a validar.
    Retorna la entrada validada."""
    
    # Por medio de una condicional while se pedirá al usuario una entrada valida
    # hasta que la condicional if se cumpla
    
    Validar = False
    while Validar == False:
        x = input(str(tipo))
        if x.isdigit():
            Validar = True
        else:
            print('Ingresa un número válido.')
    return x

def ingresa_año():
    
    """Esta función valida que la entrada sea una cadena de números y dicha cadena
    tenga una longitud igual a 4.
    x es igual al año a validar.
    Retorna la entrada validada."""
    
    # Por medio de una condicional while se pedirá al usuario una entrada valida
    # hasta que la condicional if se cumpla
    
    Validar = False
    while Validar == False:
        x = input('Año: ')
        if x.isdigit() and len(x) == 4:
            Validar = True
        else:
            print('Ingresa un número de 4 dígitos. ')
    
    x = int(x)
    return x

def ingresa_precio():
    
    """Esta función valida que la entrada sea una cadena de dígitos. 
    A diferencia de la función ingresar_número(), esta función se especializa en 
    el precio e imprimirá el mensaje 
    'Ingresa un precio valido' si no es válida la entrada 
    Retorna el precio validado."""
    
    # Por medio de una condicional while se pedirá al usuario una entrada valida
    # hasta que la condicional if se cumpla


    Validar = False
    while Validar == False:
        precio = input('Precio: ')
        if precio.isdigit():
            Validar = True
        else:
            print('Ingresa un precio valido ')
    
    return precio

def ingresa_venta_renta():
    
   """Esta función asigna y valida el valor del precio de acuerdo con lo que el usuario 
   necesite (venta, renta o ambos). Utilizando una estructura de control while se valida que 
   la opcion del sub_menú ingresada sea un numero mayor a o y menor a 4.
   De acuerdo con el menú impreso, el usuario decidirá que opción tomar.
   Rentorna el precio validado."""
    
   Validar = False
    
   print(' \n Precio: \n\n'
          '1. Venta \n'
          '2. Renta \n'
          '3. Ambos \n')
   
   Validar = False
   while Validar == False:
       x = input('Ingresa el número de tu preferencia: ')
       if x.isdigit() and int(x) > 0 and int(x) < 4:
           Validar = True
       else:
           print('Ingresa un número valido.')
  
   x = int(x)
   
    
   if x == 1:
        precio = ingresa_precio()
        precio_definitivo = ' Venta: ' + str(precio) + '$'
   elif x == 2:
        precio = ingresa_precio()
        precio_definitivo = ' Renta: ' + str(precio) + '$'
   else:
        while Validar == False:
            Precio_venta = input('Ingresa el precio de venta: ')
            if Precio_venta.isdigit():
                Validar = True 
            else: 
                print('Ingresa un precio valido: ')
        
        while Validar == True:
            Precio_renta = input('Ingresa el precio de renta: ')
            if Precio_renta.isdigit():
                Validar = False
            else: 
                print('Ingresa un precio valido ')
        
        precio_definitivo = ' Venta: ' + str(Precio_venta) + '$' + ' Renta: ' + (Precio_renta) + '$'
            
   return precio_definitivo   


def ingresa_nombre(tipo):
    
    """ Esta función valida que la información ingresada sean letras y no números
    Esta función es muy versátil ya que sirve para nombrar cualquier característica del
    producto multimedia que involucre solo letras y no números.
    La variable tipo sirve para ingresar el tipo de producto a nombrar.
    Retorna la entrada validada."""
    
    Validar = False
    while Validar == False:
        nombre = input(str(tipo))
        if nombre.isalpha():
            Validar = True
        else:
            print('Ingresa un nombre válido: ')
    
    return nombre

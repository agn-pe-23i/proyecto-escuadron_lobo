'''
Autor: Abad Ramírez Gamaliel 
Módulo: Valdar_datos.py

Este módulo incluye funciones para validar datos.
'''

def validar_numero_rango(a,b):
    
    """ Esta función requiere dos argumentos (a,b):
    (a) requiere ser un tipo de dato entero. Indica cual será el
    número menor + 1 que puede introducir el usuario para ser válido.
    (b) requiere ser un tipo de dato entero. Indica cual será el 
    número mayor - 1 que puede introducir el usuario para ser válido.
    La variable x es la entrada. La función retorna x."""
    
    # Por medio de una condicional while se pedirá al usuario una entrada valida
    # hasta que la condicional if se cumpla

    Validar = False
    while Validar == False:
        x = input('Ingresa el número de tu preferencia: ')
        if x.isdigit() and int(x) > a and int(x) < b:
            Validar = True
        else:
            print('Ingresa un número valido.')
   
    x = int(x)
    return x

def validar_numero():
    
    """Esta funcion valida que la entrada sea un digito.
    x es igual a el número a validar.
    Retorna la entrada validada."""
    
    # Por medio de una condicional while se pedirá al usuario una entrada valida
    # hasta que la condicional if se cumpla
    
    Validar = False
    while Validar == False:
        x = input()
        if x.isdigit():
            Validar = True
        else:
            print('Ingresa un número.')
    return x

def validar_año():
    
    """Esta función valida que la entrada sea una cadena de digitos y dicha cadena
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

def validar_precio():
    
    """Esta función valida que la entrada sea una cadena de dígitos. 
    A diferencia de la función validar_numero(), esta función  imprimirá el mensaje 
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

def validar_venta_renta():
    
   """Esta función asigna y valida el valor del precio de acuerdo con lo que el usuario 
   necesite (venta, renta o ambos). Llamando a la funcion validar_numero_rango()
   y de acuerdo con el menú impreso, el usuario decidirá que opción tomar.
   Rentorna el precio validado."""
    
   Validar = False
    
   print(' \n Precio: \n\n'
          '1. Venta \n'
          '2. Renta \n'
          '3. Ambos \n')
   
   # Utilizando condicionales if se determina que opción desea el usuario.
   x = validar_numero_rango(0, 4) 
       
   if x == 1:
        precio = validar_precio()
        precio_definitivo = ' Venta: ' + str(precio) + '$'
   elif x == 2:
        precio = validar_precio()
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

def validar_s_n():
 
    """ Esta función valida la opcion entre 'S' = Si, 'N' = No.
    Esta especialmente diseñada para la eliminación de elementos dentro de un diccionario.
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

def validar_director():
    
    """ Esta función valida que la información ingresada sean letras y no números.
    Se puede utilizar para validar nombres personales y apellidos. 
    Retorna la entrada validada."""
    
    Validar = False
    while Validar == False:
        director = input('Director@: ')
        if director.isalpha():
            Validar = True
        else:
            print('Ingresa un nombre válido: ')
    
    return director



    


    

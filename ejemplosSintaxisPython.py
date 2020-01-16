#Este archivo es unicamente introductorio a la sintaxis de este lenguaje version 3, ver markdown para una explicacion mas detallada
#python no tiene multilinea en los comentarios

import random # python no tiene un metodo como random() en otros lenguajes, es necesario importar esta libreria que viene por defecto: uso linea 70
def suma(): # manera de declarar una funcion, NOTA: en python es muy importante la identacion
    numero1 = 10; #python no es un lenguaje de tipado requerido, por lo tanto las variables y su tipo se identifican una vez se asigna un valor 
    numero2 = 2;
    respuesta = 0;

    respuesta = numero1 + numero2;
    print("esta es la respuesta: "+ str(respuesta)); #estamos imprimiendo un string, por lo tanto en debemos covertir el valor numerico a string para que sean compatibles


def obtenerTipoDato():
    variable1 = 10; 
    variable2 = "perro";
    variable3 = False;
    variable4 = b"Hello";
    variable5 = ["apple", "banana", "cherry"]

    print(type(variable1)); #metodo para determinar el tipo de dato de una variable
    print(type(variable2));
    print(type(variable3));
    print(type(variable4));
    print(type(variable5));


def especificacionTipoDato():
    variable1 = str("cadena");
    variable2 = int(2);
    variable3 = float(2.1);
    variable4 = list(("perro", "gato", "chivo"));

    print(type(variable1)); #metodo para determinar el tipo de dato de una variable
    print(type(variable2));
    print(type(variable3));
    print(type(variable4));

    print(variable1); #valor de la variable
    print(variable2);
    print(variable3);
    print(variable4);


variableGlobal = "bueno";
def variablesGlobales():
    global variableGlobal;
    variableGlobal = "excelente";


def conversiones():
    #para realizar un cast practicamente se requiere el tipo de valor al que se desea convertir un tipo de dato ejemplo: str(dato)
    entero = 1;
    flotante = 1.2
    complejo = 1j;

    conversionEnteroFlotante = float(entero)
    conversionFlotanteEntero = int(entero)
    conversionEnteroComplejo = complex(entero)

    print(conversionEnteroFlotante);
    print(conversionFlotanteEntero);
    print(conversionEnteroComplejo);
    
    print(type(conversionEnteroFlotante));
    print(type(conversionFlotanteEntero));
    print(type(conversionEnteroComplejo));


def numeroRandom():
    print(random.randrange(1,10)); #generando un numero aleatorio, ocupo una libreria ver linea 4

def caracteristicasTipoString():
    #cadenas de texto
    cadena1 = 'prueba'; #no importa el tipo de comilla
    cadena2 = "prueba2";
    cadenaMultilinea = """Lorem ipsum dolor sit amet,
    consectetur adipiscing elit,
    sed do eiusmod tempor incididunt
    ut labore et dolore magna aliqua."""; #cadena multilinea
    print(cadena1);
    print(cadena2);
    print(cadenaMultilinea);
    print(cadena2[0:3])# de una cadena puedo seleccionar lo unico que deseo imprimir seleccionado un rango (comportamiento  de arreglo), si pongo los numeros en negativo comienza a contar desde el fin de la palabra
    print("tamaño de cadena con len linea 85: ",len(cadena2)); #funcion len para regresar la longitud de una cadena 
    print("reemplazar p por c: ",cadena2.replace("p","c")); #funcion len para regresar la longitud de una cadena 
    
    #metodos interesantes:
    #   - cadena.strip(): quita cualquier espacio del inicio de la cadena, si tengo " hola", regresa "hola"     
    #   - cadena.lower(): convierte toda la cadena a minisculas, si existen mayusculas si tengo "HOla" regresa "hola"
    #   - cadena.upper(): hace lo contrario de la anterior, si tengo minusculas, convierte todo a mayusculas
    #   - cadena.split(","): al igual que otros lenguajes regresa un arreglo sin el caracter especificado en el metodo



#invocacion de funciones
suma(); #mando llamar una funcion
obtenerTipoDato();
especificacionTipoDato();
conversiones();
numeroRandom();
variablesGlobales();
print("python es: "+variableGlobal); #lo invoco aqui para que se modifique la variable con el metodo de arriba, puedes mover esta linea arriba de la funcion variablesGlobales para ver la diferencia
caracteristicasTipoString();    
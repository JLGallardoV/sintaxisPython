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
    cadena1 = 'pru3ba'; #no importa el tipo de comilla
    cadena2 = "PRUEBA";
    cadenaMultilinea = """Lorem ipsum dolor sit amet,
    consectetur adipiscing elit,
    sed do eiusmod tempor \"incididunt"\
    ut labore et dolore magna aliqua."""; #cadena multilinea y uso de comillas
    print(cadena1);
    print(cadena2);
    print("obtiene el primer caracter de una cadena "+cadena1[0]); #obtenemos el caracter de determinada posicion
    print("todas son mayuculas en cadena2?",cadena2.isupper()); #regresa un boleano si todas las letras son mayusculas
    print("todas son minusculas en cadena1?",cadena1.islower()); #regresa un boleano si todas las letras son minusculas
    print("todas son letras del alfabeto en cadana1?",cadena1.isalpha()); #regresa un boleano si todas las letras perteneces al abecedario, en este ejemplo regresa false ya que hay numeros NOTA los espacios cuentan como caracter
    print("regresa la posicion del caracter 3 si existe en la cadena1?",cadena1.find("3",0,5)); #busca un caracter y regresa su posicion  ("caracter",inicioRango,finRango), si no lo encuentra regresa un -1
    print("concatenacion de cadenas: "+cadena1+" "+cadena2);
    print(cadenaMultilinea);
    print(cadena2[0:3])# de una cadena puedo seleccionar lo unico que deseo imprimir seleccionado un rango (comportamiento  de arreglo), si pongo los numeros en negativo comienza a contar desde el fin de la palabra
    print("tamaño de cadena con len linea 85: ",len(cadena2)); #funcion len para regresar la longitud de una cadena 
    print("reemplazar p por c: ",cadena2.replace("p","c")); #funcion len para regresar la longitud de una cadena 
    
    inspeccionar = "buscare una palabra en esta frase";
    encontrar = "palabra" in inspeccionar; #regresa verdadero o falso si se encuentra una coincidencia en la variable string anterior, si en lugar de poner in ponemos not in verifica que no haya coincidencias
    print("hubo una coincidencia: "+str(encontrar)); #no es compatible string con boleano por eso hago un cast

    numerico1 = 3
    numerico2 = 567
    numerico3 = 49.95
    cadenaTexto = "valor numerico 1: {2} valor numerico 2: {1} valor numerico 3: {0} concatenados sin convertir a str." #manera de anexar variables a una cadena de texto sin tener que convertir a string, los indices en las llaves son para dar orden en caso de querer un lugar especifico NO SON OBLIGATORIAS 
    print(cadenaTexto.format(numerico1, numerico2, numerico3))


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
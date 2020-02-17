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


def evaluarSentencias():
    print("9 es mayor que 21?");
    print(9>21); # nos imprime un boleano si la sentencia de adentro se cumple
    print("4 es igual que 4?")
    print(4==4);

    #uso de condicional if
    a = 10;
    b = 11;

    if a < b:
        print("a es menor que b");
    else:
        print("a NO es menor que b");

    #funcion predefinida de python la cual nos arroja un booleano si se cumple un sentencia con relacion a los tipos de dato de un objeto
    variable = 120;
    print(isinstance(variable,int));

def usarOperadores():
    #en esta funcion solo se mostraran operadores no tan basicos

    numero1 = 3;
    numero2 = 2;

    #aritmeticos: para operaciones aritmeticas
    print("modulo");
    print(numero1%numero2); #modulo, practicamente es el residuo de una división
    print("exponencial");
    print(numero1**numero2); #exponencial, 10 * 10 * 10
    print("division piso");
    print(numero1 // numero2); #division piso, arroja el resultado de una division rededondeando el resultado menor o igual a .5 entonces se queda con el entero y mayor a .5 nos regresa el entero siguiente

    #asignacion: aqui como en otros lenguajes no se permite el i++ o i-- se expresan ya sea de su manera ordinaria o de la sieguiente manera 
    numero1 += 2 #es lo mismo que numero1 = numero1 + numero2
    numero1 **= 1 #es lo mismo que numero1 = numero1 ** numero2
    numero1 //= 3 #es lo mismo que numero1 = numero1 // numero2
    print("uso de += "+str(numero1)); 
    print("uso de **= "+str(numero1)); 
    print("uso de //= "+str(numero1)); 

    #comparacion
    print(9>21); #como ya sabes nos regresan una expresion booleana, existen mas, para un ejemplo practico solo pongo esos (<=, ==, !=)    
    print(9<21);    
    print(9>=21);

    #logicos: usados para condicionar una expresion
    print("condicional AND: ");    
    print(numero1 > numero2 and numero2 < numero1); #tambien regresan una expresion booleana
    print("condicional OR: ");    
    print(numero1 > numero2 or numero2 < numero1); #tambien regresan una expresion booleana
    print("condicional NEGACION: ");    
    print(not(numero1 > numero2 and numero2 < numero1)); #tambien regresan una expresion booleana

    #identidad: compara si una expresion y su contenido es identico, de caso contrario regresa un booleano
    print("la variable uno y su contenido es igual a la variable 2? ")    
    print(numero1 is numero2);
    print("la variable uno y su contenido NO es igual a la variable 2? ")    
    print(numero1 is not numero2);

    #membresia: verifica si una expresion esta presente en alguna secuencia (una lista por ejemplo)
    lista = ["perro", "gato"];
    print("perro esta en la lista? ");
    print("perro" in lista); #perro esta en la lista?
    print("burro esta en la lista? ");
    print("burro" not in lista); #burro no esta en la lista?

def usarListas():
    #son algo asi como arreglos pero nos permiten añadir diferentes tipos de datos en esta estructura 
    lista = ["perro",2,[1,1],"vaca"];
    print("esto es una lista" + str(lista));
    print("accediendo a un elemento de una lista: "+str(lista[0]));
    print("imprimiendo un determinado rango en la lista"+str(lista[0:1]));# nota: el inicio del rango se incluye pero el fin del rango no se incluye(en la extraccion)

    #metodos que se pueden invocar en una lista
    lista.append("chivo");
    print("se agrego un chivo a la lista "+ str(lista));
    lista.extend("hola");
    print("se añadio un hola "+ str(lista)); #cada elemento a añadir se agrega caracter por caracter idependientemente sea una cadena
    print("devolviendo el indice de perro en la lista: "+str(lista.index("perro")));
    print("cuantas existe perro en la lista? "+str(lista.count("perro")));
    lista.remove("perro");
    print("se elimino perro :"+str(lista));


def usarTuplas():
    #Las tuplas son colecciones ordenadas y no pueden cambiar (inmutables), es decir, son estaticas y sin posibilidad de modificar sus elementos
    tupla1 = ("perro",1,"puerco");
    tupla2 = ("a","b","c")
    print("esta es una tupla: "+str(tupla1));
    print("imprimiendo un determinado rango en la tupla"+str(tupla1[0:1]));# nota: el inicio del rango se incluye pero el fin del rango no se incluye(en la extraccion)
    tupla3 = tupla1 + tupla2;
    print("concatenando tuplas: "+str(tupla3));  

 
def usarSets():
    #un conjunto es una coleccion la cual no esta ordenada ni indexada por tal motivo no podemos acceder a su posicion mediante un indice como lo es en un arreglo
    conjunto = {"perro","chivo","lagarto"};
    conjunto1 = {1,2,"perro"};
    
    print("eso es un conjunto: "+str(conjunto));
    
    #metodos que se pueden usar en un conjunto
    print("hay un lagarto en el conjunto: "+str("lagarto" in conjunto));
    conjunto.add("cebra"); #no podemos modificar los elementos de un conjunto pero si podemos añadir nuevos elementos
    print("añadimos una nuevo animal al conjunto" + str(conjunto));
    conjunto.update(["pez","gallina","gato"]); #añadimos mas de un elemento al conjunto
    print("añadimos mas de un animal al conjunto" + str(conjunto));
    print("cuantos elementos hay en el conjunto: "+str(len(conjunto)));
    conjunto.remove("chivo"); #eliminado el elemento chivo, si no existe el elemento marcará un error   
    print("se elimino el chivo del conjunto: "+str(conjunto));
    conjunto.discard("pez"); #eliminado el elemento chivo, si no existe el elemento NO marcará error   
    print("se elimino el pez del conjunto: "+str(conjunto));
    conjunto.pop(); #recuerda que una caracteristica de los conjuntos es que no son ordenados, por ende en esta funcion no sabras que elemento se elimino
    print("se elimino el algun elemento del conjunto: "+str(conjunto));
    print("eliminare todos los elementos del conjunto: "+str(conjunto.clear()));
    conjunto = {"perro","chivo","lagarto"};
    conjunto2 = conjunto.union(conjunto1); #haciendo una union de conjuntos, si hay un elemento que se repita en ambos conjuntos solo lo pone una vez
    print("este es el conjunto 2, resultado de una union: "+str(conjunto2));
    conjunto2 = conjunto.intersection(conjunto1); #haciendo una interseccion de conjuntos, si hay un elemento que se repita en ambos conjuntos es el que muestra
    print("este es el conjunto 2, resultado de una interseccion: "+str(conjunto2));


def usarDiccionarios():
    #los diccionarios son algo asi como objetos, donde contienen sus propiedad (key en python) y valor (value), son desordenados pero indexados y editables
    diccionario = {
        "nombre": "jose",
        "apellidoP": "gallardo",
        "edad": 22
    }

    print("este es un diccionario: "+ str(diccionario))
    #manipulacion de diccionarios
    print("extrayendo el valor del key nombre del diccionario :"+diccionario["nombre"]); #usando el metodo get("nombre") tenemos el mismo resultado
    diccionario["nombre"] = "luis";
    print("cambiando el valor del key nombre del diccionario :"+diccionario.get("nombre"));
    for i in diccionario:
        print("recorriendo con un for un diccionario: "+str(i)); #aqui solo devolvemos las keys del diccionario
        print("valores del diccionario recorridos mediante un for: "+str(diccionario[i])); #aqui si devuelven sus valores
     
    for i in diccionario.values():
        print("asi tambien puedo obtener los valores del diccionario: "+str(i));

    for i,j in diccionario.items():
        print("asi imprimo practicamente el key con su respuectivo valor: "+str(i) +" "+str(j)); # si solo uso la variable i, la impresion esta entre parantesis (key:value)

    if "nombre" in diccionario:
        print("la key nombre se encuentra en el diccionario");
    
    print("imprimimos la longitud (numero de keys) del diccionario: "+str(len(diccionario)));

    diccionario["origen"] = "abasolo";# de esta manera se añade una nueva key con su respectivo valor
    print("aqui se agrego una nueva key con un valor al diccionario: "+str(diccionario));

    diccionario.pop("apellidoP"); #asi eliminamos una key y su valor de un diccionario
    print("eliminamos la key y su valor de apellidoP: "+str(diccionario));
    diccionario.popitem(); #remueve el ultimo elemento del diccionario
    print("removimos el ultimo elemento del diccionario: "+str(diccionario));
    diccionarioCopia = diccionario.copy();
    print("este es un diccionario copiado "+str(diccionarioCopia));
    print("vaciamos por completo el diccionario: "+ str(diccionario.clear())); # podemos usar del diccionario, pero esta palabra reservada elimina por completo el diccionario marcando un error por indefinida  

    #diccionarios anidados (practicamente son objetos pero se acceden de manera diferente, esto es obvio, pues es otro lenguaje):
    miFamilia = {
        "papa":{
            "nombre":"juan",
            "edad":36
        },
        "mama":{
            "nombre":"maria",
            "edad":32
        },
        "hermano":{
            "nombre":"juan jr",
            "edad":27
        }
    }
    print("este es un diccionario anidado: "+str(miFamilia));
    nuevoDiccionario = dict(raza = "doberman",edad = 23); #podemos usar el constructor para crear un nuevo diccionario
    print("de esta manera tambien puedo crear un diccionario: "+str(nuevoDiccionario));


def condicionalIf():
    #los if se manejan como en cualquier otro lenguaje a diferencia que aqui no se usan las llaves debido a que python trabaja con identacion y no con llaves
    variable1 = 200;
    variable2 = 100;
    
    if variable1 > variable2:
        print("entro en el IF del primer condicional");
    
    if variable2 > variable1:
        print("que raro") 
    else:
        print("entro en el ELSE del segundo condicional");

    if variable2 > variable1:
        print("que raro")
    elif variable1 > variable2:
        print("entro en un ELIF del tercer condicional");
    
    #print en una linea, el primer print es como si se ejecutara si el if se cumple, el segundo es como si el else se cumpliera
    print("if de una linea variable 1 fue mayor") if variable1 > variable2 else print("if de una linea variable 2 fue mayor");
    

def ciclosForWhile():
    #ciclo while; se detiene el ciclo hasta que la condicion resulte false
    i = 0
    animales = ["perro","chivo","caballo","puerco","tejon"];#lista a iterar
    descripciones = ["pequeño","barbon","veloz","gordo","agresivo"];#lista a iterar
    while i < 10:
        i += 1; #como ya se comento esto es igual a usar i++ en otros lenguajes
        if i ==4:
            continue #simplemente se salta esa iteracion, si te fijas en los print no pinta el 4
        if i == 7:
            break; #rompe completamente el ciclo sin importar si la condicion del while no ha sido aun false
        print("while ejecutandose"+str(i)+" vez(ces)");

    
    #ciclo for; no se parece tanto al de otros lenguajes, ya que este no contiene una condicional relacional, simplemente recorre una
    # estructura de datos (itera cada uno de sus elementos hastas que pasa por cada uno de ellos)
    for animal in animales:
        if animal == "perro":
            continue #al igual que en un ciclo while, aqui tambien se puede usar un continue para saltar la actual iteracion 
        if animal == "puerco":
            break #al igual que en un ciclo while, aqui tambien se puede usar un breack para rompler el ciclo 
        print("ciclo for, elemento: "+animal);

    #el metodo range nos ayuda a llevar acabo un ciclo pero con un numero de iteraciones limite (el que defines en el parametro), 
    #esto hace un for mas parecido a los que conocemos en otros lenguajes
    #nota, podemos hacer rangos(2,4) de 2 a 4(no incluido) otra manera es range(2,20,2) indica del 2 al 20 (no incluido) pero de 2 en 2
    for animal in range(4): 
        print("ciclo for con rango: "+animales[animal]);

    #for anidado
    for animal in animales:
        for descripcion in descripciones:
            print("este es un for anidado: "+str(animal),str(descripcion));
    
    #la palabra reservada pass nos ahorra un error en consola en caso de que por alguna extraña razon no se pueda iterar un ciclo
    for animal in animales:
        pass;
    

def funcionesConParametros(nombre):
    #recibiendo parametros en una funcion, al momento de su invocacion se debe hacer uso del numero de parametros establecidos
    print("hola: ",str(nombre));


def funcionesConParametrosDesconocidos(*personas):
    #cuando no se sabe el numero de parametros se antepone el caracter "*" para permitir un numero desconocido de parametros 
    print("estas son las personas presentes: ",personas);


def funcionesConKeyboard(parametro1,parametro2):
    #para establecer desde el paso de parametros que parametro pertenece a quien, se usan los keyboards (ver invocacion de la funcion)
    print("mira el orden de los parametros: ",parametro1," - ",parametro2); 


def funcionesConKeyboardDesconocido(**personas):
    # si se tienen varios parametros desconocidos y se quiere añadir un orden de toma de valores se usa **
    print("mira que parametro estoy tomando: ",personas["segundo"])


def funcionConValorPorDefecto(parametro = "buenos dias"):
    #establecemos un parametro por defecto, en caso de no pasarle el parametro en su invocacion, entonces toma el "buenos dias"
    print("parametro por defecto: ",parametro);


def funcionRecibiendoLista(lista):
    for x in lista:
        print("contenido lista: ",str(x));


def funcionRetornarValor(numero):
    resultado = 5 + numero;
    return resultado;




        
        
    


#invocacion de funciones
print("***UNA SIMPLE SUMA***");
suma();
print("\n***OBTENIENDO TIPO DE DATO DE UNA VARIABLE***");
obtenerTipoDato();
print("\n***ASIGNANDO TIPOS DE DATOS***");
especificacionTipoDato();
print("\n***REALIZANDO CONVERSIONES***");
conversiones();
print("\n***NUMERO ALEATORIO***");
numeroRandom();
print("\n***MANEJANDO VARIABLES GLOBALES***");
variablesGlobales();
print("python es: "+variableGlobal); #lo invoco aqui para que se modifique la variable con el metodo de arriba, puedes mover esta linea arriba de la funcion variablesGlobales para ver la diferencia
print("\n***MANIPULACION DE CADENAS CON DISTINTOS METODOS***");
caracteristicasTipoString();
print("\n***EVALUANDO SENTENCIAS***");
evaluarSentencias();
print("\n***USO DE OPERADORES***");
usarOperadores();
print("***USO DE LISTAS***");
usarListas();
print("***USO DE TUPLAS***");
usarTuplas();
print("***USO DE CONJUNTOS***");
usarSets();
print("***USO DE DICCIONARIOS***");
usarDiccionarios();
print("***USO DE CONDICIONAL IF***");
condicionalIf();
print("***USO DE CICLOS***");
ciclosForWhile();
print("***FUNCIONES CON PARAMETROS***");
funcionesConParametros("juanito");
funcionesConParametrosDesconocidos(" pedro"," juan"," pablo"," lupe");
funcionesConKeyboard(parametro1="hello",parametro2="hola");
funcionesConKeyboardDesconocido(primero="juan",segundo="rosa");
funcionConValorPorDefecto();
funcionConValorPorDefecto("hola");
milista = ["perro","gato","chivo"]
funcionRecibiendoLista(milista);
print(funcionRetornarValor(3));
# ¿ cuantos perros tienes ? ¿ cuales son sus caracterisiticas ?
class Perro:
    # el metodo siguiente es equivalente al constructor, el self (covencion, puede ser otro nombre) va como parametro inicial,
    # ya que gracias a este se puede acceder a las propiedades de la clase para manipularlas
      def __init__(self, raza, tamanio, origen):
        self.raza = raza;
        self.tamanio = tamanio;
        self.origen = origen;
      
      #__repr__  es un metodo especial el cual regresa un string en lugar de la direccion en memoria del objeto
      def __repr__(self):
        # el string que regresaremos es un diccionario que tiene los atributos del objeto
        # el metodo str nos devulve el objeto en en version string
        return str(self.__dict__);


# creando un objeto
Athena = Perro("doberman","grande","alemania")
Canela = Perro("doberman","grande","alemania")
Yara = Perro("doberman","grande","alemania")
Princesa = Perro("Schnauzer","pequeño","alemania")


arregloPerros = [Athena,Canela,Yara,Princesa]
#print(arregloPerros[0]);

for perro in arregloPerros:
  print(perro)
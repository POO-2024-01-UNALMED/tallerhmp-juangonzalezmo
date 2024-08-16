from persona import Persona
from deportista import Deportista

class Futbolista(Persona, Deportista):

    listaFutbolistas = []

    def __init__(self,nombre,edad,altura,sexo,añosPracticando,golesMarcados,tarjetasRojas,piernaHabil):

        Persona.__init__(self,nombre,edad,altura,sexo)
        Deportista.__init__(self,añosPracticando)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil

        Futbolista.listaFutbolistas.append(self)

    def getGolesMarcados(self):
        return self._golesMarcados

    def getTarjetasRojas(self):
        return self._tarjetasRojas

    def getPiernaHabil(self):
        return self._piernaHabil

    def setGolesMarcados(self, golesMarcados):
        self._golesMarcados = golesMarcados

    def setTarjetasRojas(self, tarjetasRojas):
        self._tarjetasRojas = tarjetasRojas

    def setPiernaHabil(self, piernaHabil):
        self._piernaHabil = piernaHabil

    def getNombre(self):
        return self._nombre
    
    def getEdad(self):
        return self._edad
    
    def getAltura(self):
        return self._altura
    
    def getSexo(self):
        return self._sexo

    def setNombre(self, nombre):
        self._nombre = nombre

    def setEdad(self,edad):
        self._edad = edad

    def setAltura(self, altura):
        self._altura = altura
    
    def setSexo(self, sexo):
        self._sexo = sexo

    def getDeporte(self):
        return self._deporte
    
    def getAñosPracticando(self):
        return self._añosPracticando
    
    def setDeporte(self, deporte):
        self._deporte = deporte

    def setAñosPracticando(self, añosPracticando):
        self._añosPracticando = añosPracticando
    
    def __str__(self):
        return "Mi nombre es "+ self._nombre + " soy profesional en el deporte "+self._deporte+ " Tengo " +str(self._edad) +" años de edad y llevo "+ str(self._añosPracticando) +" años en el deporte"
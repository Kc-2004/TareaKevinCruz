class Rutina:
    pass
    def __init__(self, nombre, actividad) :
        self.nombre = nombre
        self.actividad = actividad
  

rutinauno = Rutina("Kevin Cruz","Trabaja")
rutinados = Rutina("Kevin Cruz", "Estudia")

class Estudiar(Rutina):

    pass
    def RealizarRutina():
        return "{} {} por las mañanas de Lunes a Jueves".format(rutinauno.nombre, rutinauno.actividad)

class Trabajar(Rutina):

    pass
    def RealizarRutina():
        return " {} {} desde las 3 p.m hasta las 11.30 p.m de Lunes a Sabado".format(rutinados.nombre, rutinados.actividad)
    
tareaUno= Estudiar
tareaDos= Trabajar
print(tareaUno.RealizarRutina())
print(tareaDos.RealizarRutina())
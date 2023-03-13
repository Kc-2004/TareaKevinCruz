class Mundial:
    pass
    def __init__(self, equipo1, equipo2):
     self.equipo1 = equipo1
     self.equipo2 = equipo2

primerpartido= Mundial("Brasil","Mexico")
segundopartido= Mundial("Francia","Portugal")

class PartidoUno(Mundial):
   pass

   def Resultados(resultado):
      return "{} quedo {} contra {}".format(primerpartido.equipo1,resultado,primerpartido.equipo2)

class PartidoDos(Mundial):
   pass
   
   def Resultados(resultado):
      return "{} quedo {} contra {}".format(segundopartido.equipo1, resultado , segundopartido.equipo2)

ResultadoUno=PartidoUno
ResultadoDos=PartidoDos
print(ResultadoUno.Resultados("3 a 1"))
print(ResultadoDos.Resultados("3 a 3"))
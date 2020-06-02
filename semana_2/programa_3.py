class Avion:
  def __init__(self):
    print("rapidez")
    print("tamaño")
    print("color")
    print("cantidad_de_asientos")
    print("motor")
  def metodosAvion(self):
    print("viajar")
    print("carga")
'Subclase 1'
class Transporte(Avion):
  def __init__(self):
    print("carga")
    print("altura")
    print("resistencia")
    print("figura")
    print("modelo")
  def metodosTransporte(self):
    print("transportar_tropas")
    print("entrenamiento")

objeto_avion=Avion()
objeto_avion.metodosAvion()

objeto_transporte=Transporte()
objeto_transporte.metodosTransporte()
objeto_transporte=Avion()
objeto_transporte.metodosAvion()
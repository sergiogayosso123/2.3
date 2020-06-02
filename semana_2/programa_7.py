class Coche:
  def __init__(self):
    print("color")
    print("material")
    print("personas")
    print("resistencia")
    print("velocidad")
  def metodosCoche(self):
    print("transportarte")
    print("viajar")
'Subclase 1'
class Transporte(Coche):
  def __init__(self):
    print("diseño")
    print("motor")
    print("asientos")
    print("volante")
    print("placa")
  def metodosTransporte(self):
    print("pasear")
    print("comunicar")

objeto_coche=Coche()
objeto_coche.metodosCoche()

objeto_transporte=Transporte()
objeto_transporte.metodosTransporte()
objeto_transporte=Coche()
objeto_transporte.metodosCoche()

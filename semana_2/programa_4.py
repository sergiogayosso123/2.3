class Vacaciones:
  def __init__(self):
    print("clima")
    print("duracion")
    print("lugar")
    print("antiguedad")
    print("labor")
  def metodosVacaciones(self):
    print("distraerse")
    print("desestres")
'Subclase 1'
class Lugar(Vacaciones):
  def __init__(self):
    print("recursos")
    print("servicios")
    print("comodidad")
    print("pago")
    print("periodo")
  def metodosLugar(self):
    print("descansar")
    print("estar_con_familia")

objeto_vacaciones=Vacaciones()
objeto_vacaciones.metodosVacaciones()

objeto_lugar=Lugar()
objeto_lugar.metodosLugar()
objeto_lugar=Vacaciones()
objeto_lugar.metodosVacaciones()
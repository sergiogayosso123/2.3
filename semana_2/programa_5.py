class Serie_tv:
  def __init__(self):
    print("trama")
    print("exito")
    print("calidad")
    print("capitulos")
    print("a_quien_va_dirijido")
  def metodosSerie_tv(self):
    print("distraerse")
    print("conocer")
'Subclase 1'
class Programa(Serie_tv):
  def __init__(self):
    print("escenas")
    print("duracion")
    print("seguidores")
    print("diseño")
    print("periodo")
  def metodosPrograma(self):
    print("informar")
    print("comunicar")

objeto_serie_tv=Serie_tv()
objeto_serie_tv.metodosSerie_tv()

objeto_programa=Programa()
objeto_programa.metodosPrograma()
objeto_programa=Serie_tv()
objeto_programa.metodosSerie_tv()

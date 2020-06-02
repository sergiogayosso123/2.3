class Futbolista:
  def __init__(self):
    print("fuerte")
    print("rapida")
    print("eficaz")
    print("sencilla")
    print("amable")
  def metodosFutbolista(self):
    print("hacer_deporte")
    print("enseñar")
'Subclase 1'
class Juego(Futbolista):
  def __init__(self):
    print("carismatica")
    print("tolerante")
    print("habil")
    print("buena_vision")
    print("dominio_de_balon")
  def metodosJuego(self):
    print("practicar")
    print("realizar_ejercicios")

objeto_futbolista=Futbolista()
objeto_futbolista.metodosFutbolista()

objeto_juego=Juego()
objeto_juego.metodosJuego()
objeto_juego=Futbolista()
objeto_juego.metodosFutbolista()
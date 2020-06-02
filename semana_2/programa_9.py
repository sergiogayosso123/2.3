class Cajero:
  def __init__(self):
    print("validacion")
    print("codigo")
    print("monitor")
    print("scanner")
    print("pantalla")
  def metodosCajero(self):
    print("depositos")
    print("datos")
'Subclase 1'
class Aparato(Cajero):
  def __init__(self):
    print("figura")
    print("diseño")
    print("numeros")
    print("digitos")
    print("signos")
  def metodosAparato(self):
    print("movimientos")
    print("retiros")

objeto_cajero=Cajero()
objeto_cajero.metodosCajero()

objeto_aparato=Aparato()
objeto_aparato.metodosAparato()
objeto_aparato=Cajero()
objeto_aparato.metodosCajero()
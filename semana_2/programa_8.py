class Calculadora:
  def __init__(self):
    print("tamaño")
    print("figura")
    print("material")
    print("botones")
    print("operaciones")
  def metodosCalculadora(self):
    print("cuentas")
    print("problemas")
'Subclase 1'
class Aparato(Calculadora):
  def __init__(self):
    print("fuente_de_energia")
    print("tipo_de_teclado")
    print("pantalla")
    print("digitos")
    print("signos")
  def metodosAparato(self):
    print("calculos")
    print("porcentajes")

objeto_calculadora=Calculadora()
objeto_calculadora.metodosCalculadora()

objeto_aparato=Aparato()
objeto_aparato.metodosAparato()
objeto_aparato=Calculadora()
objeto_aparato.metodosCalculadora()
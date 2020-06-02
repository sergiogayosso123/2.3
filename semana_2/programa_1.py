class Banco:
  def __init__(self):
    print("cajeros")
    print("ventanilla")
    print("oficinas")
    print("personal")
    print("puertas")
  def depositos(self):
    print("depositos")
  def transferencias(self):
    print("transferencia")
'Subclase 1'
class BancoComercial(Banco):
  def __init__(self):
    print("BANCO COMERCIAL")
    print("estabilidad")
    print("atencion_al_cliente")
    print("estratejias")
    print("horarios")
    print("juzteza")
  def metodosBancoComercial(self):
    print("consultas")
    print("reconocer_rostro")

objeto_banco=Banco()
objeto_banco.depositos()
objeto_banco.transferencias()

objeto_banco_comercial=BancoComercial()
objeto_banco_comercial.metodosBancoComercial()
objeto_banco_comercial.depositos()
objeto_banco_comercial.transferencias()
objeto_banco_comercial=Banco()

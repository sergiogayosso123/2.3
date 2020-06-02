class Classroom:
  def __init__(self):
    print("agilidad")
    print("organizacion")
    print("comunicacion")
    print("enfoque_academico")
    print("gratitud")
  def metodosClassroom(self):
    print("enviar_actividades")
    print("notificaciones")
'Subclase 1'
class Pagina(Classroom):
  def __init__(self):
    print("crear")
    print("revisar")
    print("codigos")
    print("seguro")
    print("herramientas")
  def metodosPagina(self):
    print("debates")
    print("agendar_actividades")

objeto_classroom=Classroom()
objeto_classroom.metodosClassroom()

objeto_pagina=Pagina()
objeto_pagina.metodosPagina()
objeto_pagina=Classroom()
objeto_aparato.metodosClassroom()
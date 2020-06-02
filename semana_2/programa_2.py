class Estudiante:
  def __init__(self):
    print("amable")
    print("responsable")
    print("tolerante")
    print("carisma")
    print("respeto")
  def metodosEstudiante(self):
    print("aprender")
    print("tener_metas")
'Subclase 1'
class Alumno(Estudiante):
  def __init__(self):
    print("puntual")
    print("sencillo")
    print("cumplido")
    print("participativo")
    print("creativo")
  def metodosAlumno(self):
    print("tener_una_educacion")
    print("resolver_problemas")

objeto_estudiante=Estudiante()
objeto_estudiante.metodosEstudiante()

objeto_alumno=Alumno()
objeto_alumno.metodosAlumno()
objeto_alumno=Estudiante()
objeto_alumno.metodosEstudiante()
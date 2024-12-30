from django.db import models

# Create your models here.


class Alumno(models.Model):
    """
    Modelo que representa a un alumno.

    Atributos:
        nombre (str): Nombre del alumno.
        edad (int): Edad del alumno.
        correo_electronico (str): Correo electrónico del alumno.
        direccion (str, opcional): Dirección del alumno. Puede ser nulo o estar en blanco.
        telefono (str, opcional): Teléfono del alumno. Puede ser nulo o estar en blanco.
        fecha_inscripcion (date): Fecha de inscripción del alumno. Se establece automáticamente al crear el registro.
        cedula (str): Cédula del alumno. No puede ser nulo.
        estado (bool): Estado del alumno. Por defecto es True.

    Métodos:
        __str__(): Devuelve una representación en cadena del alumno, que es su nombre.
    """
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    correo_electronico = models.EmailField()
    direccion = models.CharField(max_length=255, null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    cedula = models.CharField(max_length=20)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Responsable(models.Model):
    """
    Modelo que representa a un responsable de un alumno.

    Atributos:
        nombre (str): Nombre del responsable.
        telefono (str): Teléfono del responsable.
        correo_electronico (str): Correo electrónico del responsable.
        cedula (str): Cédula del responsable. No puede ser nulo.
        alumno (ForeignKey): Relación con el alumno correspondiente.
    
    Métodos:
        __str__(): Devuelve una representación en cadena del responsable, que es su nombre.
    """
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo_electronico = models.EmailField()
    cedula = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre
    
class ResponsableAlumno(models.Model):
    """
    Modelo intermedio para asociar un responsable con un alumno por un periodo de tiempo.

    Atributos:
        alumno (ForeignKey): Relación con el alumno correspondiente.
        responsable (ForeignKey): Relación con el responsable correspondiente.
        fecha_inicio (date, opcional): Fecha de inicio de la responsabilidad. Puede ser nulo.
        fecha_fin (date, opcional): Fecha de fin de la responsabilidad. Puede ser nulo.
        tipo_relacion (str): Tipo de relación entre el responsable y el alumno.
    """
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    responsable = models.ForeignKey(Responsable, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    TIPO_RELACION_CHOICES = [
        ('madre', 'Madre'),
        ('padre', 'Padre'),
        ('tutor', 'Tutor'),
        ('otro', 'Otro'),
    ]
    tipo_relacion = models.CharField(max_length=10, choices=TIPO_RELACION_CHOICES, default='madre')

    def __str__(self):
        return f"{self.responsable.nombre} - {self.alumno.nombre}"
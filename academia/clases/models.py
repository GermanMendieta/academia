from django.db import models

from alumnos.models import Alumno

# Create your models here.

class Profesora(models.Model):
    """
    Modelo que representa a una profesora en la academia.
    Atributos:
        nombre (CharField): Nombre de la profesora, con un máximo de 100 caracteres.
        especialidad (CharField): Especialidad de la profesora, con un máximo de 100 caracteres.
        correo_electronico (EmailField): Correo electrónico de la profesora, puede ser nulo o estar en blanco.
        telefono (CharField): Teléfono de la profesora, con un máximo de 15 caracteres, puede ser nulo o estar en blanco.
        fecha_contratacion (DateField): Fecha de contratación de la profesora.
    Métodos:
        __str__: Devuelve el nombre de la profesora.
    """
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    correo_electronico = models.EmailField(null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    fecha_contratacion = models.DateField()

    def __str__(self):
        return self.nombre


class Clase(models.Model):
    """
    Modelo que representa una clase en el sistema de academia.
    Atributos:
        nombre (CharField): El nombre de la clase, con una longitud máxima de 100 caracteres.
        profesora (ForeignKey): Una clave foránea al modelo Profesora, que representa a la profesora de la clase.
        alumnos (ManyToManyField): Una relación de muchos a muchos con el modelo Alumno, que representa a los alumnos inscritos en la clase.
        horario (TimeField): La hora a la que está programada la clase.
        duracion (DurationField): La duración de la clase.
        aula (CharField): El aula donde se lleva a cabo la clase, con una longitud máxima de 50 caracteres. Este campo es opcional (puede ser nulo o estar en blanco).
    Métodos:
        __str__(): Devuelve el nombre de la clase como su representación en cadena.
    """

    nombre = models.CharField(max_length=100)
    profesora = models.ForeignKey(Profesora, on_delete=models.CASCADE)
    alumnos = models.ManyToManyField(Alumno)
    horario = models.TimeField()
    duracion = models.DurationField()
    aula = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nombre


class ElementoAula(models.Model):
    """
    Modelo que representa un elemento dentro de un aula.
    Atributos:
        nombre (CharField): Nombre del elemento del aula, con un máximo de 100 caracteres.
        descripcion (TextField): Descripción opcional del elemento del aula.
        cantidad (IntegerField): Cantidad de este tipo de elemento en el aula.
        aula (ForeignKey): Relación con el modelo Clase, indicando a qué aula pertenece este elemento.
    Métodos:
        __str__: Retorna el nombre del elemento del aula.
    """
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    cantidad = models.IntegerField()
    aula = models.ForeignKey(
        Clase, on_delete=models.CASCADE, related_name='elementos')

    def __str__(self):
        return self.nombre


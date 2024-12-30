from django import forms
from .models import Alumno, Responsable, ResponsableAlumno


class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'cedula', 'edad', 'correo_electronico',
                  'direccion', 'telefono', 'estado']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'correo_electronico': forms.EmailInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class ResponsableForm(forms.ModelForm):
    class Meta:
        model = Responsable
        fields = ['nombre',  'cedula', 'telefono', 'correo_electronico']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'correo_electronico': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class ResponsableAlumnoForm(forms.ModelForm):
    class Meta:
        model = ResponsableAlumno
        fields = ['alumno', 'responsable',
                  'fecha_inicio', 'fecha_fin', 'tipo_relacion']
        widgets = {
            'alumno': forms.Select(attrs={'class': 'form-control'}),
            'responsable': forms.Select(attrs={'class': 'form-control'}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'tipo_relacion': forms.Select(attrs={'class': 'form-control'}),
        }

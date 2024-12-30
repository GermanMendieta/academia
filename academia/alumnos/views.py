import json
from django.shortcuts import render, redirect, get_object_or_404
from .models import Alumno, Responsable, ResponsableAlumno
from .forms import AlumnoForm, ResponsableAlumnoForm, ResponsableForm


def alumnos_view(request):
    if request.method == 'POST':
        form_alumnos = AlumnoForm(request.POST)
        if form_alumnos.is_valid():
            form_alumnos.save()
            return redirect('alumnos:alumnos_view')
        else:
            error_message = "There was an error with your submission. Please correct the errors below."
            context = get_context()
            context.update({'error_message': error_message})
            return render(request, 'alumnos_view.html', context)

    return render(request, 'alumnos_view.html', context=get_context())


def edit_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('alumnos:alumnos_view')
        else:
            error_message = "There was an error with your submission. Please correct the errors below."
            return render(request, 'alumnos_view.html', get_context() + {'error_message': error_message})


def delete_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    if request.method == 'POST':
        alumno.estado = False
        alumno.save()
        return redirect('alumnos:alumnos_view')


def selected_multiple_alumnos(request):
    if request.method == 'POST':
        ids = request.POST.getlist('ids')
        action = request.POST.get('actionType')

        if action == 'deactivate':
            Alumno.objects.filter(id__in=ids).update(estado=False)
        elif action == 'activate':
            Alumno.objects.filter(id__in=ids).update(estado=True)
        elif action == 'delete':
            Alumno.objects.filter(id__in=ids).delete()
        elif action == 'associate':
            return redirect('alumnos:associate_responsables')

        return redirect('alumnos:alumnos_view')


def add_responsable(request):
    context = get_context()
    context.update({
        'responsables_json': json.dumps(list(Responsable.objects.all().values())),
    })
    if request.method == 'POST':
        form = ResponsableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alumnos:add_responsable')
        else:
            error_message = "There was an error with your submission. Please correct the errors below."
            context.update({'error_message': error_message, })
        return render(request, 'add_responsable.html', context)
    return render(request, 'add_responsable.html', context=context)


def edit_responsable(request, id):
    responsable = get_object_or_404(Responsable, id=id)
    if request.method == 'POST':
        form = ResponsableForm(request.POST, instance=responsable)
        if form.is_valid():
            form.save()
            return redirect('alumnos:alumnos_view')
    else:
        form = ResponsableForm(instance=responsable)
    return render(request, 'edit_responsable.html', {'form': form})


def associate_responsables(request):
    if request.method == 'POST':
        alumnos_ids = request.POST.getlist('alumnos')
        responsables_ids = request.POST.getlist('responsables')
        for alumno_id in alumnos_ids:
            for responsable_id in responsables_ids:
                ResponsableAlumno.objects.create(
                    alumno_id=alumno_id,
                    responsable_id=responsable_id
                )
        return redirect('alumnos:associate_responsables')
    else:
        alumnos = Alumno.objects.all()
        responsables = Responsable.objects.all()
        relaciones = ResponsableAlumno.objects.select_related(
            'alumno', 'responsable').all()
    return render(request, 'associate_responsables.html', {'alumnos': alumnos, 'responsables': responsables, 'relaciones': relaciones})


def delete_responsable(request, id):
    responsable = get_object_or_404(Responsable, id=id)
    if request.method == 'POST':
        responsable.delete()
        return redirect('alumnos:add_responsable')


def get_context():
    alumnos = list(Alumno.objects.all().values())
    alumnos_json = json.dumps(alumnos)
    responsables = list(Responsable.objects.all().values())

    responsables_alumnos = ResponsableAlumno.objects.select_related(
        'alumno', 'responsable').all()

    form_alumnos = AlumnoForm()
    form_Responsables = ResponsableForm()
    form_ResponsablesAlumnos = ResponsableAlumnoForm()

    context = {
        'alumnos': alumnos,
        'alumnos_json': alumnos_json,
        'responsables': responsables,
        'relaciones': responsables_alumnos,
        'form': form_alumnos,
        'form_Responsables': form_Responsables,
        'form_ResponsablesAlumnos': form_ResponsablesAlumnos,
    }
    return context

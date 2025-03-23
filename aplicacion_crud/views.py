from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Citas
from datetime import datetime
from django.utils import timezone
from django.contrib import messages
from django.utils import timezone

# Create your views here.

def registrarse(request):
    if request.method == 'GET':
        return render(request, "registrarse.html")
    else:
        if request.POST['password1'] == request.POST['password2']:
            try :
                user = User.objects.create_user(username=request.POST["username"], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect(citas)
            except:
                return render(request, "registrarse.html",{
                    'error':'El usuario ya existe'
                })
        else:
            return render(request, "registrarse.html",{
                    'error':'Las contraseñas no coinciden'
                })

@login_required        
def citas(request):
    citas = Citas.objects.filter(estatus=1)
    return render(request, "citas.html",{
        'citas':citas
    })
    
@login_required        
def citas_canceladas(request):
    citas = Citas.objects.filter(estatus=0)
    return render(request, "citas_canceladas.html",{
        'citas':citas
    })

def cerrar_sesion(request):
    logout(request)
    return redirect('iniciar_sesion')

def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, "iniciar_sesion.html")
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        print(user)
        if user is None:
            return render(request, "iniciar_sesion.html",{
                'error':'Credenciales incorrectas'
            })
        else:
            login(request, user)
            return redirect(citas)

@login_required          
def crear_cita(request):
    if request.method == 'GET':
        return render(request, 'crear_cita.html')
    else:
        fecha_hora_str = request.POST.get('fecha_hora')
        fecha_hora_naive = timezone.datetime.fromisoformat(fecha_hora_str)
        fecha_convertida = timezone.make_aware(fecha_hora_naive)
        
        fecha_hora = request.POST['fecha_hora']
        paciente = request.POST['paciente']
        tiempo = request.POST['tiempo']
        medico = request.POST['medico']
        numero_cita = request.POST['numero_cita']
        
        bandera= False
        if fecha_convertida <= timezone.now():   
            error = 'La fecha y hora deben ser superiores a la fecha y hora actuales.'
            bandera= True
        elif len(paciente) < 5:
            error = 'El nombre del paciente es muy corto'
            bandera= True
        elif int(tiempo) > 60:
            error = 'El tiempo maximo de cita es de 60 miutos'
            bandera= True
        elif len(medico) < 5:
            error = 'El nombre del medico es muy corto'
            bandera= True
        
        if bandera == True:                        
            return render(request, 'crear_cita.html', {
                'fecha_hora': fecha_hora,
                'paciente': paciente,
                'tiempo': tiempo,
                'medico': medico,
                'numero_cita':numero_cita,
                'error': error
            })        
        try:
            cita = Citas.objects.create(fecha_hora=request.POST['fecha_hora'],
                                        paciente=request.POST['paciente'],
                                        tiempo=request.POST['tiempo'],
                                        medico=request.POST['medico'],
                                        cita=request.POST['numero_cita'],
                                        estatus=1
                                        )
        except:
            return redirect(citas,{
                'error': 'Error al guardar los datos'
            })
            
        return redirect(citas)

@login_required() 
def cita(request, id):
    cita = Citas.objects.get(pk=id)
    fecha_hora_formateada = cita.fecha_hora.strftime('%Y-%m-%dT%H:%M')
    return render(request, 'cita.html',{
        'fecha_hora_formateada':fecha_hora_formateada,
        'cita':cita,
    })
    
@login_required
def editar_cita(request, id):
    cita = Citas.objects.get(pk=id)
    if request.method == 'GET':
        fecha_hora_formateada = cita.fecha_hora.strftime('%Y-%m-%dT%H:%M')
        paciente = cita.paciente
        tiempo = cita.tiempo
        medico = cita.medico
        numero_cita = cita.cita
        
        return render(request, 'editar_cita.html',{
            'fecha_hora':fecha_hora_formateada,
            'paciente':paciente,
            'tiempo':tiempo,
            'medico':medico,
            'numero_cita':numero_cita,
            'cita':cita,
        })
    else:   
        fecha_hora_str = request.POST.get('fecha_hora')
        fecha_hora_naive = timezone.datetime.fromisoformat(fecha_hora_str)
        fecha_convertida = timezone.make_aware(fecha_hora_naive)
        
        fecha_hora = request.POST['fecha_hora']
        paciente = request.POST['paciente']
        tiempo = request.POST['tiempo']
        medico = request.POST['medico']
        numero_cita = request.POST['numero_cita']
            
        bandera= False
        if fecha_convertida <= timezone.now():   
            error = 'La fecha y hora deben ser superiores a la fecha y hora actuales.'
            bandera= True
        elif len(paciente) < 5:
            error = 'El nombre del paciente es muy corto'
            bandera= True
        elif int(tiempo) > 60:
            error = 'El tiempo maximo de cita es de 60 miutos'
            bandera= True
        elif len(medico) < 5:
            error = 'El nombre del medico es muy corto'
            bandera= True
            
        if bandera == True:                        
            return render(request, 'editar_cita.html', {
                'fecha_hora': fecha_hora,
                'paciente': paciente,
                'tiempo': tiempo,
                'medico': medico,
                'numero_cita':numero_cita,
                'cita':cita,
                'error': error
            }) 
            
        fecha_hora_str = request.POST.get('fecha_hora')
        fecha_hora = datetime.fromisoformat(fecha_hora_str)
        
        cita = Citas.objects.get(pk=id)
        cita.fecha_hora = fecha_hora
        cita.tiempo=tiempo
        cita.medico=medico
        cita.save()
        
        return redirect(citas)

@login_required
def eliminar_cita(request, id):
    cita = Citas.objects.get(pk=id)
    cita.estatus = 0
    cita.save()
    
    return redirect(citas)

@login_required
def activar_cita(request, id):
    cita = Citas.objects.get(pk=id)
    cita.estatus = 1
    cita.save()
    
    return redirect(citas_canceladas)
        
        
        
    
    

        
        
    
    

"""
Codigo en Vista para el Login
"""
#from rest_framework.views import APIView
from django.shortcuts import render, redirect
#from .models import Registros
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
# from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Respuestaschatbot

# Create your views here.
@login_required(login_url='login')

def HomePage(request):
    """a"""
    return render (request, 'inicio.html')
    
def SignupPage(request):
    """b"""
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        
        if pass1!=pass2:
            messages.error(request, "La Contraseña no coincide")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            contact(request)
            return redirect('login')
        
    return render (request,'registro.html')

def LoginPage(request):
    """c"""
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        # print(username,pass1)
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            messages.success(request, "Usuario registrado exitosamente")
            return redirect('home')
        else:
            messages.error(request, "El Usuario o Contraseña son Incorrectos")
    return render (request, 'index.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def contact(request):
    if request.method == "POST":
        username=request.POST['username']
        email=request.POST['email']
        #subject=request.POST['subject']
        #message=request.POST['message']
        
        template = render_to_string('email_template.html', {
            'name': username,
            'email': email,
            #'message': message
        })
        
        email = EmailMessage(
            subject='Confirmacion de registro',
            body=template,
            from_email=settings.EMAIL_HOST_USER,
            to=[email]
         )
        
        email.fail_silenty = False
        email.send()
        messages.success(request, "Registro exitoso se ha enviado un mensaje a tu correo")
        return redirect('login')
    
#graficas

def grafica(request):
    registros = Respuestaschatbot.objects.all()
    return {'registros': registros}

def consulta1(request):
    # Realiza una consulta que cuente las filas con 'SI' en la columna pregunta1
    count = Respuestaschatbot.objects.filter(pregunta1="si").count()
    return {'count_si': count}

def consulta2(request):
    # Realiza una consulta que cuente las filas con 'NO' en la columna pregunta1
    count2 = Respuestaschatbot.objects.filter(pregunta1="no").count()
    return {'count_no': count2}



def Enc(request):
    
    grafica_data = grafica(request)
    tuvista_data = consulta1(request)
    tuvista_data2 = consulta2(request)
    
    # Combina los contextos de ambas vistas en un solo diccionario
    context = {**grafica_data, **tuvista_data, **tuvista_data2}
    return render (request, 'encu.html',context)
import datetime
import json
from urllib import request
from django.forms import ValidationError
from django.shortcuts import redirect, render
from rest_framework.views import APIView
from django.utils.crypto import get_random_string
from api.models import registro_cliente
from api.models import tinaco
from django.core.mail import send_mail
from django.contrib import messages
from datetime import datetime
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.
from django.middleware.csrf import get_token
from django.http import JsonResponse
import pyrebase 

config = {
    "apiKey": "AIzaSyD_81il9tAwbSOx3Rg4b-aC-xOdxMPK9m4",
    "authDomain": "apitinacos.firebaseapp.com",
    "databaseURL": "https://apitinacos-default-rtdb.firebaseio.com",
    "projectId": "apitinacos",
    "storageBucket": "apitinacos.appspot.com",
    "messagingSenderId": "950663012062",
    "appId": "1:950663012062:web:ff0ca609ee54cf2af22c4f",
    "measurementId": "G-PBESQLCYW6"
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

def get_csrf_token(request):
    token = get_token(request)
    response_data = {'csrf_token': token}
    
    # Convierte el diccionario en una cadena JSON
    json_data = json.dumps(response_data)
    
    # Devuelve la respuesta JSON
    return JsonResponse(json_data, safe=False, json_dumps_params={'ensure_ascii': False})



class Home(APIView):
    template_name="index.html"
    def get(self, request):
        return render(request, self.template_name)
    
class Login(APIView):
    template_name="login.html"
    def get(self, request):
        return render(request, self.template_name)
    
class SignIn(APIView):
    template_name="signup.html"
    def get(self, request):
        return render(request, self.template_name)
    
# def formulario_verificacion(request):
#     if request.method == 'POST':
#         nombre = request.POST['nombreForm']
#         paterno = request.POST['aPaternoForm']
#         materno = request.POST['aMaternoForm']
#         correoF = request.POST['CorreoForm'] 
#         passw = request.POST['PswdForm'] 
#         #genero = request.POST['gender']
#         codigoTi = request.POST['res_code']
#         if 'gender' in request.POST:
#                 genero = request.POST['gender']
#         else:
#             genero = None  # O asigna un valor por defecto si es apropiado en tu caso

#         try:
#             if not nombre or not paterno or not materno or not correoF or not passw or not genero or not codigoTi:
#                 messages.error(request, 'Verifica los campos, todos son obligatorios!')
#                 return render(request, 'signup.html')

#             # Verificar si el correo ya existe en la base de datos
#             if registro_cliente.objects.filter(nombre=correoF).exists():
#                 messages.error(request, 'Este usuario ya existe!')
#                 return render(request, 'signup.html')
#             if not tinaco.objects.filter(idTinaco=codigoTi).exists():
#                 messages.error(request, 'Este tinaco no existe, verifica la existencia!')
#                 return render(request, 'signup.html')
            

#             # Guardar el usuario en la base de datos
#             usuario = registro_cliente(nombre=nombre, aPaterno = paterno, aMaterno = materno,
#                                        correo = correoF, pswd_cliente = passw, genero = genero, 
#                                          codigo = codigoTi )
#             usuario.full_clean()  # Esto verifica las restricciones del modelo
#             usuario.save()

#             # Enviar correo de verificación
#             subject = 'Datos de usuario enviados correctamente!'
#             message = f'¡Gracias por registrarte en nuestro sitio! Los datos de tu cuenta son Nombre de usuario {correoF} y tu contraseña es {passw}{get_random_string()}'
#             from_email = 'marco.vallejo2000@gmail.com'  # Debe ser una dirección de correo configurada en tu servidor de correo

#             send_mail(subject, message, from_email, [correoF])

#             messages.success(request, 'Usuario registrado. Por favor, verifica tu correo.')
#             token = get_token(request)
#             return JsonResponse({'csrf_token': token}) 
#             return render(request, 'signup.html')

#         except ValidationError as e:
#             messages.error(request, str(e))
#             return render(request, 'signup.html')
        
#         except MultiValueDictKeyError:
#             messages.error(request, 'Error multiValor!')
#             return render(request, 'signup.html')
#     else:
#         return render(request, 'signup.html')
    
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Utiliza get() para evitar KeyError
        password = request.POST.get('password')

        try:
            if email == ('admin@gmail.com'):
                return redirect('dashboard')  # Redirige a una vista llamada 'index'
            user = registro_cliente.objects.get(name=email, passw=password)
            request.session['name'] = user.name
            return redirect('index1')  # Redirige a una vista llamada 'index'
        except registro_cliente.DoesNotExist:
            messages.error(request, '')
        except registro_cliente.MultipleObjectsReturned:
            messages.error(request, 'No se puede acceder')
        
    return render(request,'SIGN UP & SIGN IN PAGE.html')

# views.py

from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def formulario_verificacion(request):
    if request.method == 'POST':
        # Configuración de Firebase
        firebase_config = {
           "apiKey": "AIzaSyD_81il9tAwbSOx3Rg4b-aC-xOdxMPK9m4",
            "authDomain": "apitinacos.firebaseapp.com",
            "databaseURL": "https://apitinacos-default-rtdb.firebaseio.com",
            "projectId": "apitinacos",
            "storageBucket": "apitinacos.appspot.com",
            "messagingSenderId": "950663012062",
            "appId": "1:950663012062:web:ff0ca609ee54cf2af22c4f",
            "measurementId": "G-PBESQLCYW6"
        }

        firebase = pyrebase.initialize_app(firebase_config)
        db = firebase.database()

        # Obtener datos del formulario
        nombre = request.POST['nombreForm']
        paterno = request.POST['aPaternoForm']
        materno = request.POST['aMaternoForm']
        correoF = request.POST['CorreoForm']
        passw = request.POST['PswdForm']
        codigoTi = request.POST['res_code']

        genero = request.POST.get('gender')  # Utiliza get para manejar campos no presentes

        try:
            if not nombre or not paterno or not materno or not correoF or not passw or not genero or not codigoTi:
                messages.error(request, 'Verifica los campos, todos son obligatorios!')
                return render(request, 'signup.html')

            # # Verificar si el correo ya existe en la base de datos
            # if registro_cliente.objects.filter(nombre=correoF).exists():
            #     messages.error(request, 'Este usuario ya existe!')
            #     return render(request, 'signup.html')

            # if not tinaco.objects.filter(idTinaco=codigoTi).exists():
            #     messages.error(request, 'Este tinaco no existe, verifica la existencia!')
            #     return render(request, 'signup.html')

            # Guardar el usuario en Firebase
            data = {
                "nombre": nombre,
                "aPaterno": paterno,
                "aMaterno": materno,
                "correo": correoF,
                "psw_cliente": passw,
                "genero": genero,
                "codigo_tinaco": codigoTi,
            }

            db.child("cliente").push(data)

            # Enviar correo de verificación
            # (Aquí va el código para enviar el correo)

            messages.success(request, 'Usuario registrado. Por favor, verifica tu correo.')
            return render(request, 'signup.html')

        except ValidationError as e:
            messages.error(request, str(e))
            return render(request, 'signup.html')

        except MultiValueDictKeyError:
            messages.error(request, 'Error multiValor!')
            return render(request, 'signup.html')

    else:
        return render(request, 'signup.html')

from datetime import datetime

from django import forms
from django.forms import CharField, ModelForm, TextInput

from core.kardex.models import Armas, Kardex, Persona, Cursos, Puestos, Vehiculos, Bienes

# from image_uploader_widget.widgets import ImageUploaderWidget

# %TEMP%
from crum import get_current_request
from django.contrib.auth import update_session_auth_hash

class PersonaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True
        
    class Meta:
        model = Persona
        fields = '__all__'

        widgets = {
            'clavesp': forms.TextInput(attrs={'placeholder': 'Ingrese Clave de Servidor Público'}),
            'rfc': forms.TextInput(attrs={'placeholder': 'Ingrese su RFC'}),
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese un Nombre'}),
            'apaterno': forms.TextInput(attrs={'placeholder': 'Ingrese Apellido Paterno'}),
            'amaterno': forms.TextInput(attrs={'placeholder': 'Ingrese Apellido Materno'}),
            
            'fecha_alta': forms.TextInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control  datetimepicker',
                    'min': '1922-01-01',
                    'max': '2024-01-01',
                }
            ),
            'fecha_nacimiento': forms.TextInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control  datetimepicker',
                    'min': '1960-01-01',
                    'max': '2003-01-01',
                }
            ),
            # 'fecha_baja': forms.TextInput(
            #     attrs={
            #         'type': 'date',
            #         'class': 'form-control  datetimepicker',
            #     }
            # ), 
           'num_plaza': forms.TextInput(attrs={'placeholder': 'Ingrese su Número de Plaza'}),
           'cuip': forms.TextInput(attrs={'placeholder': 'Ingrese su CUIP'}),
           'curp': forms.TextInput(attrs={'placeholder': 'Ingrese su CURP', 'maxlength':'18'}),
           'calle': forms.TextInput(attrs={'placeholder': 'Ingrese su Calle'}),
           'exterior': forms.TextInput(attrs={'placeholder': 'Número Exterior'}),
           'interior': forms.TextInput(attrs={'placeholder': 'Interior'}),
           'cp': forms.TextInput(attrs={'placeholder': 'Ingrese su Código Postal'}),
           'municipio': forms.Select(attrs={
                'class': 'custom-select select2',
                # 'style': 'width: 100%'
            }),
            'user': forms.HiddenInput(
                attrs={
                    'required': False
                }
            ),    
        #     'colonia': forms.Select(attrs={
        #         'class': 'custom-select select2',
        #         # 'style': 'width: 100%'
        #     }),

            #'foto': ImageUploaderWidget(),

        }
        exclude = ['is_change_password', 'is_staff', 'user_permissions', 'date_joined',
                   'last_login', 'is_superuser', 'token']

    def update_session(self, user):
        request = get_current_request()
        if user == request.user:
            update_session_auth_hash(request, user)

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                u = form.save(commit=False)
                u.save()
                self.update_session(u)
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class CursoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True
    
    class Meta:
        model = Cursos
        
        fields = '__all__'
        
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre del Curso'}),
            'persona': forms.Select(attrs={
                'class': 'custom-select select2',
                # 'style': 'width: 100%'
            }),
        }

        exclude = ['is_change_password', 'is_staff', 'user_permissions', 'date_joined',
                   'last_login', 'is_superuser', 'token']

    def update_session(self, user):
        request = get_current_request()
        if user == request.user:
            update_session_auth_hash(request, user)

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                u = form.save(commit=False)
                u.save()
                self.update_session(u)
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class VehiculoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['matricula'].widget.attrs['autofocus'] = True
    
    class Meta:
        model = Vehiculos
        fields = '__all__'
        widgets = {
            'matricula': forms.TextInput(attrs={'placeholder': 'Agrega Matrícula'}),
            'persona': forms.Select(attrs={
                'class': 'custom-select select2',
                # 'style': 'width: 100%'
            }),
        }
        exclude = ['is_change_password', 'is_staff', 'user_permissions', 'date_joined',
                   'last_login', 'is_superuser', 'token']

    def update_session(self, user):
        request = get_current_request()
        if user == request.user:
            update_session_auth_hash(request, user)

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                u = form.save(commit=False)
                u.save()
                self.update_session(u)
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class ArmaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['matricula'].widget.attrs['autofocus'] = True
    
    class Meta:
        model = Armas
        fields = '__all__'
        widgets = {
            'matricula': forms.TextInput(attrs={'placeholder': 'Ingresa Número de Matrícula'}),
            'persona': forms.Select(attrs={
                'class': 'custom-select select2',
                # 'style': 'width: 100%'
            }),
        }
        exclude = ['is_change_password', 'is_staff', 'user_permissions', 'date_joined',
                   'last_login', 'is_superuser', 'token']

    def update_session(self, user):
        request = get_current_request()
        if user == request.user:
            update_session_auth_hash(request, user)

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                u = form.save(commit=False)
                u.save()
                self.update_session(u)
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class KardexForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Kardex
        fields = '__all__'
        widgets = {
            'curso': forms.Select(attrs={
                'class': 'custom-select select2',
                # 'style': 'width: 100%'
            }),
            'fecha_actual': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                    'autocomplete': 'off',
                    'class': 'form-control datetimepicker-input',
                    'id': 'fecha_actual',
                    'data-target': '#fecha_actual',
                    'data-toggle': 'datetimepicker'
                }
            ),
            
        }

class PuestoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True
    
    class Meta:
        model = Puestos
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre del Puesto'}),
        }
        exclude = ['is_change_password', 'is_staff', 'user_permissions', 'date_joined',
                   'last_login', 'is_superuser', 'token']

    def update_session(self, user):
        request = get_current_request()
        if user == request.user:
            update_session_auth_hash(request, user)

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                u = form.save(commit=False)
                u.save()
                self.update_session(u)
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class BienesForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categoria'].widget.attrs['autofocus'] = True
    
    class Meta:
        model = Bienes
        fields = '__all__'
        widgets = {
            'descripcion': forms.TextInput(attrs={'placeholder': 'Agrega Descripción', 'rows': '2'}),
            'resguardo': forms.TextInput(attrs={'placeholder': 'Resguardo', 'rows': '2'}),
            'resguardatario': forms.Select(attrs={
                'class': 'custom-select select2',
                # 'style': 'width: 100%'
            }),
            'user': forms.HiddenInput(
                attrs={
                    'required': False
                }
            ),  
        }
        exclude = ['is_change_password', 'is_staff', 'user_permissions', 'date_joined',
                   'last_login', 'is_superuser', 'token']

    def update_session(self, user):
        request = get_current_request()
        if user == request.user:
            update_session_auth_hash(request, user)

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                u = form.save(commit=False)
                u.save()
                self.update_session(u)
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
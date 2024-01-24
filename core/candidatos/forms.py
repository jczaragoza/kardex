from datetime import datetime

from django import forms
from django.forms import CharField, ModelForm, TextInput

from core.candidatos.models import Partido, Candidato

# %TEMP%
from crum import get_current_request
from django.contrib.auth import update_session_auth_hash


class CandidatoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True
        
    class Meta:
        model = Candidato
        fields = '__all__'

        partido = forms.CharField(required=True)

        widgets = {
            
            'rfc': forms.TextInput(attrs={'placeholder': 'Ingrese su RFC', 'maxlength':'13'}),
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese un Nombre'}),
            'apaterno': forms.TextInput(attrs={'placeholder': 'Ingrese Apellido Paterno'}),
            'amaterno': forms.TextInput(attrs={'placeholder': 'Ingrese Apellido Materno'}),
            'vinculos_delincuencia':forms.Textarea(attrs={'rows': 2}),
            'vinculos_politicos':forms.Textarea(attrs={'rows': 2}),
            'vehiculo':forms.Textarea(attrs={'rows': 2}),
            'cargos_ocupados':forms.Textarea(attrs={'rows': 2}),
            'experiencia_laboral':forms.Textarea(attrs={'rows': 2}),
            'comisiones':forms.Textarea(attrs={'rows': 2}),
            'temas_atencion':forms.Textarea(attrs={'rows': 2}),
            'amenazas':forms.Textarea(attrs={'rows': 2}),
            'fecha_nacimiento': forms.TextInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control  datetimepicker',
                    'min': '1940-01-01',
                    'max': '2003-01-01',
                }
            ),
            'curp': forms.TextInput(attrs={'placeholder': 'Ingrese su CURP', 'maxlength':'18'}),
            'direccion': forms.TextInput(attrs={'placeholder': 'Ingrese una dirección'}),
            # Agregar un botón con un icono de suma al lado del campo 'direccion'
            'direccion_button': forms.TextInput(attrs={'type': 'button', 'value': '+', 'class': 'icon-button'}),
            'user': forms.HiddenInput(
                attrs={
                    'required': False
                }
            ),    

        }
        exclude = ['is_change_password', 'is_staff', 'user_permissions', 'date_joined', 'last_login', 'is_superuser', 'token']
    
    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data['fecha_nacimiento']

        # Asegurarse de que el año tenga solo 4 dígitos
        if fecha_nacimiento.year > 9999:
            raise forms.ValidationError("El año no puede tener más de 4 dígitos.")
        
        return fecha_nacimiento

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
    
class CapturaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True
        
    class Meta:
        model = Candidato
        fields = '__all__'

        widgets = {
            
            'rfc': forms.TextInput(attrs={'placeholder': 'Ingrese su RFC', 'maxlength':'13'}),
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese un Nombre'}),
            'apaterno': forms.TextInput(attrs={'placeholder': 'Ingrese Apellido Paterno'}),
            'amaterno': forms.TextInput(attrs={'placeholder': 'Ingrese Apellido Materno'}),
            'vinculos_delincuencia':forms.Textarea(attrs={'rows': 2}),
            'vinculos_politicos':forms.Textarea(attrs={'rows': 2}),
            'vehiculo':forms.Textarea(attrs={'rows': 2}),
            'cargos_ocupados':forms.Textarea(attrs={'rows': 2}),
            'experiencia_laboral':forms.Textarea(attrs={'rows': 2}),
            'comisiones':forms.Textarea(attrs={'rows': 2}),
            'temas_atencion':forms.Textarea(attrs={'rows': 2}),
            'amenazas':forms.Textarea(attrs={'rows': 2}),
            'fecha_nacimiento': forms.TextInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control  datetimepicker',
                    'min': '1940-01-01',
                    'max': '2003-01-01',
                }
            ),
           'curp': forms.TextInput(attrs={'placeholder': 'Ingrese su CURP', 'maxlength':'18'}),
           'direccion': forms.Textarea(attrs={'rows': 2}),
           'user': forms.HiddenInput(
                attrs={
                    'required': False
                }
            ),    

        }
        exclude = ['is_change_password', 'is_staff', 'user_permissions', 'date_joined', 'last_login', 'is_superuser', 'token', 'is_active']
    
    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data['fecha_nacimiento']

        # Asegurarse de que el año tenga solo 4 dígitos
        if fecha_nacimiento.year > 9999:
            raise forms.ValidationError("El año no puede tener más de 4 dígitos.")
        
        return fecha_nacimiento

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

class PartidoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True
    
    class Meta:
        model = Partido
        
        fields = '__all__'
        
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre del Partido'}),
            
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

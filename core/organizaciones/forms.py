from datetime import datetime

from django import forms
from django.forms import CharField, ModelForm, TextInput

from core.organizaciones.models import Organizacion, Evento, Detalle, FichaCurricular

# %TEMP%
from crum import get_current_request
from django.contrib.auth import update_session_auth_hash


class OrganizacionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True
        
    class Meta:
        model = Organizacion
        fields = '__all__'

        registro = forms.CharField(required=False)

        widgets = {
            
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese nombre del colectivo'}),
            'inicio_actividades': forms.TextInput(attrs={'placeholder': 'Descripción de antecedentes de la organización'}),
            'registro': forms.TextInput(attrs={'placeholder': 'Registro Oficial del colectivo'}),
            'objetivo':forms.Textarea(attrs={'rows': 2}),
            'dirigentes': forms.TextInput(attrs={'placeholder': 'Ingrese nombres de dirigentes'}),
            'situacion_actual': forms.Textarea(attrs={'rows': 2}),
            'cargo': forms.TextInput(attrs={'placeholder': 'Ingrese cargo del dirigente'}),
            'direccion':forms.Textarea(attrs={'rows': 2}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Ingrese número de teléfono'}),
            'correo': forms.TextInput(attrs={'placeholder': 'Ingrese Correo'}),
            'facebook': forms.TextInput(attrs={'placeholder': 'Ingrese facebook'}),
            'instagram': forms.TextInput(attrs={'placeholder': 'Ingrese Instagram'}),
            'twitter': forms.TextInput(attrs={'placeholder': 'Ingrese Twitter'}),
            'influencia': forms.TextInput(attrs={'placeholder': 'Zona de influencia'}),
            'puntos_reunion':forms.Textarea(attrs={'rows': 2}),
            'principales_actividades':forms.Textarea(attrs={'rows': 2}),
            'modus_operandi':forms.Textarea(attrs={'rows': 2}),
            'vinculos_os':forms.Textarea(attrs={'rows': 2}),
            'vinculos_op':forms.Textarea(attrs={'rows': 2}),
            'vinculos_pp':forms.Textarea(attrs={'rows': 2}),
            'vinculos_au':forms.Textarea(attrs={'rows': 2}),
            'vinculos_de':forms.Textarea(attrs={'rows': 2}),
            'ingresos_fuente': forms.TextInput(attrs={'placeholder': 'Fuente de Ingresos'}),
            'inmuebles':forms.Textarea(attrs={'rows': 2}),
            'vehiculos':forms.Textarea(attrs={'rows': 2}),
            'cuentas_bancarias':forms.Textarea(attrs={'rows': 2}),
            'inversiones':forms.Textarea(attrs={'rows': 2}),
            'negocios':forms.Textarea(attrs={'rows': 2}),
            'demandas': forms.TextInput(attrs={'placeholder': 'Demandas del colectivo'}),
            'deudas':forms.Textarea(attrs={'rows': 2}),
            'medidas_presion':forms.Textarea(attrs={'rows': 2}),
            'grupos_choque':forms.Textarea(attrs={'rows': 2}),
            'uso_armas':forms.Textarea(attrs={'rows': 2}),
            'conflictos_organizaciones':forms.Textarea(attrs={'rows': 2}),
            'conflictos_legales':forms.Textarea(attrs={'rows': 2}),
            'grupos_disidentes':forms.Textarea(attrs={'rows': 2}),
            'perfil':forms.Textarea(attrs={'rows': 2}), 
            'capacidad_convocatoria':forms.Textarea(attrs={'rows': 2}), 
            'observaciones':forms.Textarea(attrs={'rows': 2}), 
            'fecha_creacion': forms.TextInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control  datetimepicker',
                    'min': '1940-01-01',
                    'max': '2025-31-12',
                }
            ),    
            'fecha_accion': forms.TextInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control  datetimepicker',
                    'min': '1940-01-01',
                    'max': '2025-31-12',
                }
            ),
            'estatus_ficha': forms.HiddenInput(
                attrs={
                    'required': False
                }
            ),  
            'observaciones_supervisor': forms.HiddenInput(
                attrs={
                    'required': False
                }
            ),            
            'actos_relevantes':forms.Textarea(attrs={'rows': 2}),
            'organos_difusion':forms.Textarea(attrs={'rows': 2}),
            'observaciones':forms.Textarea(attrs={'rows': 2}),
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

class EventoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True
        
    class Meta:
        model = Evento
        fields = '__all__'

        widgets = {
            
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese nombre del evento'}),
            'fecha_evento': forms.TextInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control  datetimepicker',
                    'min': '1940-01-01',
                    'max': '2025-31-12',
                }
            ),  
            'descripcion':forms.Textarea(attrs={'rows': 2}),
  
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

class FichaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True
        
    class Meta:
        model = FichaCurricular
        fields = '__all__'

        widgets = {
            
            'fecha_nacimiento': forms.TextInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control  datetimepicker',
                    'min': '1940-01-01',
                    'max': '2025-31-12',
                }
            ),
            'domicilio_particular':forms.Textarea(attrs={'rows': 2}),    
            'domicilio_laboral':forms.Textarea(attrs={'rows': 2}),    
            'padres':forms.Textarea(attrs={'rows': 2}),
            'conyuge':forms.Textarea(attrs={'rows': 2}),    
            'hijos':forms.Textarea(attrs={'rows': 2}),
            'otros':forms.Textarea(attrs={'rows': 2}),
            'vehiculos':forms.Textarea(attrs={'rows': 2}),    
            'domicilio_particular':forms.Textarea(attrs={'rows': 2}),  
            'inmuebles':forms.Textarea(attrs={'rows': 2}),      
            'cuentas_bancarias':forms.Textarea(attrs={'rows': 2}),      
            'inversiones':forms.Textarea(attrs={'rows': 2}),      
            'negocios':forms.Textarea(attrs={'rows': 2}),      
            'demandas':forms.Textarea(attrs={'rows': 2}),      
            'deudas':forms.Textarea(attrs={'rows': 2}),      
            'actividades_politicas':forms.Textarea(attrs={'rows': 2}),
            'puestos_eleccion_popular':forms.Textarea(attrs={'rows': 2}),
            'capacidad_convocatoria':forms.Textarea(attrs={'rows': 2}),
            'vulnerabilidades':forms.Textarea(attrs={'rows': 2}),
            'vinculos_orgs':forms.Textarea(attrs={'rows': 2}),      
            'vinculos_pol':forms.Textarea(attrs={'rows': 2}),
            'vinculos_ongs':forms.Textarea(attrs={'rows': 2}),    
            'vinculos_autoridades':forms.Textarea(attrs={'rows': 2}),    
            'vinculos_delictivos':forms.Textarea(attrs={'rows': 2}),    
            'imagen_publica':forms.Textarea(attrs={'rows': 2}),    
            'habilidades':forms.Textarea(attrs={'rows': 2}), 
            'perfil':forms.Textarea(attrs={'rows': 2}), 
            'observaciones':forms.Textarea(attrs={'rows': 2}),   
            'antecedentes_penales':forms.Textarea(attrs={'rows': 2}),   
            
            'conflictos_legales':forms.Textarea(attrs={'rows': 2}),   
            'organizacion': forms.Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),
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

class DetalleForm(ModelForm):
           
    class Meta:
        model = Detalle
        fields = '__all__'

        widgets = {
            'evento': forms.Select(
                attrs={
                    'class': 'custom-select select2',
                    'style': 'width: 80%'
                }
            ),
            'organizacion': forms.Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 80%'
                }
            ),
            'fichacurricular': forms.Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 80%'
                }
            ),
        }

class SupervisionOrganizacionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True
        
    class Meta:
        model = Organizacion
        fields = '__all__'

        registro = forms.CharField(required=False)

        widgets = {
            
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese nombre del colectivo'}),
            'inicio_actividades': forms.TextInput(attrs={'placeholder': 'Descripción de antecedentes de la organización'}),
            'registro': forms.TextInput(attrs={'placeholder': 'Registro Oficial del colectivo'}),
            'objetivo':forms.Textarea(attrs={'rows': 2}),
            'dirigentes': forms.TextInput(attrs={'placeholder': 'Ingrese nombres de dirigentes'}),
            'situacion_actual': forms.Textarea(attrs={'rows': 2}),
            'cargo': forms.TextInput(attrs={'placeholder': 'Ingrese cargo del dirigente'}),
            'direccion':forms.Textarea(attrs={'rows': 2}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Ingrese número de teléfono'}),
            'correo': forms.TextInput(attrs={'placeholder': 'Ingrese Correo'}),
            'facebook': forms.TextInput(attrs={'placeholder': 'Ingrese facebook'}),
            'instagram': forms.TextInput(attrs={'placeholder': 'Ingrese Instagram'}),
            'twitter': forms.TextInput(attrs={'placeholder': 'Ingrese Twitter'}),
            'influencia': forms.TextInput(attrs={'placeholder': 'Zona de influencia'}),
            'puntos_reunion':forms.Textarea(attrs={'rows': 2}),
            'principales_actividades':forms.Textarea(attrs={'rows': 2}),
            'modus_operandi':forms.Textarea(attrs={'rows': 2}),
            'vinculos_os':forms.Textarea(attrs={'rows': 2}),
            'vinculos_op':forms.Textarea(attrs={'rows': 2}),
            'vinculos_pp':forms.Textarea(attrs={'rows': 2}),
            'vinculos_au':forms.Textarea(attrs={'rows': 2}),
            'vinculos_de':forms.Textarea(attrs={'rows': 2}),
            'ingresos_fuente': forms.TextInput(attrs={'placeholder': 'Fuente de Ingresos'}),
            'inmuebles':forms.Textarea(attrs={'rows': 2}),
            'vehiculos':forms.Textarea(attrs={'rows': 2}),
            'cuentas_bancarias':forms.Textarea(attrs={'rows': 2}),
            'inversiones':forms.Textarea(attrs={'rows': 2}),
            'negocios':forms.Textarea(attrs={'rows': 2}),
            'demandas': forms.TextInput(attrs={'placeholder': 'Demandas del colectivo'}),
            'deudas':forms.Textarea(attrs={'rows': 2}),
            'medidas_presion':forms.Textarea(attrs={'rows': 2}),
            'grupos_choque':forms.Textarea(attrs={'rows': 2}),
            'uso_armas':forms.Textarea(attrs={'rows': 2}),
            'conflictos_organizaciones':forms.Textarea(attrs={'rows': 2}),
            'conflictos_legales':forms.Textarea(attrs={'rows': 2}),
            'grupos_disidentes':forms.Textarea(attrs={'rows': 2}),
            'perfil':forms.Textarea(attrs={'rows': 2}), 
            'capacidad_convocatoria':forms.Textarea(attrs={'rows': 2}), 
            'observaciones':forms.Textarea(attrs={'rows': 2}), 
            'fecha_creacion': forms.TextInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control  datetimepicker',
                    'min': '1940-01-01',
                    'max': '2025-31-12',
                }
            ),    
            'fecha_accion': forms.TextInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control  datetimepicker',
                    'min': '1940-01-01',
                    'max': '2025-31-12',
                }
            ),
            'user': forms.HiddenInput(
                attrs={
                    'required': False
                }
            ),    
            'observaciones_supervisor': forms.HiddenInput(
                attrs={
                    'required': False
                }
            ),            
            'actos_relevantes':forms.Textarea(attrs={'rows': 2}),
            'organos_difusion':forms.Textarea(attrs={'rows': 2}),
            'observaciones_supervisor':forms.Textarea(attrs={'rows': 2}),

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
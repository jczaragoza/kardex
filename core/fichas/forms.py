from django import forms
from django.forms import ModelForm

from django.core.exceptions import ValidationError

# %TEMP%
from crum import get_current_request
from django.contrib.auth import update_session_auth_hash

from core.fichas.models import Lider, Organizacion, Evento, Integrantes, Partido, Domicilios, TemasAtencion, Vehiculos, ExperienciaLaboral, CargosPopulares

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
        
    def save(self, commit=True):
        data = {}
        try:
            if self.is_valid():
                super().save()
            else:
                data['error'] = self.errors
        except Exception as e:
            data['error'] = str(e)
        return data

    # def update_session(self, user):
    #     request = get_current_request()
    #     if user == request.user:
    #         update_session_auth_hash(request, user)

    # def save(self, commit=True):
    #     data = {}
    #     form = super()
    #     try:
    #         if form.is_valid():
    #             u = form.save(commit=False)
    #             u.save()
    #             self.update_session(u)
    #         else:
    #             data['error'] = form.errors
    #     except Exception as e:
    #         data['error'] = str(e)
    #     return data

class ExperienciaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
                
    class Meta:
        model = ExperienciaLaboral
        fields = '__all__'

        widgets = {
            'nombre':forms.Textarea(attrs={'rows': 3, 'placeholder': 'Ejemplo: Director, Gerente, Subdirector, Secretario'}),
            'dependencia':forms.TextInput(attrs={'placeholder': 'Ejemplo: Seguridad, Gobierno del estado, Esc. Primaria Oficial, etc.'}),
            'periodo':forms.TextInput(attrs={'placeholder': 'Ejemplo: 2022-2024'}),
            'observaciones':forms.Textarea(attrs={'rows': 3}),
        }

        exclude = ['is_change_password', 'is_staff', 'user_permissions', 'date_joined',
                   'last_login', 'is_superuser', 'token']
        
    def save(self, commit=True):
        data = {}
        try:
            if self.is_valid():
                super().save()
            else:
                data['error'] = self.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    
class CargoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
                
    class Meta:
        model = CargosPopulares
        fields = '__all__'

        widgets = {
            'nombre':forms.Textarea(attrs={'rows': 3, 'placeholder': 'Ejemplo: Presidente Municipal, Diputado Local, etc.'}),
            'detalles':forms.TextInput(attrs={'placeholder': 'Ejemplo: Distrito XII, Municipio'}),
            'periodo':forms.TextInput(attrs={'placeholder': 'Ejemplo: 2022-2024'}),
            'observaciones':forms.Textarea(attrs={'rows': 3}),
        }

        exclude = ['is_change_password', 'is_staff', 'user_permissions', 'date_joined',
                   'last_login', 'is_superuser', 'token']
        
    def save(self, commit=True):
        data = {}
        try:
            if self.is_valid():
                super().save()
            else:
                data['error'] = self.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class TemasForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
                
    class Meta:
        model = TemasAtencion
        fields = '__all__'

        widgets = {
            'nombre':forms.Textarea(attrs={'rows': 5}),
        }

        exclude = ['is_change_password', 'is_staff', 'user_permissions', 'date_joined',
                   'last_login', 'is_superuser', 'token']
        
    def save(self, commit=True):
        data = {}
        try:
            if self.is_valid():
                super().save()
            else:
                data['error'] = self.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class DomicilioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
                
    class Meta:
        model = Domicilios
        fields = '__all__'

        widgets = {
            
            'calle': forms.TextInput(attrs={'placeholder': 'Ingrese nombre de la calle'}),
            'numero_ext': forms.TextInput(attrs={'placeholder': 'Ingrese número exterior'}),
            'numero_int': forms.TextInput(attrs={'placeholder': 'Ingrese número interior'}),
            'dpto': forms.TextInput(attrs={'placeholder': 'Departamento'}),
            'edificio': forms.TextInput(attrs={'placeholder': 'Edificio'}),
            'mzn': forms.TextInput(attrs={'placeholder': 'Manzana'}),
            'lote': forms.TextInput(attrs={'placeholder': 'Lote'}),
            'colonia': forms.TextInput(attrs={'placeholder': 'Colonia'}),
            'municipio': forms.TextInput(attrs={'placeholder': 'Ingrese municipio'}),
            'cp': forms.TextInput(attrs={'placeholder': 'Código Postal', 'maxlength':'5'}),
        }

        exclude = ['is_change_password', 'is_staff', 'user_permissions', 'date_joined',
                   'last_login', 'is_superuser', 'token']
        
    def save(self, commit=True):
        data = {}
        try:
            if self.is_valid():
                super().save()
            else:
                data['error'] = self.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    
class VehiculoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Hacer los campos requeridos
        self.fields['marca'].required = True
        self.fields['submarca'].required = True
        self.fields['matricula'].required = True
                
    class Meta:
        model = Vehiculos
        fields = '__all__'

        widgets = {
            'marca': forms.TextInput(attrs={'placeholder': 'Ingrese marca del vehículo'}),
            'submarca': forms.TextInput(attrs={'placeholder': 'Ingrese submarca del vehículo'}),
            'modelo': forms.TextInput(attrs={'placeholder': 'Ingrese modelo del vehículo (Año)'}),
            'color': forms.TextInput(attrs={'placeholder': 'Ingrese color'}),
            'matricula': forms.TextInput(attrs={'placeholder': 'Ingrese matricula'}),
            'observaciones':forms.Textarea(attrs={'rows': 2}),
        }

        exclude = ['is_change_password', 'is_staff', 'user_permissions', 'date_joined', 'last_login', 'is_superuser', 'token']
    def save(self, commit=True):
        data = {}
        try:
            if self.is_valid():
                super().save()
            else:
                data['error'] = self.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class LiderForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Lider
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
            'domicilios': forms.SelectMultiple(
                attrs={
                    'class': 'form-control select2',
                    'multiple': 'multiple',
                    'style': 'width:100%'
                }
            ),
            'vehiculos': forms.SelectMultiple(
                attrs={
                    'class': 'form-control select2',
                    'multiple': 'multiple',
                    'style': 'width:100%'
                }
            ),
            'domicilio_laboral':forms.Textarea(attrs={'rows': 2}),
            'padres':forms.Textarea(attrs={'rows': 2}),
            'conyuge':forms.Textarea(attrs={'rows': 2}),
            'hijos':forms.Textarea(attrs={'rows': 2}),
            'otros':forms.Textarea(attrs={'rows': 2}),
            'experiencia_laboral': forms.SelectMultiple(
                attrs={
                    'class': 'form-control select2',
                    'multiple': 'multiple',
                    'style': 'width:100%'
                }
            ),            
            'temas_atencion': forms.SelectMultiple(
                attrs={
                    'class': 'form-control select2',
                    'multiple': 'multiple',
                    'style': 'width:100%'
                }
            ),
            'amenazas':forms.Textarea(attrs={'rows': 2}),
            'comisiones':forms.Textarea(attrs={'rows': 2}),
            'actividades_politicas':forms.Textarea(attrs={'rows': 2}),
            'inmuebles':forms.Textarea(attrs={'rows': 2}),
            'cuentas_bancarias':forms.Textarea(attrs={'rows': 2}),
            'inversiones':forms.Textarea(attrs={'rows': 2}),
            'negocios':forms.Textarea(attrs={'rows': 2}),
            'demandas':forms.Textarea(attrs={'rows': 2}),
            'deudas':forms.Textarea(attrs={'rows': 2}),
            'cargos_populares': forms.SelectMultiple(
                attrs={
                    'class': 'form-control select2',
                    'multiple': 'multiple',
                    'style': 'width:100%'
                }
            ),         
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
            'observaciones_supervisor':forms.Textarea(attrs={'rows': 2}),
            'antecedentes_penales':forms.Textarea(attrs={'rows': 2}),
            'conflictos_legales':forms.Textarea(attrs={'rows': 2}),
            'conflictos_organizaciones':forms.Textarea(attrs={'rows': 2}),
            'organizaciones': forms.SelectMultiple(
                attrs={
                    'class': 'form-control select2',
                    'multiple': 'multiple',
                    'style': 'width:100%'
                }
            ), 
            'eventos': forms.SelectMultiple(
                attrs={
                    'class': 'form-control select2',
                    'multiple': 'multiple',
                    'style': 'width:100%'
                }
            ),            

            'user': forms.HiddenInput(
                attrs={
                    'required': False
                }
            ),

        }

        exclude = ['is_change_password', 'is_staff', 'user_permissions', 'date_joined', 'last_login', 'is_superuser', 'token']
        
    def save(self, commit=True):
        data = {}
        try:
            if self.is_valid():
                super().save()
            else:
                data['error'] = self.errors
        except Exception as e:
            data['error'] = str(e)
        return data

    # def update_session(self, user):
    #     request = get_current_request()
    #     if user == request.user:
    #         update_session_auth_hash(request, user)

    # def save(self, commit=True):
    #     data = {}
    #     form = super()
    #     try:
    #         if form.is_valid():
    #             u = form.save(commit=False)
    #             u.save()
    #             self.update_session(u)
    #         else:
    #             data['error'] = form.errors
    #     except Exception as e:
    #         data['error'] = str(e)
    #     return data

class LiderCapturaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Lider
        fields = '__all__'
        
        widgets = {

            'fecha_nacimiento': forms.TextInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control  datetimepicker',
                    'min': '1940-01-01',
                    'max': '2008-12-31',
                }
            ),
            'domicilio_particular':forms.Textarea(attrs={'rows': 2}),
            'domicilio_laboral':forms.Textarea(attrs={'rows': 2}),
            'padres':forms.Textarea(attrs={'rows': 2}),
            'conyuge':forms.Textarea(attrs={'rows': 2}),
            'hijos':forms.Textarea(attrs={'rows': 2}),
            'otros':forms.Textarea(attrs={'rows': 2}),
            'experiencia_laboral': forms.SelectMultiple(
                attrs={
                    'class': 'form-control select2',
                    'multiple': 'multiple',
                    'style': 'width:100%'
                }
            ),            
            'vehiculos': forms.SelectMultiple(
                attrs={
                    'class': 'form-control select2',
                    'multiple': 'multiple',
                    'style': 'width:100%'
                }
            ), 
            'temas_atencion': forms.SelectMultiple(
                attrs={
                    'class': 'form-control select2',
                    'multiple': 'multiple',
                    'style': 'width:100%'
                }
            ),
            'amenazas':forms.Textarea(attrs={'rows': 2}),
            'comisiones':forms.Textarea(attrs={'rows': 2}),
            'actividades_politicas':forms.Textarea(attrs={'rows': 2}),
            # 'domicilio_particular':forms.Textarea(attrs={'rows': 2}),
            'domicilios': forms.SelectMultiple(
                attrs={
                    'class': 'form-control select2',
                    'multiple': 'multiple',
                    'style': 'width:100%'
                }
            ),
            'inmuebles':forms.Textarea(attrs={'rows': 2}),
            'cuentas_bancarias':forms.Textarea(attrs={'rows': 2}),
            'inversiones':forms.Textarea(attrs={'rows': 2}),
            'negocios':forms.Textarea(attrs={'rows': 2}),
            'demandas':forms.Textarea(attrs={'rows': 2}),
            'deudas':forms.Textarea(attrs={'rows': 2}),
            'actividades_politicas':forms.Textarea(attrs={'rows': 2}),
            'cargos_populares': forms.SelectMultiple(
                attrs={
                    'class': 'form-control select2',
                    'multiple': 'multiple',
                    'style': 'width:100%'
                }
            ),         
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
            'observaciones_supervisor': forms.HiddenInput(
                attrs={
                    'required': False
                }
            ),
            'antecedentes_penales':forms.Textarea(attrs={'rows': 2}),
            'estatus_ficha': forms.HiddenInput(
                attrs={
                    'required': False
                }
            ),
            'conflictos_legales':forms.Textarea(attrs={'rows': 2}),
            'conflictos_organizaciones':forms.Textarea(attrs={'rows': 2}),
            'organizaciones': forms.SelectMultiple(
                attrs={
                    'class': 'form-control select2',
                    'multiple': 'multiple',
                    'style': 'width:100%'
                }
            ), 
            'eventos': forms.SelectMultiple(
                attrs={
                    'class': 'form-control select2',
                    'multiple': 'multiple',
                    'style': 'width:100%'
                }
            ),            

            'user': forms.HiddenInput(
                attrs={
                    'required': False
                }
            ),

        }

        exclude = ['is_change_password', 'is_staff', 'user_permissions', 'date_joined',
                   'last_login', 'is_superuser', 'token', 'is_active']

    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')

        if fecha_nacimiento:
            try:
                # Intenta parsear la fecha y extraer el año
                year = int(fecha_nacimiento.split('-')[0])
                if len(str(year)) > 4:
                    raise ValidationError("El año no puede tener más de 4 dígitos.")
            except ValueError:
                raise ValidationError("Formato de fecha no válido.")

        return fecha_nacimiento

    def save(self, commit=True):
        data = {}
        try:
            if self.is_valid():
                super().save()
            else:
                data['error'] = self.errors
        except Exception as e:
            data['error'] = str(e)
        return data

    # def update_session(self, user):
    #     request = get_current_request()
    #     if user == request.user:
    #         update_session_auth_hash(request, user)

    # def save(self, commit=True):
    #     data = {}
    #     form = super()
    #     try:
    #         if form.is_valid():
    #             u = form.save(commit=False)
    #             u.save()
    #             self.update_session(u)
    #         else:
    #             data['error'] = form.errors
    #     except Exception as e:
    #         data['error'] = str(e)
    #     return data

class OrganizacionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    
    class Meta:
        model = Organizacion
        fields = '__all__'

        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese nombre del colectivo'}),
            'inicio_actividades': forms.TextInput(attrs={'placeholder': 'Descripción de antecedentes de la organización'}),
            'registro': forms.TextInput(attrs={'placeholder': 'Registro Oficial del colectivo'}),
            'objetivo':forms.Textarea(attrs={'rows': 2}),
            'fecha_creacion': forms.TextInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control  datetimepicker',
                    'min': '1940-01-01',
                    'max': '2025-31-12',
                }
            ),
            'situacion_actual': forms.Textarea(attrs={'rows': 2}),
            'cargo': forms.TextInput(attrs={'placeholder': 'Ingrese cargo del dirigente'}),
            'direccion':forms.Textarea(attrs={'rows': 2}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Ingrese número de teléfono'}),
            'correo': forms.TextInput(attrs={'placeholder': 'Ingrese Correo'}),
            'facebook': forms.TextInput(attrs={'placeholder': 'Ingrese facebook'}),
            'instagram': forms.TextInput(attrs={'placeholder': 'Ingrese Instagram'}),
            'twitter': forms.TextInput(attrs={'placeholder': 'Ingrese Twitter'}),
            'zona_influencia': forms.TextInput(attrs={'placeholder': 'Zona de influencia'}),
            'zona_operaciones': forms.TextInput(attrs={'placeholder': 'Zona, Colonias o Localidades donde opera'}),
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
            'fecha_accion': forms.TextInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control  datetimepicker',
                    'min': '1940-01-01',
                    'max': '2025-31-12',
                }
            ),
            'actos_relevantes':forms.Textarea(attrs={'rows': 2}),
            'organos_difusion':forms.Textarea(attrs={'rows': 2}),
            'observaciones_supervisor':forms.Textarea(attrs={'rows': 2}),
            'lideres': forms.SelectMultiple(
                attrs={
                    'class': 'form-control select2',
                    'multiple': 'multiple',
                    'style': 'width:100%'
                }
            ),
            'eventos': forms.SelectMultiple(
                attrs={
                    'class': 'form-control select2',
                    'multiple': 'multiple',
                    'style': 'width:100%'
                }
            ),  
            'user': forms.HiddenInput(
                attrs={
                    'required': False
                }
            ),
            
        }

        exclude = []

    # def update_session(self, user):
    #     request = get_current_request()
    #     if user == request.user:
    #         update_session_auth_hash(request, user)

    def save(self, commit=True):
        data = {}
        try:
            if self.is_valid():
                super().save()
            else:
                data['error'] = self.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    
class OrganizacionCapturaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    
    class Meta:
        model = Organizacion
        fields = '__all__'

        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese nombre del colectivo'}),
            'inicio_actividades': forms.TextInput(attrs={'placeholder': 'Descripción de antecedentes de la organización'}),
            'registro': forms.TextInput(attrs={'placeholder': 'Registro Oficial del colectivo'}),
            'objetivo':forms.Textarea(attrs={'rows': 2}),
            'fecha_creacion': forms.TextInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control  datetimepicker',
                    'min': '1940-01-01',
                    'max': '2025-31-12',
                }
            ),
            'situacion_actual': forms.Textarea(attrs={'rows': 2}),
            'cargo': forms.TextInput(attrs={'placeholder': 'Ingrese cargo del dirigente'}),
            'direccion':forms.Textarea(attrs={'rows': 2}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Ingrese número de teléfono'}),
            'correo': forms.TextInput(attrs={'placeholder': 'Ingrese Correo'}),
            'facebook': forms.TextInput(attrs={'placeholder': 'Ingrese facebook'}),
            'instagram': forms.TextInput(attrs={'placeholder': 'Ingrese Instagram'}),
            'twitter': forms.TextInput(attrs={'placeholder': 'Ingrese Twitter'}),
            'zona_influencia': forms.TextInput(attrs={'placeholder': 'Zona de influencia'}),
            'zona_operaciones': forms.TextInput(attrs={'placeholder': 'Zona, Colonias o Localidades donde opera'}),
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
            'lideres': forms.SelectMultiple(
                attrs={
                    'class': 'form-control select2',
                    'multiple': 'multiple',
                    'style': 'width:100%'
                }
            ),
            'integrantes_nombres': forms.SelectMultiple(
                attrs={
                    'class': 'form-control select2',
                    'multiple': 'multiple',
                    'style': 'width:100%', 
                }
            ),
            'eventos': forms.SelectMultiple(
                attrs={
                    'class': 'form-control select2',
                    'multiple': 'multiple',
                    'style': 'width:100%'
                }
            ),  
            'user': forms.HiddenInput(
                attrs={
                    'required': False
                }
            ),
            
        }

        exclude = []

    # def update_session(self, user):
    #     request = get_current_request()
    #     if user == request.user:
    #         update_session_auth_hash(request, user)

    def save(self, commit=True):
        data = {}
        try:
            if self.is_valid():
                super().save()
            else:
                data['error'] = self.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    
class IntegranteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    
    class Meta:
        model = Integrantes
        fields = '__all__'

        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese nombre del integrante'}),
            'Cargo': forms.TextInput(attrs={'placeholder': 'Ingrese cargo en el colectivo'}),
        }

        exclude = []

    def save(self, commit=True):
        data = {}
        try:
            if self.is_valid():
                super().save()
            else:
                data['error'] = self.errors
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

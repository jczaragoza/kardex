# Create your models here.
from django.db import models
from django.forms import CharField
from django.forms.models import model_to_dict
from config.settings import MEDIA_URL, STATIC_URL
from smart_selects.db_fields import ChainedForeignKey


from core.organizaciones.choices import *
from datetime import date, datetime
from core.user.models import *

# model Eventos
class Evento(models.Model): 
    nombre = models.CharField(max_length=255, verbose_name='Nombre del Evento')
    descripcion = models.TextField(verbose_name = 'Descripción del Evento')
    fecha_evento = models.TextField(verbose_name='Fecha de Evento', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    def get_full_name(self):
        return '{} / {}'.format(self.nombre, self.fecha_evento)

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['-fecha_evento']
    
    def toJSON(self):
        item = model_to_dict(self)
        item['modified'] = self.modified.strftime('%Y-%m-%d')
        item['full_name'] = self.get_full_name()
        return item
    
    #MAYÚSCULAS
    def save(self):
        self.nombre = self.nombre.upper()
        super(Evento, self).save()

# model Organización
class Organizacion(models.Model): 
    nombre = models.CharField(max_length=255, verbose_name='Nombre de Organización')
    tipo_organizacion = models.CharField(max_length=255, null=True, blank=True, choices=tipo_org, default='Sin Información')
    foto = models.ImageField(blank=True, null=True, upload_to='organizaciones/fotos', verbose_name='Imagen')
    fecha_creacion = models.DateField(verbose_name='Fecha de Creación', null=True, blank=True)
    inicio_actividades = models.CharField(max_length=255, blank=True, null=True, verbose_name='Antecedentes (Descripción)')
    registro = models.CharField(max_length=255, null=True, blank=True, verbose_name='Registro Oficial')
    objetivo = models.TextField(null=True, blank=True, verbose_name='Objetivo de la Organización')
    tendencia = models.CharField(max_length=500, blank=True, null=True, verbose_name='Tendencia Ideológica')
    #tendencia = models.CharField(max_length=500, blank=True, null=True, verbose_name='Tendencia Ideológica', choices=tendencia_choices, default='Sin Información')
    situacion_actual = models.TextField(blank=True, null=True, verbose_name='Situación Actual')
    #dirigentes = models.CharField(max_length=550, blank=True, null=True, verbose_name='Dirigentes')
    integrantes = models.PositiveIntegerField(null=True, blank=True, verbose_name='Número de Integrantes', default='1')    
    #cargo = models.CharField(max_length=50, blank=True, null=True, verbose_name='Cargo')
    direccion = models.TextField(null=True, blank=True, verbose_name='Dirección de oficinas')
    telefono = models.CharField(max_length=50, blank=True, null=True, verbose_name='Teléfono')
    sitio_web = models.CharField(max_length=255, blank=True, null=True, verbose_name='Sitio WEB')
    correo = models.EmailField(max_length=50, blank=True, null=True, verbose_name='Correo Electrónico')
    facebook = models.CharField(max_length=255, blank=True, null=True, verbose_name='Facebook')
    seguidores = models.PositiveIntegerField(null=True, blank=True, verbose_name='Número de Seguidores en Faceboook', default='1')    
    instagram = models.CharField(max_length=50, blank=True, null=True, verbose_name='Instagram')
    twitter = models.CharField(max_length=50, blank=True, null=True, verbose_name='Twitter')
    zona_influencia = models.CharField(max_length=255, blank=True, null=True, verbose_name='Zona de Influencia')
    zona_operaciones = models.CharField(max_length=255, blank=True, null=True, verbose_name='Zona, Colonias o Localidades donde opera')
    puntos_reunion = models.TextField(blank=True, null=True, verbose_name='Puntos de reunión')
    poder_convocatoria = models.CharField(max_length=20, blank=True, null=True, verbose_name='Poder de convocatoria', choices=convocatoria_choices, default='Bajo' )
    capacidad_convocatoria = models.TextField(blank=True, null=True, verbose_name='Capacidad de convocatoria')
    principales_actividades = models.TextField(blank=True, null=True, verbose_name='Principales Actividades')
    modus_operandi = models.TextField(blank=True, null=True, verbose_name='Modus Operandi')
    vinculos_os = models.TextField(blank=True, null=True, verbose_name='Vínculos con Organizaciónes Sociales')
    vinculos_op = models.TextField(blank=True, null=True, verbose_name='Vínculos con Organizaciónes Políticas')
    vinculos_pp = models.TextField(blank=True, null=True, verbose_name='Vínculos con Partidos Políticos')
    vinculos_au = models.TextField(blank=True, null=True, verbose_name='Vínculos con Autoridades')
    vinculos_de = models.TextField(blank=True, null=True, verbose_name='Vínculos Delictivos')
    fuente_ingresos = models.CharField(max_length=255, blank=True, null=True, verbose_name='Fuente de Ingresos')
    inmuebles = models.TextField(blank=True, null=True, verbose_name='Inmuebles')
    vehiculos = models.TextField(blank=True, null=True, verbose_name='Vehículos')
    cuentas_bancarias = models.TextField(blank=True, null=True, verbose_name='Cuentas Bancarias')
    inversiones = models.TextField(blank=True, null=True, verbose_name='Inversiones')
    negocios = models.TextField(blank=True, null=True, verbose_name='Negocios')
    demandas = models.TextField(blank=True, null=True, verbose_name='Demandas')
    deudas = models.TextField(blank=True, null=True, verbose_name='Deudas')
    medidas_presion = models.TextField(blank=True, null=True, verbose_name='Medidas de presión para conseguir sus demandas')
    grupos_choque = models.TextField(blank=True, null=True, verbose_name='Grupos de choque')
    uso_armas = models.TextField(blank=True, null=True, verbose_name='Utilización de Armas')
    conflictos_organizaciones = models.TextField(blank=True, null=True, verbose_name='Conflictos con otras organizaciones')
    conflictos_legales = models.TextField(blank=True, null=True, verbose_name='Conflictos Legales')
    grupos_disidentes = models.TextField(blank=True, null=True, verbose_name='Grupos disidentes al interior de la organización, dirigentes y número de integrantes')
    organos_difusion = models.TextField(blank=True, null=True, verbose_name='Organos de Difusión')
    observaciones = models.TextField(blank=True, null=True, verbose_name='Observaciones de la Organización')
    perfil = models.TextField(blank=True, null=True, verbose_name='Perfil')
    riesgo = models.CharField(max_length=20, blank=True, null=True, verbose_name='Riesgo', choices=riesgo_choices, default='Bajo' )
    estatus_ficha = models.CharField(max_length=50, blank=True, null=True, verbose_name='Estatus ficha', choices=estatus_ficha_choices, default='En proceso')
    observaciones_supervisor = models.TextField(max_length=255, null=True, blank=True, verbose_name='Observaciones de supervisor')
       
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.nombre

    def get_user(self):
        return '{}'.format(self.user)

    def toJSON(self):
        item = model_to_dict(self)
        item['foto'] = self.get_image()
        item['modified'] = self.modified.strftime('%Y-%m-%d')
        item['fecha_creacion'] = self.fecha_creacion.strftime('%Y-%m-%d')
        item['usuario'] = self.get_user()
        return item

    def get_image(self):
        if self.foto:
            return '{}{}'.format(MEDIA_URL, self.foto)
        return '{}{}'.format(STATIC_URL, 'img/user1.png')

    class Meta:
        verbose_name = 'Organizacion'
        ordering = ['id']

    #MAYÚSCULAS
    def save(self):
        self.nombre = self.nombre.upper()
        super(Organizacion, self).save()

# model Ficha curricular.
class FichaCurricular(models.Model): 
    nombre = models.CharField(max_length=255, verbose_name='Nombre(s)')
    apaterno = models.CharField(max_length=255, verbose_name='Apellido Paterno')
    amaterno = models.CharField(max_length=255, verbose_name='Apellido Materno')
    fecha_nacimiento = models.TextField(verbose_name='Fecha de Nacimiento')
    lugar_nacimiento = models.CharField(max_length=510, blank=True, null=True, verbose_name='Lugar de Nacimiento')
    nacionalidad = models.CharField(max_length=10, blank=True, null=True, verbose_name='Nacionalidad')
    zona_influencia = models.CharField(max_length=500, verbose_name='Zona de Influencia')
    alias = models.CharField(max_length=255, blank=True, null=True, verbose_name='Alias')
    sexo = models.CharField(max_length=50, blank=True, null=True, verbose_name='Sexo', choices=sexo_choices, default='No definido')
    estado_civil = models.CharField(max_length=50, blank=True, null=True, verbose_name='Estado Civíl', choices=estado_civil_choices, default='Soltero')
    rfc = models.CharField(max_length=13, blank=True, null=True, verbose_name='RFC')
    curp = models.CharField(max_length=18, null=True, verbose_name='CURP')
    domicilio_particular = models.TextField(null=True, blank=True, verbose_name='Domicilio Particular')
    telefono_particular = models.CharField(max_length=20, blank=True, null=True, verbose_name='Teléfono Particular')
    domicilio_laboral = models.TextField(null=True, blank=True, verbose_name='Domicilio Laboral')
    telefono_trabajo = models.CharField(max_length=20, blank=True, null=True, verbose_name='Teléfono Trabajo')
    correo = models.EmailField(max_length=255, blank=True, null=True, verbose_name='Correo Electrónico')
    facebook = models.CharField(max_length=255, blank=True, null=True, verbose_name='Facebook')
    instagram = models.CharField(max_length=50, blank=True, null=True, verbose_name='Instagram')
    twitter = models.CharField(max_length=50, blank=True, null=True, verbose_name='Twitter')
    formacion_academica = models.CharField(max_length=255, blank=True, null=True, verbose_name='Formación Academica') 
    padres = models.TextField(null=True, blank=True, verbose_name='Padres')
    conyuge = models.TextField(null=True, blank=True, verbose_name='Cónyuge')
    hijos = models.TextField(null=True, blank=True, verbose_name='Hijos')
    otros = models.TextField(null=True, blank=True, verbose_name='Otros Familiares')
    organizacion = models.ForeignKey(Organizacion, blank=True, null=True, on_delete=models.SET_NULL)
    puesto_ocupado = models.CharField(max_length=255, blank=True, null=True, verbose_name='Puesto Ocupado en organización')
    periodo = models.CharField(max_length=255, blank=True, null=True, verbose_name='periodo organización')
    antecedentes_laborales = models.CharField(max_length=255, blank=True, null=True, verbose_name='Antecedentes Laborales "Empresa o Dependencia"')
    puesto_ocupado_laboral = models.CharField(max_length=255, blank=True, null=True, verbose_name='Puesto ocupado en empresa o dependencia')
    periodo_laboral = models.CharField(max_length=255, blank=True, null=True, verbose_name='Periodo laboral en empresa o dependencia ')    
    fuente_ingresos = models.CharField(max_length=255, blank=True, null=True, verbose_name='Fuente de Ingresos')
    inmuebles = models.TextField(blank=True, null=True, verbose_name='Inmuebles')
    vehiculos = models.TextField(blank=True, null=True, verbose_name='Vehículos')
    cuentas_bancarias = models.TextField(blank=True, null=True, verbose_name='Cuentas Bancarias')
    inversiones = models.TextField(blank=True, null=True, verbose_name='Inversiones')
    negocios = models.TextField(blank=True, null=True, verbose_name='Negocios')
    demandas = models.TextField(blank=True, null=True, verbose_name='Demandas')
    deudas = models.TextField(blank=True, null=True, verbose_name='Deudas')
    vinculos_orgs = models.TextField(blank=True, null=True, verbose_name='Vínculos con Organizaciónes Sociales')
    vinculos_pol = models.TextField(blank=True, null=True, verbose_name='Vínculos Políticos')
    vinculos_ongs = models.TextField(blank=True, null=True, verbose_name='Vínculos con ONGS')
    vinculos_autoridades = models.TextField(blank=True, null=True, verbose_name='Vínculos con Autoridades')
    vinculos_delictivos = models.TextField(blank=True, null=True, verbose_name='Vínculos Delictivos')
    antecedentes_penales = models.TextField(blank=True, null=True, verbose_name='Antecedentes Penales')
    actividades_politicas = models.TextField(blank=True, null=True, verbose_name='Actividades Políticas')
    conflictos_legales = models.TextField(blank=True, null=True, verbose_name='Conflictos Legales')
    puestos_eleccion_popular = models.TextField(blank=True, null=True, verbose_name='Puestos de Elección Popular')
    poder_convocatoria = models.CharField(max_length=20, blank=True, null=True, verbose_name='Poder de convocatoria', choices=convocatoria_choices, default='Bajo' )
    capacidad_convocatoria = models.TextField(blank=True, null=True, verbose_name='Capacidad de convocatoria')
    imagen_publica = models.TextField(blank=True, null=True, verbose_name='Imágen Pública')
    foto = models.ImageField(blank=True, null=True, upload_to='persona/fotos', verbose_name='Imagen')
    vulnerabilidades = models.TextField(blank=True, null=True, verbose_name='Vulnerabilidades')
    habilidades = models.TextField(blank=True, null=True, verbose_name='Capacidades o Hábilidades')
    perfil = models.TextField(blank=True, null=True, verbose_name='Perfil')
    riesgo = models.CharField(max_length=20, blank=True, null=True, verbose_name='Riesgo', choices=riesgo_choices, default='Bajo' )
    estatus_ficha = models.CharField(max_length=50, blank=True, null=True, verbose_name='Estatus ficha', choices=estatus_ficha_choices, default='En proceso')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    observaciones = models.TextField(blank=True, null=True, verbose_name='Observaciones')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre 

    def get_full_name(self):
        return '{} {} {}'.format(self.nombre, self.apaterno, self.amaterno)

    def get_org(self): 
        return '{}'.format(self.organizacion)

    def toJSON(self):
        item = model_to_dict(self)
        item['full_name'] = self.get_full_name()
        item['foto'] = self.get_image()
        item['modified'] = self.modified.strftime('%d-%m-%Y')
        item['full_org'] = self.get_org()
     
        return item

    def get_image(self):
        if self.foto:
            return '{}{}'.format(MEDIA_URL, self.foto)
        return '{}{}'.format(STATIC_URL, 'img/user1.png')

    
    def get_edad(self):
        today = date.today()
        return today.year - self.fecha_nacimiento.year - ((today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))

    class Meta:
        verbose_name = 'fichacurricular'
        verbose_name_plural = 'Fichacurricular'
        ordering = ['id']

    #MAYÚSCULAS
    def save(self):
        self.nombre = self.nombre.upper()
        self.apaterno = self.apaterno.upper()
        self.amaterno = self.amaterno.upper()
        self.zona_influencia = self.zona_influencia.upper()
        super(FichaCurricular, self).save()

# model detalle Evento
class Detalle(models.Model): 
    
    organizacion = models.ForeignKey(Organizacion, on_delete=models.SET_NULL, blank=True, null=True)
    evento = models.ForeignKey(Evento, on_delete=models.SET_NULL, blank=True, null=True)
    fichacurricular = models.ForeignKey(FichaCurricular, on_delete=models.SET_NULL, blank=True, null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def get_evento(self): 
        return '{} / {}'.format(self.evento.nombre, self.evento.fecha_evento)
    
    def get_fechaevento(self): 
        return '{}'.format(self.evento.fecha_evento)

    def get_org(self): 
        return '{}'.format(self.organizacion)

    def get_ficha(self): 
        return '{}'.format(self.fichacurricular)

    def toJSON(self):
        item = model_to_dict(self)
        item['full_evento'] = self.get_evento()
        item['fecha_evento'] = self.get_fechaevento()
        item['full_org'] = self.get_org()
        item['full_ficha'] = self.get_ficha()
        item['modified'] = self.modified.strftime('%Y-%m-%d')
        return item
        
    class Meta:
        verbose_name = 'detalle'
        verbose_name_plural = 'Detalles'
        ordering = ['id']

from django.db import models

# Create your models here.
from django.db import models
from django.forms.models import model_to_dict
from config.settings import MEDIA_URL, STATIC_URL
from smart_selects.db_fields import ChainedForeignKey

from core.candidatos.choices import *
from datetime import date, datetime

from core.user.models import *

class TipoContendiente(models.Model):
    tipo_contendiente = models.CharField(max_length=50, blank=True, null=True, verbose_name='Contendiente a')
    
    def __str__(self):
        return self.tipo_contendiente
        
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Contendiente'
        verbose_name_plural = 'Contendientes'
        ordering = ['id']

#Model Municipio
class Municipio(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre de Municipio')
    tipo_contendiente = models.ForeignKey(TipoContendiente, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.nombre 
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Municipio, self).save()
    
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Municipio'
        ordering = ['id']

#MODEL DISTRITOS LOCALES EDOMEX
class Distrito_local(models.Model):
    nombre = models.CharField(max_length=255, null=True, blank=True, verbose_name='Distrito Local')
    municipios_rango = models.PositiveIntegerField(null=True, blank=True, verbose_name='Municipios que abarca', default='1')
    tipo_contendiente = models.ForeignKey(TipoContendiente, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.nombre
        
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Distrito Local'
        verbose_name_plural = 'Distritos Locales'
        ordering = ['id']

class Distrito_local_cabeceras(models.Model):
    cabecera = models.CharField(max_length=255, null=True, blank=True, verbose_name='Cabeceras')
    distrito_local = models.ForeignKey(Distrito_local, on_delete=models.SET_NULL, blank=True, null=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.cabecera
    
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Distrito Local Cabeceras'
        verbose_name_plural = 'Distritos Locales Cabeceras'
        ordering = ['id']

#MODEL DISTRITOS FEDERALES EDOMEX
class Distrito_federal(models.Model):
    nombre = models.CharField(max_length=255, null=True, blank=True, verbose_name='Distrito Federal')
    municipios_rango = models.PositiveIntegerField(null=True, blank=True, verbose_name='Municipios que abarca', default='1')
    tipo_contendiente = models.ForeignKey(TipoContendiente, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.nombre
        
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Distrito Federal'
        verbose_name_plural = 'Distritos Federales'
        ordering = ['id']

class Distrito_federal_municipios(models.Model):
    distrito_federal = models.ForeignKey(Distrito_federal, on_delete=models.SET_NULL, blank=True, null=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.distrito_federal
        
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Distrito Federal Municipio'
        verbose_name_plural = 'Distritos Federales Municipios'
        ordering = ['id']

class Partido(models.Model):
    nombre = models.CharField(max_length=255, null=True, blank=True, verbose_name='Nombre partido')
    siglas = models.CharField(max_length=100, blank=True, null=True, verbose_name='Siglas Partido', choices=partido_siglas_choices, default='PAN')
    foto = models.ImageField(blank=True, null=True, upload_to='candiato/fotos', verbose_name='Imagen Partido')
        
    def __str__(self):
        return self.nombre

    def get_image(self):
        if self.foto:
            return '{}{}'.format(MEDIA_URL, self.foto)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')


    #MAYÚSCULAS
    def save(self):
        self.nombre = self.nombre.upper()
        super(Partido, self).save()

    def toJSON(self):
        item = model_to_dict(self)
        item['foto'] = self.get_image()
        return item

    class Meta:
        verbose_name = 'Partido'
        verbose_name_plural = 'Partidos'
        ordering = ['id']

# model Candidato.
class Candidato(models.Model): 
    tipo_contendiente = models.ForeignKey(TipoContendiente, on_delete=models.SET_NULL, blank=True, null=True)
    distrito_local = ChainedForeignKey(
        Distrito_local,
        chained_field="tipo_contendiente",
        chained_model_field="tipo_contendiente", 
        show_all=False,
        auto_choose=True,
        sort=True,
        blank=True,
        null=True
    )
    municipio = ChainedForeignKey(
        Municipio,
        chained_field="tipo_contendiente",
        chained_model_field="tipo_contendiente", 
        show_all=False,
        auto_choose=True,
        sort=True,
        blank=True,
        null=True
    )
    distrito_federal = ChainedForeignKey(
        Distrito_federal,
        chained_field="tipo_contendiente",
        chained_model_field="tipo_contendiente", 
        show_all=False,
        auto_choose=True,
        sort=True,
        blank=True,
        null=True
    )
    periodo = models.CharField(max_length=25, blank=True, null=True, verbose_name='Período', choices=periodo_choices, default='2022 - 2024')
    nombre = models.CharField(max_length=255, verbose_name='Nombre(s)')
    apaterno = models.CharField(max_length=255, verbose_name='Apellido Paterno')
    amaterno = models.CharField(max_length=255, verbose_name='Apellido Materno')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de Nacimiento')
    estatus_candidato = models.CharField(max_length=50, verbose_name='Estatus Candidato', choices=estatus_candidato_choices)
    foto = models.ImageField(blank=True, null=True, upload_to='candidato/fotos', verbose_name='Imagen')
    partido = models.ForeignKey(Partido, on_delete=models.SET_NULL, null=True)
    rfc = models.CharField(max_length=13, null=True, verbose_name='RFC', unique=True)
    curp = models.CharField(max_length=18, null=True, verbose_name='CURP', unique=True)
    direccion = models.TextField(null=True, blank=True, verbose_name='Domicilio')
    # direccion = models.JSONField(default=list)
    estado_civil = models.CharField(max_length=50, blank=True, null=True, verbose_name='Estado Civil', choices=estado_civil_choices)
    correo = models.EmailField(max_length=50, blank=True, null=True, verbose_name='Correo Electrónico')
    telefono_fijo = models.CharField(max_length=20, blank=True, null=True, verbose_name='Teléfono Fijo')
    telefono_movil = models.CharField(max_length=20, blank=True, null=True, verbose_name='Teléfono Móvil')
    escolaridad = models.CharField(max_length=255, null=True, blank=True, verbose_name= 'Formación Académica')
    vinculos_delincuencia = models.TextField(null=True, blank=True, verbose_name='Vínculos con la delincuencia organizada')
    vehiculo = models.TextField(max_length=500, null=True, blank=True, verbose_name='Vehículos')
    facebook = models.CharField(max_length=255, blank=True, null=True, verbose_name='Facebook')
    twitter = models.CharField(max_length=50, blank=True, null=True, verbose_name='Twitter')
    zona_influencia = models.CharField(max_length=255, blank=False, null=True, verbose_name='Zona de Influencia')
    poder_convocatoria = models.CharField(max_length=20, blank=True, null=True, verbose_name='Poder de convocatoria', choices=convocatoria_choices, default='Bajo' )
    vinculos_politicos = models.TextField(blank=True, null=True, verbose_name='Vínculos Políticos')
    cargos_ocupados = models.TextField(blank=True, null=True, verbose_name='Cargos Ocupados')
    experiencia_laboral = models.TextField(blank=True, null=True, verbose_name='Experiencia Laboral')
    comisiones = models.TextField(blank=True, null=True, verbose_name='Comisiones')
    temas_atencion = models.TextField(blank=True, null=True, verbose_name='Temas de Atención')
    amenazas = models.TextField(blank=True, null=True, verbose_name='Amenazas')
    riesgo = models.CharField(max_length=20, blank=True, null=True, verbose_name='Riesgo', choices=riesgo_choices, default='Bajo' )
    estatus_ficha = models.CharField(max_length=50, blank=True, null=True, verbose_name='Estatus ficha', choices=estatus_ficha_choices, default='Revisado')
    protesta = models.CharField(max_length=50, blank=True, null=True, verbose_name='Ha tomado protesta', choices=protesta_choices, default='SI')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, verbose_name='Estado')

    def get_user(self):
        return '{}'.format(self.user)
        
    def get_full_name(self):
        return '{} {} {}'.format(self.nombre, self.apaterno, self.amaterno)

    def get_partido(self):
        return '{}'.format(self.partido.siglas)

    def get_municipio(self):
        return '{}'.format(self.municipio.nombre)

    def toJSON(self):
        item = model_to_dict(self)
        item['full_name'] = self.get_full_name()
        item['foto'] = self.get_image()
        item['fecha_nacimiento'] = self.fecha_nacimiento.strftime('%Y-%m-%d')
        item['modified'] = self.modified.strftime('%Y-%m-%d')
        item['full_partido'] = self.get_partido()
        item['usuario'] = self.get_user()
             
        return item

    def get_image(self):
        if self.foto:
            return '{}{}'.format(MEDIA_URL, self.foto)
        return '{}{}'.format(STATIC_URL, 'img/user1.png')

    def __str__(self):
        return self.get_full_name()
    
    # CALCULAR EDAD
    def get_edad(self):
        today = date.today()
        return today.year - self.fecha_nacimiento.year - ((today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))

    class Meta:
        verbose_name = 'Candidato'
        verbose_name_plural = 'Candidatos'
        ordering = ['id']

    #MAYÚSCULAS
    def save(self):
        self.nombre = self.nombre.upper()
        self.apaterno = self.apaterno.upper()
        self.amaterno = self.amaterno.upper()
        self.rfc = self.rfc.upper()
        self.curp = self.curp.upper()
        self.zona_influencia = self.zona_influencia.upper()
        super(Candidato, self).save()



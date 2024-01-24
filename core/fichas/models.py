# Create your models here.
import datetime
from django.db import models
from django.forms.models import model_to_dict
from config.settings import MEDIA_URL, STATIC_URL

from datetime import date
from datetime import datetime as dt  # Cambié el nombre de datetime a dt
from django.db import models

from core.user.models import *

#Choices
from core.fichas.choices import *

# model Eventos
class Evento(models.Model): 
    nombre = models.CharField(max_length=255, verbose_name='Nombre del Evento')
    descripcion = models.TextField(verbose_name = 'Descripción del Evento')
    fecha_evento = models.TextField(verbose_name='Fecha de Evento', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} / {}'.format(self.fecha_evento, self.nombre)
    
    def toJSON(self):
        item = model_to_dict(self)
        item['modified'] = self.modified.strftime('%Y-%m-%d')
        return item
    
    #MAYÚSCULAS
    def save(self):
        self.nombre = self.nombre.upper()
        super(Evento, self).save()

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['fecha_evento']

# Modelo Integrantes.
class Integrantes(models.Model): 
    nombre = models.CharField(max_length=255, verbose_name='Nombre(s)')
    Cargo = models.CharField(max_length=255, verbose_name='Cargo')

    def __str__(self):
        return self.nombre
    
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Integrante'
        ordering = ['id']

# Modelo Direcciones.
class Domicilios(models.Model): 
    abrev = models.CharField(max_length=50, blank=True, null=True, verbose_name='Abreviatura', choices = abreviatura_choices)
    calle = models.CharField(max_length=255, verbose_name='Calle', null = True, blank = True)
    numero_ext = models.CharField(max_length=255, verbose_name='Número Exterior', null = True, blank = True)
    numero_int = models.CharField(max_length=255, verbose_name='Número Interior', null = True, blank = True)
    dpto = models.CharField(max_length=255, verbose_name='Departamento', null = True, blank = True)
    edificio = models.CharField(max_length=255, verbose_name='Edificio', null = True, blank = True)
    mzn = models.CharField(max_length=255, verbose_name='Manzana', null = True, blank = True)
    lote = models.CharField(max_length=255, verbose_name='Lote', null = True, blank = True)
    colonia = models.CharField(max_length=255, verbose_name='Colonia', null=True, blank=True)
    municipio = models.CharField(max_length=255, verbose_name='Municipio', null=True, blank=True)
    estado = models.CharField(max_length=50, blank=True, null=True, verbose_name='Estado', choices=estado_choices, default='Estado de México')
    cp = models.PositiveBigIntegerField(verbose_name='Código postal', null=True, blank=True)
    
    def __str__(self):
        # Lista de campos a mostrar en el formato
        campos = [self.abrev, self.calle, self.numero_ext, self.numero_int, self.dpto, self.edificio, self.mzn, self.lote, self.colonia, self.municipio, self.estado, self.cp]

        # Filtra los campos que no son None o están vacíos
        campos_filtrados = [campo for campo in campos if campo not in (None, '', 'NULL')]

        # Concatena los campos filtrados en el formato
        return ', '.join(map(str, campos_filtrados))
    
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'domicilio'
        verbose_name_plural = 'domicilios'
        ordering = ['id']

# Modelo Vehículos.
class Vehiculos(models.Model): 
    marca = models.CharField(max_length=255, verbose_name='Marca')
    submarca = models.CharField(max_length=255, verbose_name='Submarca', null=True, blank=True)
    modelo = models.CharField(max_length=255, verbose_name='Modelo', null=True, blank=True)
    color = models.CharField(max_length=255, verbose_name='Color', null=True, blank=True)
    matricula = models.CharField(max_length=8, verbose_name='Matricula', null=True, blank=True)
    observaciones = models.TextField(verbose_name='Observaciones', blank=True, null=True)
    
    def __str__(self):
        # Lista de campos a mostrar en el formato
        campos = [self.marca, self.submarca, self.modelo, self.color, self.matricula]

        # Filtra los campos que no son None o están vacíos
        campos_filtrados = [campo for campo in campos if campo not in (None, '', 'NULL')]

        # Concatena los campos filtrados en el formato
        return ', '.join(map(str, campos_filtrados))
    
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'vehiculo'
        verbose_name_plural = 'vehiculos'
        ordering = ['id']

# Modelo Temas_atención.
class TemasAtencion(models.Model): 
    nombre = models.TextField(verbose_name='Descripción')
    
    def __str__(self):
        return self.nombre[:200]
    
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'tema_atencion'
        ordering = ['id']

# Modelo Experiencia Laboral.
class ExperienciaLaboral(models.Model): 
    nombre = models.TextField(verbose_name='Descripción del puesto', blank=True, null=True)
    dependencia = models.CharField(max_length=1024, null=True, blank=True, verbose_name='Empresa o Dependencia')
    periodo = models.CharField(max_length=255, blank=True, null=True, verbose_name='Periodo')
    observaciones = models.TextField(verbose_name='Observaciones', blank=True, null=True)
    
    def __str__(self):
        # Lista de campos a mostrar en el formato
        campos = [self.nombre, self.dependencia, self.periodo]

        # Filtra los campos que no son None o están vacíos
        campos_filtrados = [campo for campo in campos if campo not in (None, '', 'NULL')]

        # Concatena los campos filtrados en el formato
        return ', '.join(map(str, campos_filtrados))
    
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'experiencia_laboral'
        ordering = ['id']

# Modelo cargos de elección popular.
class CargosPopulares(models.Model): 
    nombre = models.TextField(verbose_name='Descripción del cargo', blank=True, null=True)
    detalles = models.CharField(max_length=1024, null=True, blank=True, verbose_name='Detalles')
    periodo = models.CharField(max_length=255, blank=True, null=True, verbose_name='Periodo')
    observaciones = models.TextField(verbose_name='Observaciones', blank=True, null=True)
    
    def __str__(self):
        # Lista de campos a mostrar en el formato
        campos = [self.nombre, self.detalles, self.periodo]

        # Filtra los campos que no son None o están vacíos
        campos_filtrados = [campo for campo in campos if campo not in (None, '', 'NULL')]

        # Concatena los campos filtrados en el formato
        return ', '.join(map(str, campos_filtrados))
    
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'cargo_popular'
        ordering = ['id']

#Model Municipio
class Municipio(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre de Municipio')
    
    def __str__(self):
        return self.nombre 
    
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'municipio'
        verbose_name_plural = 'municipios'
        ordering = ['id']

#MODEL DISTRITOS LOCALES EDOMEX
class Distrito_local(models.Model):
    nombre = models.CharField(max_length=255, null=True, blank=True, verbose_name='Distrito Local')
    municipios_rango = models.PositiveIntegerField(null=True, blank=True, verbose_name='Municipios que abarca', default='1')
        
    def __str__(self):
        return self.nombre
        
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'distrito local'
        verbose_name_plural = 'distritos locales'
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
        verbose_name = 'cabecera'
        verbose_name_plural = 'cabeceras'
        ordering = ['id']

#MODEL DISTRITOS FEDERALES EDOMEX
class Distrito_federal(models.Model):
    nombre = models.CharField(max_length=255, null=True, blank=True, verbose_name='Distrito Federal')
    municipios_rango = models.PositiveIntegerField(null=True, blank=True, verbose_name='Municipios que abarca', default='1')
        
    def __str__(self):
        return self.nombre
        
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'distrito federal'
        verbose_name_plural = 'distritos federales'
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
        verbose_name = 'distrito federal municipio'
        verbose_name_plural = 'distritos federales municipios'
        ordering = ['id']

#Model Partido
class Partido(models.Model):
    nombre = models.CharField(max_length=255, null=True, blank=True, verbose_name='Nombre partido')
    siglas = models.CharField(max_length=100, blank=True, null=True, verbose_name='Siglas Partido', choices=partido_siglas_choices, default='PAN')
    foto = models.ImageField(blank=True, null=True, upload_to='partido/fotos', verbose_name='Imagen Partido')
        
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
        verbose_name = 'partido_fichas'
        ordering = ['id']      

# Modelo Líder.
class Lider(models.Model): 
    nombre = models.CharField(max_length=255, verbose_name='Nombre(s)')
    apaterno = models.CharField(max_length=255, verbose_name='Apellido Paterno')
    amaterno = models.CharField(max_length=255, verbose_name='Apellido Materno')
    candidato_activo = models.BooleanField(default=False, verbose_name="Candidato activo")
    tipo_contendiente = models.CharField(max_length=50, blank=True, null=True, verbose_name='Tipo de contendiente', choices=tipo_contendiente_choices)
    periodo_electoral = models.CharField(max_length=25, blank=True, null=True, verbose_name='Periodo Electoral', choices=periodo_electoral_choices, default='2025 - 2027')
    municipio = models.ForeignKey(Municipio, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Municipio Electoral')
    partido = models.ForeignKey(Partido, on_delete=models.SET_NULL, blank=True, null=True)
    protesta = models.CharField(max_length=50, blank=True, null=True, verbose_name='Ha tomado protesta', choices=protesta_choices, default='SI')
    distrito_local = models.ForeignKey(Distrito_local, on_delete=models.SET_NULL, blank=True, null=True)
    distrito_federal = models.ForeignKey(Distrito_federal, on_delete=models.SET_NULL, blank=True, null=True)
    fecha_nacimiento = models.TextField(verbose_name='Fecha de Nacimiento')
    lugar_nacimiento = models.CharField(max_length=510, blank=True, null=True, verbose_name='Lugar de Nacimiento')
    nacionalidad = models.CharField(max_length=10, blank=True, null=True, verbose_name='Nacionalidad')
    zona_influencia = models.CharField(max_length=500, verbose_name='Zona de Influencia')
    alias = models.CharField(max_length=255, blank=True, null=True, verbose_name='Alias')
    sexo = models.CharField(max_length=50, blank=True, null=True, verbose_name='Sexo', choices=sexo_choices, default='No definido')
    estado_civil = models.CharField(max_length=50, blank=True, null=True, verbose_name='Estado Civíl', choices=estado_civil_choices, default='Soltero')
    rfc = models.CharField(max_length=13, blank=True, null=True, verbose_name='RFC')
    curp = models.CharField(max_length=18, null=True, verbose_name='CURP', unique=True)
    domicilios = models.ManyToManyField(Domicilios, verbose_name='Domicilios', blank=True)
    #domicilio_particular = models.TextField(null=True, blank=True, verbose_name='Domicilio Particular')
    telefono_particular = models.CharField(max_length=20, blank=True, null=True, verbose_name='Teléfono Particular')
    domicilio_laboral = models.TextField(null=True, blank=True, verbose_name='Domicilio Laboral')
    telefono_trabajo = models.CharField(max_length=20, blank=True, null=True, verbose_name='Teléfono Trabajo')
    correo = models.EmailField(max_length=255, blank=True, null=True, verbose_name='Correo Electrónico')
    facebook = models.CharField(max_length=255, blank=True, null=True, verbose_name='Facebook')
    instagram = models.CharField(max_length=255, blank=True, null=True, verbose_name='Instagram')
    twitter = models.CharField(max_length=255, blank=True, null=True, verbose_name='Twitter')
    youtube = models.CharField(max_length=255, blank=True, null=True, verbose_name='Canal de youtube')
    formacion_academica = models.CharField(max_length=255, blank=True, null=True, verbose_name='Formación Academica') 
    padres = models.TextField(null=True, blank=True, verbose_name='Padres')
    conyuge = models.TextField(null=True, blank=True, verbose_name='Cónyuge')
    hijos = models.TextField(null=True, blank=True, verbose_name='Hijos')
    otros = models.TextField(null=True, blank=True, verbose_name='Otros Familiares')
    puesto_ocupado = models.CharField(max_length=255, blank=True, null=True, verbose_name='Puesto Ocupado en organización')
    periodo = models.CharField(max_length=255, blank=True, null=True, verbose_name='periodo organización')
    experiencia_laboral = models.ManyToManyField(ExperienciaLaboral, verbose_name='Experiencia Laboral', blank=True)
    cargos_populares = models.ManyToManyField(CargosPopulares, verbose_name='Cargos de elección popular', blank=True)
    # antecedentes_laborales = models.CharField(max_length=1024, blank=True, null=True, verbose_name='Antecedentes Laborales "Empresa o Dependencia"')
    # puesto_ocupado_laboral = models.CharField(max_length=255, blank=True, null=True, verbose_name='Puesto ocupado en empresa o dependencia')
    # periodo_laboral = models.CharField(max_length=255, blank=True, null=True, verbose_name='Periodo laboral en empresa o dependencia ')    
    fuente_ingresos = models.CharField(max_length=255, blank=True, null=True, verbose_name='Fuente de Ingresos')
    comisiones = models.TextField(blank=True, null=True, verbose_name='Comisiones')
    temas_atencion = models.ManyToManyField(TemasAtencion, verbose_name='Temas de atención', blank=True)
    amenazas = models.TextField(blank=True, null=True, verbose_name='Amenazas')
    vehiculos = models.ManyToManyField(Vehiculos, verbose_name='Vehículos', blank=True)
    inmuebles = models.TextField(blank=True, null=True, verbose_name='Inmuebles')
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
    conflictos_organizaciones = models.TextField(blank=True, null=True, verbose_name='Conflictos con organizaciones')
    #puestos_eleccion_popular = models.TextField(blank=True, null=True, verbose_name='Puestos de Elección Popular')
    poder_convocatoria = models.CharField(max_length=20, blank=True, null=True, verbose_name='Poder de convocatoria', choices=convocatoria_choices, default='Bajo' )
    capacidad_convocatoria = models.TextField(blank=True, null=True, verbose_name='Capacidad de convocatoria')
    imagen_publica = models.TextField(blank=True, null=True, verbose_name='Imágen Pública')
    foto = models.ImageField(blank=True, null=True, upload_to='persona/fotos', verbose_name='Imagen')
    vulnerabilidades = models.TextField(blank=True, null=True, verbose_name='Vulnerabilidades')
    habilidades = models.TextField(blank=True, null=True, verbose_name='Capacidades o Hábilidades')
    perfil = models.TextField(blank=True, null=True, verbose_name='Perfil')
    riesgo = models.CharField(max_length=20, blank=True, null=True, verbose_name='Riesgo', choices=riesgo_choices, default='Bajo' )
    estatus_ficha = models.CharField(max_length=50, blank=True, null=True, verbose_name='Estatus ficha', choices=estatus_ficha_choices, default='En proceso')
    observaciones_supervisor = models.TextField(max_length=255, null=True, blank=True, verbose_name='Observaciones de supervisor')
    observaciones = models.TextField(blank=True, null=True, verbose_name='Observaciones')
    organizaciones = models.ManyToManyField('Organizacion', verbose_name='Organizaciones', blank=True, related_name='lideres_organizacion')
    eventos = models.ManyToManyField(Evento, verbose_name='Eventos', blank=True, related_name='lideres_evento')
        
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lider_user')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, verbose_name='Estado')

    def __str__(self):
        return '{} {} {}'.format(self.nombre, self.apaterno, self.amaterno)

    def get_user(self):
        return '{}'.format(self.user)

    def get_full_name(self):
        return '{} {} {}'.format(self.nombre, self.apaterno, self.amaterno)
    
    def get_org(self):
        for i in self.organizaciones.all():
            return '{}'.format(i)
    
    def get_eventos(self):
        return '{}'.format(self.eventos)
    
    def get_vehiculos(self):
        return '{}'.format(self.vehiculos)
    
    def get_domicilios(self):
        return '{}'.format(self.domicilios)
    
    def get_temas(self):
        return '{}'.format(self.temas_atencion)
    
    def get_experiencia(self):
        return '{}'.format(self.experiencia_laboral)
    
    def get_cargo(self):
        return '{}'.format(self.cargos_populares)
    
    def toJSON(self):
        item = model_to_dict(self)
        item['foto'] = self.get_image()
        item['full_name'] = self.get_full_name()
        item['created'] = self.created.strftime('%Y-%m-%d')
        item['modified'] = self.modified.strftime('%d-%m-%Y %H:%M:%S')
        item['usuario'] = self.get_user()
        item['organizaciones'] = self.get_org()
        item['eventos'] = self.get_eventos()
        item['domicilios'] = self.get_domicilios()
        item['temas_atencion'] = self.get_temas()
        item['vehiculos'] = self.get_vehiculos()
        item['experiencia_laboral'] = self.get_experiencia()
        item['cargos_populares'] = self.get_cargo()
        return item

    def get_image(self):
        if self.foto:
            return '{}{}'.format(MEDIA_URL, self.foto)
        return '{}{}'.format(STATIC_URL, 'img/user1.png')

    #MAYÚSCULAS
    def save(self):
        self.nombre = self.nombre.upper()
        self.apaterno = self.apaterno.upper()
        self.amaterno = self.amaterno.upper()
        self.zona_influencia = self.zona_influencia.upper()
        super(Lider, self).save()
    
    # CALCULAR EDAD
    def calcular_edad(self):
        fecha_nacimiento = dt.strptime(self.fecha_nacimiento, "%Y-%m-%d").date()
        hoy = dt.now().date()

        edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        return edad

    class Meta:
        verbose_name = 'Lider'
        verbose_name_plural = 'Lideres'
        ordering = ['id']

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
    situacion_actual = models.TextField(blank=True, null=True, verbose_name='Situación Actual')
    integrantes_numero = models.PositiveIntegerField(null=True, blank=True, verbose_name='Número de Integrantes', default='1')    
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
    lideres = models.ManyToManyField(Lider, verbose_name='Líderes', blank=True, related_name='organizacion_lideres')
    integrantes_nombres = models.ManyToManyField(Integrantes, verbose_name='Integrantes', blank=True, related_name='organizacion_integrantes')
    eventos = models.ManyToManyField(Evento, verbose_name='Eventos', blank=True, related_name='organizacion_evento')
      
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organizacion_lider')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, verbose_name='Estado')

    def __str__(self):
        return self.nombre
    
    def get_user(self):
        return '{}'.format(self.user)
    
    def get_integrantes_nombres(self):
        return '{}'.format(self.integrantes_nombres)
    
    def get_lideres(self):
        return '{}'.format(self.lideres)
    
    def get_eventos(self):
        return '{}'.format(self.eventos)

    def toJSON(self):
        item = model_to_dict(self)
        item['foto'] = self.get_image()
        item['modified'] = self.modified.strftime('%Y-%m-%d %H:%M:%S')
        item['fecha_creacion'] = self.fecha_creacion.strftime('%Y-%m-%d')
        item['usuario'] = self.get_user()
        item['lideres'] =self.get_lideres()
        item['integrantes_nombres'] =self.get_integrantes_nombres()
        item['eventos'] = self.get_eventos()
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


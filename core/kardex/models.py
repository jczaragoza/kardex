from django.db import models
from django.forms.models import model_to_dict
from config.settings import MEDIA_URL, STATIC_URL
from smart_selects.db_fields import ChainedForeignKey

from core.kardex.choices import *
from core.user.models import *
from datetime import date, datetime

#Models combo Unidad ADministrativa
class Unidad_administrativa(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre de Unidad Administrativa')

    def __str__(self):
        return self.nombre

    #MAYÚSCULAS
    def save(self):
        self.nombre = self.nombre.upper()
        super(Unidad_administrativa, self).save()

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'unidad administrativa'
        ordering = ['id']

class Adscripcion(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre de Adscripción')
    unidad_administrativa = models.ForeignKey(Unidad_administrativa, on_delete=models.CASCADE, verbose_name='Unidad Administrativa')
    
    def __str__(self):
        return self.nombre
    
    #MAYÚSCULAS
    def save(self):
        self.nombre = self.nombre.upper()
        super(Adscripcion, self).save()

    def toJSON(self):
        item = model_to_dict(self)
        item['unidad_administrativa'] = self.unidad_administrativa.toJSON()
        return item

    class Meta:
        verbose_name = 'Adscripción'
        ordering = ['id']

class Direccion(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre de Dirección')
    adscripcion = models.ForeignKey(Adscripcion, on_delete=models.CASCADE, verbose_name='Adscripción')
    
    def __str__(self):
        return self.nombre

    #MAYÚSCULAS
    def save(self):
        self.nombre = self.nombre.upper()
        super(Direccion, self).save()

    def toJSON(self):
        item = model_to_dict(self)
        item['direccion'] = self.adscripcion.toJSON()
        return item

    class Meta:
        verbose_name = 'Dirección'
        ordering = ['id']

class Subdireccion(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre de Subdirección')
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, verbose_name='Dirección')
    
    def __str__(self):
        return self.nombre
    #MAYUS
    def save(self):
        self.nombre = self.nombre.upper()
        super(Subdireccion, self).save()
    
    def toJSON(self):
        item = model_to_dict(self)
        item['direccion'] = self.direccion.toJSON()
        return item
    class Meta:
        verbose_name = 'Subdireccion'
        ordering = ['id']

class Departamento(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre del departamento')
    subdireccion = models.ForeignKey(Subdireccion, on_delete=models.CASCADE, verbose_name='Subdirección')
        
    def __str__(self):
        return self.nombre 

    def save(self):
        self.nombre = self.nombre.upper()
        super(Departamento, self).save()
    
    def toJSON(self):
        item = model_to_dict(self)
        item['subdireccion'] = self.subdireccion.toJSON()
        return item
    
    class Meta:
        verbose_name = 'Departamento'
        ordering = ['id']

#Model Municipio
class Municipio(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre de Municipio')
    
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

class Colonia(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre de Colonia')
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, verbose_name='Municipio')
    
    def __str__(self):
        return self.nombre 
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Colonia, self).save()

    def toJSON(self):
        item = model_to_dict(self)
        item['municipio'] = self.municipio.toJSON()
        return item

    class Meta:
        verbose_name = 'Colonia'
        ordering = ['id']

#Puesto
class Puestos(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True, verbose_name='Nombre de Puesto')
    codigo_puesto = models.CharField(max_length=255, blank=True, null=True, verbose_name='Código de Puesto')
    nivel_rango = models.CharField(max_length=255, null=True, blank=True, verbose_name='Nivel del Puesto')
    sueldo_bruto = models.DecimalField(default=00.00, max_digits=20, decimal_places=2, verbose_name='Sueldo Bruto')
    sueldo_neto = models.DecimalField(default=00.00, max_digits=20, decimal_places=2, verbose_name='Sueldo Neto')
    
    def __str__(self):
        return self.nombre 
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Puestos, self).save()
    
    def toJSON(self):
        item = model_to_dict(self)
        item['sueldo_bruto'] = format(self.sueldo_bruto, '.2f')
        item['sueldo_neto'] = format(self.sueldo_neto, '.2f')
        return item
    
    class Meta:
        verbose_name = 'Puesto'
        ordering = ['id']

# model Persona.
class Persona(models.Model): 
    nombre = models.CharField(max_length=255, verbose_name='Nombre(s)')
    apaterno = models.CharField(max_length=255, verbose_name='Apellido Paterno')
    amaterno = models.CharField(max_length=255, verbose_name='Apellido Materno')
    clavesp = models.CharField(max_length=9, blank=True, null=True, verbose_name = 'Clave SP', unique=True)
    rfc = models.CharField(max_length=13, blank=True, null=True, verbose_name='RFC', unique=True)
    fecha_alta = models.DateField(verbose_name='Fecha de Alta')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de Nacimiento')
    estatus = models.CharField(max_length=20, blank=True, null=True, verbose_name='Estatus', choices=estatus_choices, default='Activo')
    foto = models.ImageField(blank=True, null=True, upload_to='persona/fotos', verbose_name='Imagen')
    puesto = models.ForeignKey(Puestos, on_delete=models.SET_NULL, null=True)
    num_plaza = models.CharField(max_length=20, blank=True, null=True, verbose_name='Número de Plaza')
    cuip = models.CharField(max_length=20, null=True, blank=True, verbose_name='CUIP')
    curp = models.CharField(max_length=18, null=True, verbose_name='CURP')
    unidad_administrativa = models.ForeignKey(Unidad_administrativa, on_delete=models.SET_NULL, blank=True, null=True)
    adscripcion = ChainedForeignKey(
        Adscripcion,
        on_delete=models.SET_NULL,
        chained_field="unidad_administrativa",
        chained_model_field="unidad_administrativa",
        show_all=False,
        auto_choose=True,
        sort=True,
        blank=True,
        null=True
    )
    direccion = ChainedForeignKey(
        Direccion,
        on_delete=models.SET_NULL,
        chained_field="adscripcion",
        chained_model_field="adscripcion",
        show_all=False,
        auto_choose=True,
        sort=True,
        blank=True,
        null=True

    )
    subdireccion = ChainedForeignKey(
        Subdireccion,
        on_delete=models.SET_NULL,
        chained_field="direccion",
        chained_model_field="direccion",
        show_all=False,
        auto_choose=True,
        sort=True,
        blank=True,
        null=True
    )
    departamento = ChainedForeignKey(
        Departamento,
        on_delete= models.SET_NULL,
        chained_field="subdireccion",
        chained_model_field="subdireccion",
        show_all=False,
        auto_choose=True,
        sort=True,
        blank=True,
        null=True
        
    )

    calle = models.CharField(max_length=255, null=True, blank=True, verbose_name='Domicilio del personal (Calle)')
    exterior = models.CharField(max_length=10, null=True, blank=True, verbose_name='Número ')
    interior = models.CharField(max_length=10, null=True, blank=True, verbose_name='Interior')
    municipio =models.ForeignKey(Municipio, on_delete=models.SET_NULL, blank=True, null=True)
    colonia = ChainedForeignKey(
        Colonia,
        chained_field="municipio",
        chained_model_field="municipio", 
        show_all=False,
        auto_choose=True,
        sort=True,
        blank=True,
        null=True
    )
    cp = models.CharField(max_length=5, blank=True, null=True, verbose_name='Código Postal')
    correo = models.EmailField(max_length=50, blank=True, null=True, verbose_name='Correo Electrónico')
    telefono_fijo = models.CharField(max_length=20, blank=True, null=True, verbose_name='Teléfono Fijo')
    telefono_movil = models.CharField(max_length=20, blank=True, null=True, verbose_name='Teléfono Móvil')
    contacto_familiar = models.CharField(max_length=255, blank=True, null=True, verbose_name='Contacto Familiar (Nombre)')
    numero_contacto_familiar = models.CharField(max_length=255, blank=True, null=True, verbose_name='Contacto Familiar (Número Telefónico)')
    nss = models.CharField(max_length=10, null=True, blank=True, verbose_name='ISSEMYM')
    tipo_sangre = models.CharField(max_length=5, null=True, blank=True, verbose_name='Tipo de Sangre', choices=tipo_sangre_choices, default='O+') 
    escolaridad = models.CharField(max_length=255, null=True, blank=True, verbose_name= 'Último Grado de Estudios', choices=ultimo_grado_estudios, default='Licenciatura Completa')
    observaciones = models.CharField(max_length=255, null=True, blank=True, verbose_name='Observaciones')
    #fecha_baja = models.DateField(verbose_name='Fecha de Baja', blank=True, null=True)
    motivo_baja = models.CharField(max_length=255, null=True, blank=True, verbose_name='Fecha y Motivo de Baja')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    
    def get_full_name(self):
        return '{} {} {}'.format(self.nombre, self.apaterno, self.amaterno)

    def get_puesto(self):
        return '{}'.format(self.puesto.nombre)

    def get_adscripcion(self):
        return '{}'.format(self.adscripcion)


    def toJSON(self):
        item = model_to_dict(self)
        item['full_name'] = self.get_full_name()
        item['fecha_alta'] = self.fecha_alta.strftime('%Y-%m-%d')
        item['foto'] = self.get_image()
        item['fecha_nacimiento'] = self.fecha_nacimiento.strftime('%Y-%m-%d')
        item['modified'] = self.modified.strftime('%Y-%m-%d')
        item['full_puesto'] = self.get_puesto()
        item['adscripcion'] = self.get_adscripcion()
        #item['fecha_baja'] = self.fecha_baja.strftime('%Y-%m-%d')     
        return item

    def get_image(self):
        if self.foto:
            return '{}{}'.format(MEDIA_URL, self.foto)
        return '{}{}'.format(STATIC_URL, 'img/user1.png')

    def __str__(self):
        return self.get_full_name()
    
    def get_edad(self):
        today = date.today()
        return today.year - self.fecha_nacimiento.year - ((today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ['id']

    #MAYÚSCULAS
    def save(self):
        self.nombre = self.nombre.upper()
        self.apaterno = self.apaterno.upper()
        self.amaterno = self.amaterno.upper()
        self.rfc = self.rfc.upper()
        self.curp = self.curp.upper()
        super(Persona, self).save()

# Cursos model.
class Cursos(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Personal DGI')
    nombre = models.CharField(max_length=255, null=True, blank=True, verbose_name='Curso')
    horas = models.PositiveIntegerField(null=True, blank=True, verbose_name='Duración (Horas)', default='1')
    tipo_curso = models.CharField(max_length=100, blank=True, null=True, verbose_name='Tipo de curso', choices=cursos_choices, default='Curso')
    documento = models.CharField(max_length=20, blank=True, null=True, verbose_name='Documento Obtenido', choices=docs_choices, default='Constancia')
    institucion = models.CharField(max_length=255, blank=True, null=True, verbose_name='Institución que imparte')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre
    
    #MAYÚSCULAS
    def save(self):
        self.nombre = self.nombre.upper()
        super(Cursos, self).save()

    def toJSON(self):
        item = model_to_dict(self)
        item['persona_nombre'] = '{} {} {}'.format(self.persona.nombre, self.persona.apaterno, self.persona.amaterno)
        return item

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['id']

# Modelo Arma.
class Armas(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Personal DGI')
    matricula = models.CharField(max_length=255, verbose_name='Matrícula', unique=True)
    clase = models.CharField(max_length=255, null=True, blank=True, verbose_name='Clase', choices=clase_choices, default='ESCOPETA')
    marca = models.CharField(max_length=255, null=True, blank=True, verbose_name='Marca', choices=marca_arma_choices, default='COLT')
    calibre = models.CharField(max_length=255, null=True, blank=True, verbose_name='Calibre', choices=calibre_choices, default='38')
    modelo = models.CharField(max_length=255, null=True, blank=True, verbose_name='Modelo')
    resguardo = models.CharField(max_length=255, verbose_name='No de resguardo', unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return self.matricula
    
    #MAYÚSCULAS
    def save(self):
        self.matricula= self.matricula.upper()
        self.resguardo= self.resguardo.upper()
        super(Armas, self).save()

    def toJSON(self):
        item = model_to_dict(self)
        item['persona_nombre'] = '{} {} {} / {}'.format(self.persona.nombre, self.persona.apaterno, self.persona.amaterno, self.resguardo)
        return item

    class Meta:
        verbose_name = 'Arma'
        verbose_name_plural = 'Armas'
        ordering = ['id']

# Modelo Vehículo.
class Vehiculos(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Personal DGI')
    matricula = models.CharField(max_length=255, verbose_name='Matricula', unique=True)
    marca = models.CharField(max_length=255, null=True, blank=True, verbose_name='Marca')
    marca = models.CharField(max_length=255, null=True, blank=True, verbose_name='Marca de Vehículo', choices=vehiculos_choices, default='VOLKSWAGEN') 
    submarca = models.CharField(max_length=255, null=True, blank=True, verbose_name='Submarca')
    tipo = models.CharField(max_length=255, null=True, blank=True, verbose_name='Tipo', choices=tipo_vehiculo, default='SEDAN' )
    modelo = models.CharField(max_length=255, null=True, blank=True, verbose_name='Modelo del Vehículo', choices=modelo_choices, default='2011' )
    color = models.CharField(max_length=255, null=True, blank=True, verbose_name='Color')
    motor = models.CharField(max_length=255, null=True, blank=True, verbose_name='Número de Motor', unique=True)
    serie = models.CharField(max_length=255, null=True, blank=True, verbose_name='Número de Serie', unique=True)
    resguardo = models.CharField(max_length=255, null=True, blank=True, verbose_name='No de resguardo')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return self.identificador
    
    #MAYÚSCULAS
    def save(self):
        self.submarca = self.submarca.upper()
        self.color = self.color.upper()
        self.matricula = self.matricula.upper()
        self.submarca = self.submarca.upper()
        self.resguardo = self.resguardo.upper()

        super(Vehiculos, self).save()

    def toJSON(self):
        item = model_to_dict(self)
        item['persona_nombre'] = '{} {} {} / {}'.format(self.persona.nombre, self.persona.apaterno, self.persona.amaterno, self.resguardo)
        return item

    class Meta:
        verbose_name = 'Vehículo'
        verbose_name_plural = 'Vehículos'
        ordering = ['id']

# Modelo Kardex
class Kardex(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, null=True, blank=True)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, null=True, blank=True)
    fecha_actual = models.DateField(default=datetime.now, null=True, blank=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.curso.nombre

    def toJSON(self):
        item = model_to_dict(self)
        item['curso'] = self.curso.toJSON()
        item['persona'] = self.persona.toJSON()
        item['modified'] = self.modified.strftime('%Y-%m-%d - %H: %M')

        return item

    class Meta:
        verbose_name = 'Kardex'
        ordering = ['id']

# model Bienes
class Bienes(models.Model): 
    categoria = models.CharField(max_length=255, verbose_name='Categoría')
    descripcion = models.TextField(null=True, blank=True, verbose_name='Descripcion del bien')
    resguardo = models.TextField(null=True, blank=True, verbose_name='Número de resguardo')
    resguardatario = models.ForeignKey(Persona, on_delete=models.CASCADE)
    usuario = models.CharField(max_length = 255, null=True, blank=True)
    estatus_bien = models.TextField(blank=True, null=True, verbose_name='Estatus del bien', choices=estatus_bien, default='Activo')
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.categoria

    def toJSON(self):
        item = model_to_dict(self)
        item['resguardatario'] = '{} {} {}'.format(self.resguardatario.nombre, self.resguardatario.apaterno, self.resguardatario.amaterno)
        item['modified'] = self.modified.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = 'Bien'
        verbose_name_plural = 'Bienes'
        ordering = ['id']

    #MAYÚSCULAS
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Bienes, self).save()


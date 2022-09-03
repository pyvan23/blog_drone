from django.db import models
from ckeditor.fields import RichTextField

class Categoria(models.Model):
    """ Modelo Categoría
        Método str devuelve solo el nombre de la categoría
    """
    nombre = models.CharField('Nombre de la Categoría', max_length=100, null=False, blank=False)
    estado = models.BooleanField('Categoría Activa / No Activa', default=True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)

    class Meta:
        """Correcta visualización de los campos en panel admin, en singular y plural
        """
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return str(self.nombre)

class Autor(models.Model):
    """ Modelo Autor
        Método str devuelve solo el nombre del autor
    """
    nombres = models.CharField('Nombres del Autor', max_length=255, null=False, blank=False)
    apellidos = models.CharField('Apellidos del Autor', max_length=255, null=False, blank=False)
    facebook = models.URLField('Facebook', null=True, blank=True)
    twitter = models.URLField('Twitter', null=True, blank=True)
    instagram = models.URLField('Instagram', null=True, blank=True)
    web = models.URLField('Web', null=True, blank=True)
    correo = models.EmailField('Correo Electrónico', null=False, blank=False)
    estado = models.BooleanField('Autor Activo / No Activo', default=True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)

    class Meta:
        """Correcta visualización de los campos en panel admin, en singular y plural
        """
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return str(self.nombres)

class Post(models.Model):
    """ Modelo Post
    """
    titulo = models.CharField('Título', max_length=90, blank=False, null=False)
    slug = models.CharField('Slug', max_length=100, blank=False, null=False)
    descripcion = models.CharField('Descripción', max_length=110, blank=False, null=False)
    contenido = RichTextField()
    imagen = models.URLField(max_length=999, blank=False, null=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.BooleanField('Publicado / No Publicado', default=True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)

    class Meta:
        """Correcta visualización de los campos en panel admin, en singular y plural
        """
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return str(self.titulo)

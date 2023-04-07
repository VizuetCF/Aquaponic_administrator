from django.db import models

# Create your models here.

'''
El modelo debe tener la siguiente estructura:

Normalización:

Capítulos: Capitulo 1, Capitulo 2, etc.
Subcapitulo: Subcapítulo 1, Subcapítulo 2, etc.
Contenido: Content
'''

'''
Crear la fecha del modelo
'''
class Manual_chapter(models.Model):
    Chapter_id =models.AutoField(primary_key=True)
    Chapter_name = models.CharField(max_length=50)
    # Date = models.Date()
    
    def __str__(self):
        return self.name
    
class Manual_sub_chapter(models.Model):
    Sub_chapter_id =models.AutoField(primary_key=True)
    Chapter = models.ForeignKey(Manual_chapter, on_delete=models.CASCADE)
    Sub_chapter_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
'''
Agregar las imagenes principales y las secundarias
'''
class Manual_sub_chapter_content(models.Model):
    Sub_chapter = models.ForeignKey(Manual_sub_chapter, on_delete=models.CASCADE)
    Content = models.TextField(max_length=500)
    # Principal_image = models.Imagefield()
    # Secund_images = models.Imagefield()
    
    def __str__(self):
        return self.name
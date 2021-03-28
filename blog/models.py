from django.db import models #se agregan cosas de otros archivos
from django.utils import timezone


#definición de nuestro modelo (es un objeto)
#Post es el nombre de nuestro modelo, siempre empezar en letra mayuscula
#models.Model significa que Post en un modelo de Django para guardarlo en la BD
#INFO DE CAMPOS: https://docs.djangoproject.com/en/2.2/ref/models/fields/#field-types

class Post(models.Model): 
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
from django.contrib import admin
from .models import Post 

admin.site.register(Post) #hacemos visible pagina al administrador, así que registramos el modelo

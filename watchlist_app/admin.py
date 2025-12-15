from django.contrib import admin
# APP MODELS
from watchlist_app.models import Movie

# Register your models here.

# Registering our model, in order to use make queries using Djang Admin Panel
admin.site.register(Movie)
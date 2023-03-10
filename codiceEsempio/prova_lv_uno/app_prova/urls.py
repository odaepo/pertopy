from django.urls import path

from .views import chi_siamo, contatti

urlpatterns = [
    path('chi_siamo/', chi_siamo, name='chi_siamo'),
    path('contattaci/', contatti, name='contatti')
]

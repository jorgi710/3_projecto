from django.urls import path
from .views import CalHome, CalSuma, CalResultado
app_name = 'cal'

urlpatterns = [ 
    path('', CalHome.as_view(), name='home'),
    path('suma/', CalSuma.as_view(), name='suma'),
    path('suma/resultado/', CalResultado.as_view(), name='resultado'),

]

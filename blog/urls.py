from django.urls import path
from .views import BlogHome, BlogNosotros, BlogServicios
app_name = 'blog'

urlpatterns = [ 
    path('', BlogHome.as_view(), name='home'),
    path('nosotros/', BlogNosotros.as_view(), name='nosotros'),
    path('servicios/', BlogServicios.as_view(), name='servicios'),
]

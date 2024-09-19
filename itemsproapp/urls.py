from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('solicitudesAdmin/', views.solicitudes, name='solicitudes'),
    path('', views.home, name='home'),
    path('home_admin', views.home_admin, name='home_admin'),
    path('home_cliente/', views.home_cliente, name='home_cliente'),
    path('contacto/', views.contacto, name='contacto'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('usuarios/crearCliente/', views.crear, name='crear_cliente'),
    path('usuarios/editar/<int:id>/', views.editar, name='editar_usuario'),
    path('borrar/<int:id>/', views.borrar, name='borrar_usuario'),
    path('productos/', views.productos, name='productos'),
    path('productos/crearProd/', views.crearProd, name='crear_prod'),
    path('productos/editarProd/<int:idProd>/', views.editarProd, name='editar_prod'),
    path('borrarProd/<int:idProd>/', views.borrarProd, name='borrar_prod'),
    path('salir/', views.salir, name='salir'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('clientes/', views.clientes, name='clientes'),
    path('prodClient/', views.prodClient, name='prodClient'),
    path('soldClient/', views.soldClient, name='soldClient'),
    path('solicitudesAdmin/agregar.html', views.crearSold, name='crear_sold'),
    path('solicitudesAdmin/editarSold.html/<int:idSold>/', views.editarSold, name='editar_sold'),
    path('soldProd/<int:idSold>/', views.borrarSold, name='borrar_sold'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

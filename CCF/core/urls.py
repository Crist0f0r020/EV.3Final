from django.urls import path
from .views import index, carrito, computador, notebook, login, registro, indexadmin, save_productos
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns=[
    path('', index, name="index"),
    path('carrito/', carrito, name="carrito"),
    path('computador/', computador, name="computador"),
    path('notebook/', notebook, name="notebook"),
    path('login/', login, name="login"),
    path('registro/', registro, name="registro"),
    path('loginn/', LoginView.as_view(template_name="core/admin/loginn.html"), name="loginn"),
    path('logout/', LogoutView.as_view(template_name="core/index.html"), name="logout"),
    path('indexadmin/', indexadmin, name="indexadmin"),
    path('save_productos', save_productos, name='save_productos')
]
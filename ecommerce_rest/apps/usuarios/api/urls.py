from django.urls import path
#from apps.usuarios.api.api import  UsuarioAPIView
from apps.usuarios.api.api import usuario_api_view
from apps.usuarios.api.api import usuario_detalle_view
urlpatterns=[
    # name (Opcional)

    #path('usuarios/', UsuarioAPIView.as_view(), name = 'usuario_api')
    path('usuarios/', usuario_api_view, name = 'usuario_api'),
    path('usuarios/<int:pk>', usuario_detalle_view, name = 'usuario_detalle_api_view')
]
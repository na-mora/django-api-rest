from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.usuarios.models import User
from apps.usuarios.api.serializers import UserSerializer

#class UsuarioAPIView(APIView):

#    def get(self, request):
        # Devuelve un listado
#        usuarios = User.objects.all()
        # Infomacion de la consulta ya serializada (json)
#        usuarios_serializers = UserSerializer(usuarios, many = True)
#        return Response(usuarios_serializers.data)

@api_view(['GET', 'POST', 'DELETE'])
def usuario_api_view(request):

    if request.method == 'GET':
        usuarios = User.objects.all()
        usuarios_serializers = UserSerializer(usuarios, many = True)
        return Response(usuarios_serializers.data)

    elif request.method == 'POST':
        # Permiten tambien validar (Deserializa)
        usuario_serializado = UserSerializer(data = request.data)
        if usuario_serializado.is_valid():
            usuario_serializado.save()
            return Response(usuario_serializado.data)
        return Response(usuario_serializado.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def usuario_detalle_view(request, pk=None):

    if request.method == 'GET':
        buscar = User.objects.filter(id = pk).first()
        usuario_serializado = UserSerializer(buscar)
        return Response(usuario_serializado.data)

    elif request.method == 'PUT':
        buscar = User.objects.filter(id = pk).first()
        usuario_serializado = UserSerializer(buscar, data = request.data )
        if usuario_serializado.is_valid():
            usuario_serializado.save()
            return Response(usuario_serializado.data)
        return Response(usuario_serializado.errors)

    elif request.method == 'DELETE':
        buscar = User.objects.filter(id = pk).first()
        buscar.delete()
        return Response('Eliminado')




        


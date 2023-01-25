
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


from profile_api import serializers
from profile_api import models
from profile_api import permissions
class HelloApiView(APIView):
    """ Test API View"""
    serializers_class =serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView  features"""
        an_apiview = [
            'Uses HTTP methods as funtions (get,post,patch,put,delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})


    def post(self,request):
        """Create a hello message with our name"""
        serializers = self.serializers_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk=None):
        """Handle an update an object"""
        return Response({'method':'put'})


    def patch(self,request, pk=None):
        """Handle a partial update of an objects"""
        return({'method': 'patch'})


    def delete(self,repones,pk=None):
        """delete an object"""
        return Response({'method':'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializers_class=serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""

        a_viewset =[
         'Uses actions (list,create,retrive,update,partial_update)',
         'automatically maps to urls using routers',
         'provides more funtionality with low cost '
        ]

        return Response({'message':'Hello','a_viewset':a_viewset})

    def create(self,request):
        """create a new  hello message"""
        serializer = self.serializers_class(data=request.data)

        if serializer.is_vaild():
            name = serializer.validated_data.get('name')
            message = f'Hello{name}!'
            return Response({'massage':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )
    def retrive(self,request, pk=None):
        """Handle getting an object  by its ID"""
        return Response({'HTTP_method':'GET'})

    def update(self,request,pk=None):
        """"Handle update an object"""
        return Response({'http_method':'PUT'})

    def paritial_update(self,request,pk=None):
        """Handle update an object """
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """Handle removing an objectsa"""
        return Response({'HTTP_method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes =(TokenAuthentication,)
    permission_classes =(permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentications tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

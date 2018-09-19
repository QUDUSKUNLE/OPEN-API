from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.settings import api_settings
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView, status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from app.serializers import UserSerializer, ArticlesSerializer, TokenSerializer
from app.permissions import IsOwnerOrReadOnly
from app.models import Articles
from app.models import User


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


# Create your views here.
class UserViewSet(ModelViewSet):
    """UserViewSet Class"""

    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('id')
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    http_method_names = ['get', 'post']


class ArticlesViewSet(ModelViewSet):
    """ArticlesViewSet Class"""

    serializer_class = ArticlesSerializer
    queryset = Articles.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    http_method_names = ['get', 'post', 'put', 'delete']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class LoginViewSet(ViewSet):
    """ checks username and password and return auth token """

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """ Use the ObtainAuthToken APIView to validate and create a token """

        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login saves the user’s ID in the session,
            # using Django’s session framework.
            login(request, user)
            serializer = TokenSerializer(data={
                # using drf jwt utility functions to generate a token
                'token': jwt_encode_handler(
                    jwt_payload_handler(user)
                )})
            serializer.is_valid()

            return Response(serializer.data, message='login successful')
        return Response(
            {"message": "Invalid credentials"},
            status=status.HTTP_401_UNAUTHORIZED
        )

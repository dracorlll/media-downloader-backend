from rest_framework.viewsets import ModelViewSet
from apps.defaultapp.models import Proxy
from apps.defaultapp.serializers.proxy import ProxySerializer


class ProxyViewSet(ModelViewSet):
    # authentication_classes = (SessionAuthentication, TokenAuthentication,)
    queryset = Proxy.objects.all()
    serializer_class = ProxySerializer
    # permission_classes = [permissions.IsAdminUser]

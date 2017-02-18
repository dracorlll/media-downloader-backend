from rest_framework.serializers import ModelSerializer, CharField
from apps.defaultapp.models import Proxy


class ProxySerializer(ModelSerializer):
    ip = CharField(max_length=15)
    port = CharField(max_length=5)
    country = CharField(max_length=5)

    class Meta:
        model = Proxy
        fields = (
            'ip',
            'port',
            'country'
        )

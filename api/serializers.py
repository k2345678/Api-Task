from rest_framework.serializers import ModelSerializer
from .models import *

class DataSerializer(ModelSerializer):
    class Meta:
        model = Data
        fields = "__all__"
from rest_framework import serializers
from ..models import *
from ..models.davomat_model import Davomat,Status


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class DavomatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Davomat
        fields = '__all__'
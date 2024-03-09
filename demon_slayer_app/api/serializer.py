from rest_framework.serializers import ModelSerializer
from ..models import Demon

class DemonSerializer(ModelSerializer):
    class Meta:
        model = Demon
        fields = ['id', 'name', 'race', 'affiliation', 'skill', 'quote']
from dictionary_db.models import *
from rest_framework import serializers

class Dictionary_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Dictionary
        fields = ('__all__')

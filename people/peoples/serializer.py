from rest_framework import serializers
from peoples.models import Person, Parent


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ("__all__")


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ("__all__")

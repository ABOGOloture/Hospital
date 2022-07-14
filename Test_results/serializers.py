from rest_framework import serializers
from .models import PersonalInformation, RenalFunctionTests

class PersonalInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInformation
        fields = '__all__'


class RenalFunctionTestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RenalFunctionTests
        fields = '__all__'
from rest_framework import serializers
from career.models import Leads

# leads serializer
class LeadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leads
        fields = '__all__'

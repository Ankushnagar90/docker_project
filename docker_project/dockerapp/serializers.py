from rest_framework import serializers
from .models import Sum

class SumSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sum
		fields = '__all__'
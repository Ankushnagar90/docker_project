from django.shortcuts import render
from rest_framework import viewsets
from .models import Sum
from .serializers import SumSerializer

# def hello_world(request):
#     return render(request, 'hello_world.html', {})

class SumAPI(viewsets.ModelViewSet):
	queryset = Sum.objects.all().order_by('id')
	serializer_class = SumSerializer

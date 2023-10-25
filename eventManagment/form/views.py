from django.shortcuts import render
from django.http import HttpResponse
from form.models import Event
from form.serializer import BaseFormSerializer
import json
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def get_all_forms(request):
    """
    Function that returns all the forms that exist in the DB
    """
    all_forms = Event.objects.all()
    serializer = BaseFormSerializer(all_forms, many=True)  # Serialize a queryset, so use many=True
    form_data = serializer.data  # Retrieve the serialized data

    return HttpResponse(json.dumps(form_data), content_type='application/json', status=200)


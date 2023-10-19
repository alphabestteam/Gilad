from django.shortcuts import render
from django.http import HttpResponse
from peoples.models import Person
from peoples.serializer import PersonSerializer
import json
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def get_all_people(request):
    """
    Function that returns all the people that exist in the DB
    """
    all_people = Person.objects.all()
    serializer = PersonSerializer(all_people, many=True)  # Serialize a queryset, so use many=True
    people_data = serializer.data  # Retrieve the serialized data

    return HttpResponse(json.dumps(people_data), content_type='application/json', status=200)

@csrf_exempt
def add_person(request):
    """
    function that add person to the DB
    """
    person_data = JSONParser().parse(request)
    serializer_person = PersonSerializer(data=person_data)
    if serializer_person.is_valid():
        person = Person.objects.create(
        name = person_data["name"],
        id = person_data["id"],
        birth_date = person_data["birth_date"],
        city = person_data["city"]
        )
        person.save()
        return HttpResponse(status=status.HTTP_200_OK)

@csrf_exempt
def remove_person(request, id):
    """
    function that delete person from the DB
    """
    person_to_delete = Person.objects.get(pk=id)
    person_to_delete.delete()
    return HttpResponse(status=status.HTTP_200_OK)

@csrf_exempt
def update_person(request):
    """
    Function to update an existing person based on their primary key (pk).
    """
    person_data = JSONParser().parse(request)
    person = get_object_or_404(Person, pk=person_data["id"])

    serializer = PersonSerializer(person, data=person_data, partial=True)

    if serializer.is_valid():
        serializer.save() 
        return HttpResponse(serializer.data, status=status.HTTP_200_OK)
    return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

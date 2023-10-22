from django.http import HttpResponse, JsonResponse
from peoples.models import Person, Parent
from peoples.serializer import PersonSerializer, ParentSerializer
import json
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from datetime import date


# Create your views here.
@csrf_exempt
def get_all_people(request):
    """
    Function that returns all the people that exist in the DB
    """
    all_people = Person.objects.all()
    serializer = PersonSerializer(all_people, many=True)
    people_data = serializer.data

    return HttpResponse(
        json.dumps(people_data), content_type="application/json", status=200
    )


@csrf_exempt
def add_person(request):
    """
    function that add person to the DB
    """
    person_data = JSONParser().parse(request)
    serializer_person = PersonSerializer(data=person_data)
    if serializer_person.is_valid():
        person = Person.objects.create(
            name=person_data["name"],
            id=person_data["id"],
            birth_date=person_data["birth_date"],
            city=person_data["city"],
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


@csrf_exempt
def add_parent(request):
    """
    function that add parent to the DB
    """
    parent_data = JSONParser().parse(request)
    serializer_parent = ParentSerializer(data=parent_data)
    if serializer_parent.is_valid():
        parent = Parent.objects.create(
            name=parent_data["name"],
            id=parent_data["id"],
            birth_date=parent_data["birth_date"],
            city=parent_data["city"],
            work_place=parent_data["work_place"],
            salary=parent_data["salary"],
        )
        parent.save()
        return HttpResponse(status=status.HTTP_200_OK)
    else:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def remove_parent(request, id):
    """
    function that delete parent from the DB
    """
    parent_to_delete = Parent.objects.get(pk=id)
    parent_to_delete.delete()
    return HttpResponse(status=status.HTTP_200_OK)


@csrf_exempt
def update_parent(request):
    """
    Function to update an existing parent based on their primary key (pk).
    """
    parent_data = JSONParser().parse(request)
    parent = get_object_or_404(Parent, pk=parent_data["id"])

    serializer = ParentSerializer(parent, data=parent_data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return HttpResponse(serializer.data, status=status.HTTP_200_OK)
    return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def get_all_parents(request):
    """
    Function that returns all the parents that exist in the DB
    """
    all_parents = Parent.objects.all()
    serializer = ParentSerializer(all_parents, many=True)
    parent_data = serializer.data

    return HttpResponse(
        json.dumps(parent_data), content_type="application/json", status=200
    )


@csrf_exempt
def connect_child_to_parent(request):
    """
    function that get child's id and parent's id
    and connect between them
    """
    data = json.loads(request.body)
    parent_id = data.get("parent_id")
    child_id = data.get("child_id")

    parent = get_object_or_404(Parent, id=parent_id)
    child = get_object_or_404(Person, id=child_id)

    # Add the child to the parent's children
    parent.children.add(child)

    # Return a success response
    return HttpResponse(status=200)


def parent_data(request, id):
    """
    function that return all the data on the parent, and his children
    """
    parent = Parent.objects.get(pk=id)
    parent_serializer = ParentSerializer(parent).data
    children = parent.children.all()
    children_serializer = PersonSerializer(children, many=True).data

    data = {"parent": parent_serializer, "children": children_serializer}

    return JsonResponse(data, status=200)


def rich_children(request):
    """
    function return list of all the rich children in the DB
    """
    rich_parents = Parent.objects.filter(salary__gte=50000)
    rich_children = []
    for parent in rich_parents:
        children = parent.children.all()
        for child in children:
            age = (
                date.today().year
                - child.birth_date
                - (
                    (date.today().month, child.birth_date.day)
                    < (date.today().month, child.birth_date.day)
                )
            )
            if age < 18:
                child_serializer = PersonSerializer(child)
                rich_children.append(child_serializer.data)
    return HttpResponse(rich_children, status=status.HTTP_200_OK)


def parents_of_person(request, id):
    """
    Function to return the parents of a person.
    """
    person = Person.objects.get(pk=id)
    parents = person.parents.all()
    parent_data = [{"name": parent.name, "id": parent.id} for parent in parents]

    return JsonResponse(parent_data, safe=False)


# def get_parents_of_child(request, id):
# child = Person.objects.get(id=id)
# parents = Parent.objects.filter(children=child)
# serializer = ParentSerializer(parents, many=True)
# return Response(serializer.data)

# def get_parents_of_child(request, id):
#     parents_data = [
#         {
#             'name': parent.name,
#             'work_place': parent.work_place,
#             'salary': parent.salary,
#             'children': parent.children.all().values('name', 'birth_date', 'city')
#         }
#         for parent in Parent.objects.all() if id in parent.children.all().values_list('id', flat=True)
#     ]

#     serializer = ParentSerializer(data=parents_data, many=True)
#     if serializer.is_valid():
#         return Response(serializer.validated_data)
#     return Response(serializer.errors, status=400)


def child_data(request, id):
    """
    function that return all the data of the children of the parent
    """
    parent = Parent.objects.get(pk=id)
    children = parent.children.all()
    children_data = [PersonSerializer(child).data for child in children]
    return JsonResponse(children_data, safe=False, status=200)


def grandparents(request, id):
    """
    function that get id of person and return the grandma and grandpa of the person
    """
    person = Person.objects.get(pk=id)

    parents = Parent.objects.filter(children=person.id)
    grandparents_names = []
    for parent in parents:
        grandparents = Parent.objects.filter(children=parent.id)
        grandparents_names.extend([grand.name for grand in grandparents])
    return HttpResponse(grandparents_names, status = status.HTTP_200_OK)



def brothers(request, id):
    """
    function that get person and return all his brothers
    """
    person = Person.objects.get(pk=id)
    parents = list(Parent.objects.filter(children=person.id))
    siblings = []
    for parent in parents:
        kids = parent.children.all()
        for kid in kids:
            if kid.id != person.id:
                siblings.append(kid.name)
    return HttpResponse(siblings, status = status.HTTP_200_OK)

from django.urls import path
from . import views

urlpatterns = [
    path('people/getAllPeople', views.get_all_people),
    path('people/addPerson', views.add_person),
    path('people/removePerson/<int:id>/', views.remove_person),
    path('people/updatePerson', views.update_person),

]
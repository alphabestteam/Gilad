from django.urls import path
from . import views

urlpatterns = [
    path('people/getAllPeople', views.get_all_people),
    path('people/addPerson', views.add_person),
    path('people/removePerson/<int:id>/', views.remove_person),
    path('people/updatePerson', views.update_person),
    path('people/addParent', views.add_parent),
    path('people/removeParent/<int:id>/', views.remove_parent),
    path('people/updateParent', views.update_parent),
    path('people/getAllParents', views.get_all_parents),
    path('people/connectChildToParent', views.connect_child_to_parent),
    path('people/parentData/<int:id>/', views.parent_data),
    path('people/richChildren', views.rich_children),
    path('people/parentsOfPerson/<int:id>/', views.parents_of_person),
    path('people/childData/<int:id>/', views.child_data),
    path('people/grandparents/<int:id>/', views.grandparents),
    path('people/brothers/<int:id>/', views.brothers),

]
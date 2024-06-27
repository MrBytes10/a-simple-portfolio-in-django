from django.urls import path
from . import views # the dot . means from this folder

urlpatterns = [
    path("", views.home ) # when the baseApp page is called, ho ahed and call views.home, home is the function we've created in views.py of baseApp. Allways try to give same name to the function and the template created.
    
]


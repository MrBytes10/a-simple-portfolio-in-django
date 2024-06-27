from django.shortcuts import render

# Create your views here, they will render templates in the templates/baseApp directory.
# views return http responses
def home(request):
    return render(request, "baseApp/home.html")
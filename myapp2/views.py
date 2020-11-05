from django.shortcuts import render

# Create your views here.
def myfunction(request):
    return render(request, 'page1.html')
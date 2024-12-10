from django.shortcuts import render

# Create your views here.
def suites(request):
    return render(request,'suites.html')

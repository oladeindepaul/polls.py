from django.shortcuts import render

# Create your views here.
def index(request):
  return HttpResponse("Hello, Chelsea fans, your at the fifth stand.")
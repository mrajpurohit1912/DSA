from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse("This about is homepage")

def services(request):
    return HttpResponse("This about is services homepage")

def contact(request):
    return HttpResponse("This about is  contact homepage")
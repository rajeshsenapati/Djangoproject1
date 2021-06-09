from django.shortcuts import render

# Create your views here.

def showIndex(request):
    return render(request, 'demo.html')


def loginPage(request):
    username = request.POST.get('u')
    password = request.POST.get('p')
    if username=="Rajesh" and password=="Senapati":
        return render(request, 'login.html')
    else:
        return render(request, 'error.html')

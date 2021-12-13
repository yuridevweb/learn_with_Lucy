from django.shortcuts import render
from .models import Pet, Dwelling, Avatar
# Create your views here.


def home(request):

    return render(request, 'main/home.html')


def store(request):
    avatars = Avatar.objects.all()
    #advhighScore = AdvMathScore.objects.all()
    #simplehighScore = SimpleMathScore.objects.all()
    if request.POST['submit'] == 'Buy':
        print("True")

    context = {
        'avatars': avatars,
    }

    return render(request, 'main/store.html', context)

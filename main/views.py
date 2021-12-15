from django.shortcuts import render, redirect
from .models import Pet, Dwelling, Avatar
from django.contrib import messages


# Create your views here.


def home(request):

    return render(request, 'main/home.html')


def store(request):
    user_profile = request.user.profile
    avatars = Avatar.objects.all()
    #advhighScore = AdvMathScore.objects.all()
    #simplehighScore = SimpleMathScore.objects.all()
    if request.method == "POST":
        choice = list(request.POST.items())
        item = Avatar.objects.get(name=choice[1][0])
        # print(item.price)
        # user_profile.pet_purschase(item)
        # print(type(user_profile.pet_purschase(item)))
        #messages.warning(request, user_profile.pet_purschase(item))
        #print("xxxx", user_profile.pet_purschase(item))
        if user_profile.pet_purschase(item) == "Congratulations! You have a new pet!":
            messages.warning(request, "Congratulations! You have a new pet!")
            return redirect('profile')

    user = request.user.profile.coins
    print("Money: ", user)
    context = {
        'avatars': avatars,
    }

    return render(request, 'main/store.html', context)

from django.shortcuts import render, redirect
from .models import Pet, Dwelling, Avatar
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):

    return render(request, 'main/home.html')


@login_required
def store(request):
    user_profile = request.user.profile
    avatars = Avatar.objects.all()
    pets = Pet.objects.all()
    #simplehighScore = SimpleMathScore.objects.all()
    if request.method == "POST":
        choice = list(request.POST.items())
        item = Avatar.objects.get(name=choice[1][0])
        print(item)

        if user_profile.purschase(item) == "Congratulations! Your profile has been updated!":
            messages.warning(
                request, "Congratulations! Your profile has been updated!")
            return redirect('profile')

    user = request.user.profile.coins
    print("Money: ", user)
    context = {
        'avatars': avatars,
        'pets': pets,
    }

    return render(request, 'main/store.html', context)

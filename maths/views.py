from django.shortcuts import render
from .models import MathHighScore, AdvMathScore, SimpleMathScore
from django.http import JsonResponse
from users.models import Profile
from django.contrib import messages
# Create your views here.


def maths(request):
    return render(request, 'maths/maths.html')


def addition(request):
    return render(request, 'maths/addition.html')


def advanced_addition(request):
    return render(request, 'maths/advanced_addition.html')


def simple_addition(request):
    return render(request, 'maths/simple_addition.html')


def high_score(request):
    highScore = MathHighScore.objects.all()
    advhighScore = AdvMathScore.objects.all()
    simplehighScore = SimpleMathScore.objects.all()
    context = {
        'highScore': highScore[:20],
        'advhighScore': advhighScore[:20],
        'simplehighScore': simplehighScore[:20],
    }
    return render(request, 'maths/high_score.html', context)


def get_addition_score(request):

    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # obtain data
        data = list(request.POST.items())
        elapsedTime = int(data[0][1])
        new_score = int(data[1][1])
        """ Updating the HighScore  """

        messages.warning(
            request, request.user.profile.coins_earned(new_score))
        user_name = request.user
        # Creating or updating user's score
        try:
            obj = MathHighScore.objects.get(name=user_name)
            obj.check_high_score(new_score, elapsedTime)
        except MathHighScore.DoesNotExist:
            obj = MathHighScore(
                name=user_name, score=new_score, time=elapsedTime)
        obj.format_time()
        return JsonResponse({"elapsedTime": "question"}, status=200)
    # some error occured
    return JsonResponse({"error": "error at get addition score"}, status=400)


def get_advanced_add_score(request):

    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # obtain data
        data = list(request.POST.items())
        elapsedTime = int(data[0][1])
        new_score = int(data[1][1])
        """ Updating the HighScore  """
        messages.warning(
            request, request.user.profile.coins_earned(new_score))
        user_name = request.user
        # Creating or updating user's score
        try:
            obj = AdvMathScore.objects.get(name=user_name)
            obj.check_high_score(new_score, elapsedTime)
        except AdvMathScore.DoesNotExist:
            obj = AdvMathScore(
                name=user_name, score=new_score, time=elapsedTime)
        obj.format_time()
        return JsonResponse({"elapsedTime": "question"}, status=200)
    # some error occured
    return JsonResponse({"error": "error at get addition score"}, status=400)


def get_simple_add_score(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # obtain data
        data = list(request.POST.items())
        elapsedTime = int(data[0][1])
        new_score = int(data[1][1])
        messages.warning(
            request, request.user.profile.coins_earned(new_score))
        """ Updating the HighScore  """
        user_name = request.user
        # Creating or updating user's score
        try:
            obj = SimpleMathScore.objects.get(name=user_name)
            obj.check_high_score(new_score, elapsedTime)
        except SimpleMathScore.DoesNotExist:
            obj = SimpleMathScore(
                name=user_name, score=new_score, time=elapsedTime)
        obj.format_time()
        return JsonResponse({"elapsedTime": "question"}, status=200)
    # some error occured
    return JsonResponse({"error": "error at get addition score"}, status=400)

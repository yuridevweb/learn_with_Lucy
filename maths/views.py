from django.shortcuts import render, redirect
from .models import HighScoreModel
from django.http import JsonResponse
from django.contrib import messages

# Create your views here.


def addition(request):

    return render(request, 'maths/addition.html')


def advanced_addition(request):

    return render(request, 'maths/advanced_addition.html')


def high_score(request):
    highScore = HighScoreModel.objects.all()
    context = {
        'highScore': highScore[:20],
    }

    return render(request, 'main/high_score.html', context)


def get_addition_score(request):

    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # obtain data
        data = list(request.POST.items())
        elapsedTime = int(data[0][1])
        new_score = int(data[1][1])

        """ Updating the HighScore  """
        user_name = request.user
        # Creating or updating user's score
        try:
            obj = HighScoreModel.objects.get(name=user_name)
            obj.check_high_score(new_score, elapsedTime)
            # if obj.score < new_score:
            #obj.score = new_score
            #obj.time = elapsedTime
            # elif obj.score == new_score:
            # if obj.time > elapsedTime:
            #obj.time = elapsedTime
        except HighScoreModel.DoesNotExist:
            obj = HighScoreModel(
                name=user_name, score=new_score, time=elapsedTime)
        obj.format_time()
        return JsonResponse({"elapsedTime": "question"}, status=200)

    # some error occured
    return JsonResponse({"error": "error at get addition score"}, status=400)


# reverse for records

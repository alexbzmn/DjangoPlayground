from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

import json

from django.views.decorators.csrf import csrf_exempt

from .models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def create_question_view(request, arg):
    return render(request, 'polls/createq.html')


def create_question_create(request, arg):
    questionJSON = json.loads(request.body)

    question = Question()
    question.question_text = str(questionJSON.get("Text"))
    question.pub_date = timezone.now()

    question.save()

    return HttpResponse("Question is created")


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

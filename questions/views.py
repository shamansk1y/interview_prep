from django.shortcuts import render
from .models import Question
from django.core.paginator import Paginator

def index(request):
    easy_question_count = Question.objects.filter(difficulty='Easy').count()
    medium_question_count = Question.objects.filter(difficulty='Medium').count()
    hard_question_count = Question.objects.filter(difficulty='Hard').count()

    context ={
        'easy_question_count': easy_question_count,
        'medium_question_count': medium_question_count,
        'hard_question_count': hard_question_count,
    }
    return render(request, 'index.html', context=context)


def easy_page(request):
    easy_question_count = Question.objects.filter(difficulty='Easy')
    count = 1
    paginator = Paginator(easy_question_count, count)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    context = {
        'easy_question_count': easy_question_count,
        'page_obj': page_obj,
    }
    return render(request, 'easy.html', context=context)

def medium_page(request):
    medium_question_count = Question.objects.filter(difficulty='Medium')
    count = 1
    paginator = Paginator(medium_question_count, count)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    context = {
        'medium_question_count': medium_question_count,
        'page_obj': page_obj,
    }
    return render(request, 'medium.html', context=context)


def hard_page(request):
    hard_question_count = Question.objects.filter(difficulty='Hard')
    count = 1
    paginator = Paginator(hard_question_count, count)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    context = {
        'medium_question_count': hard_question_count,
        'page_obj': page_obj,
    }
    return render(request, 'hard.html', context=context)

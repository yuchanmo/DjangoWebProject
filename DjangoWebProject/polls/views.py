from django.shortcuts import render,get_object_or_404

# Create your views here.

from django.http import HttpResponse,Http404
from polls.models import Questions
from django.template import loader

def index(request):
    latest_question_list = Questions.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list':latest_question_list
        }
    #return HttpResponse(template.render(context,request))
    return render(request,'polls/index.html',context)


def detail(request,question_id):
    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404('Question does not exist')
    question = get_object_or_404(Questions,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})

def results(request,question_id):
    response = 'you`re looking at the result of question_id%s'
    return HttpResponse(response%question_id)

def vote(request,question_id):
    question = get_object_or_404()
    return HttpResponse('you`re voting on question %s'%question_id)
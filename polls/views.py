from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question,Choice
from django.urls import reverse
from django.template import loader
# Create your views here.


def index(request):
    '''
    질문 목록을 보여주는 뷰
    :param request: 뷰 함수의 필수 인자
    :return: 최종적으로 클라이언트에게 응답할 데이터인 HttpResopnse 객체 반환
    '''
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'lastest_question_list' : lastest_question_list}
    return render(request,'polls/index.html',context)

def detail(request ,question_id):
    question = get_object_or_404(Question ,pk = question_id)
    return render(request,'polls/detail.html', {'question': question})


def result(request,question_id):
    response = "You're looking at the results of question %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try :
        selected_choice = question.choice_set.get(pk=request.Post['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',  {
            'question': question,
            'error_message': "선택하지 않았습니다",
        })
    else :
        selected_choice.vote +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:result', args=(question_id,)))
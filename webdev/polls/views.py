from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice, Daily
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now())
'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    #output = ', '.join([p.question_text for p in latest_question_list])

    context = {'latest_question_list':latest_question_list}
    return render(request, 'polls/index.html', context)
    #return HttpResponse("hello,world. Your are at the polls index.")
'''

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
'''
def detail(request,question_id):

    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/detail.html', {'question':question})

    #return HttpResponse("you're looking at question %s." % question_id)
'''

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
'''
def results(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
'''
class DailyView(generic.DetailView):
    model = Daily
    template_name = 'polls/detail.html'

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request,'polls/detail.html', {
            'question': p,
            'error_message' : 'You did not select a choice.'
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


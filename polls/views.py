from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question#, Company, Post, Post_detail
from django.db.models import Q
from datetime import datetime



class IndexView(generic.ListView):
    model = Post_detail
    template_name = 'polls/index.html'
    #context_object_name = 'latest_question_list'
    
    t = Company.objects.get(pk=1)
    t.name = "フロアB"
    t.save()
    

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        #return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
        return Post_detail.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        a=Post_detail.objects.get(body = Post.objects.get(name = 'リーダB'))
        context['now'] = datetime(2020, 11, 4, 20, 40, 59)


        context['A_list'] = Post_detail.objects.filter(post__name = 'リーダB').values('duedate')
        context['AA_list'] = Post_detail.objects.filter(duedate__lt=Post_detail.objects.filter(post__name = 'リーダB').values('duedate')).values('body')
        context['AAA_list'] = Post_detail.objects.filter(duedate__gt=Post_detail.objects.filter(post__name = 'リーダB').values('duedate')).values('body')

        
        now = datetime(2020, 11, 4, 20, 40, 59)

        A_list = Post_detail.objects.filter(post__name = 'リーダB').values('duedate')
        AA_list = Post_detail.objects.filter(duedate__lt=Post_detail.objects.filter(post__name = 'リーダB').values('duedate')).values('body')
        
        context['B_list'] = Post_detail.objects
        context['Company_list'] = Company.objects.all()
        
        #q = Question(question_text=AA_list, pub_date=timezone.now())
        #q.save()
        return context


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

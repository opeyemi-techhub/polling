from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Question, Choice, Voter
from .forms import NameForm


@csrf_exempt
def update(request):
    if request.method == "POST":
        repo=git.Repo("techg.pythonanywhere.com/")
        origin = repo.remote.origin
        origin.pull()
        return HttpResponse("Updated code to PythonAnywhere")
    else:
        return HttpResponse("Couldn't update to PythonAnywhere")

    
class LandView(generic.ListView):
    template_name='polls/login.html'
    context_object_name='first'
class IndexView(generic.ListView):
    template_name='polls/index.html'
    context_object_name='latest_question_list'
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('pub_date')[:5]

class DetailView(generic.DetailView):
    model=Question
    template_name='polls/detail.html'
    
class ResultsView(generic.DetailView):
    model=Question
    template_name='polls/results.html'
    
# Create your views here.
def index(request):
    v=request.POST.get('loginid')
    
    try:
        r=Voter.objects.get(pk=v)
        Voter.objects.get(pk=v).voter_email==request.POST.get('email')
    except (KeyError, Voter.DoesNotExist):
        return render(request, 'polls/login.html')
    else:
        m=Voter.objects.get(pk=v)
        fname=m.voter_first_name
        lname=m.voter_last_name
        gender=m.voter_gender
        age=m.voter_age
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    template=loader.get_template('index.html')
    
    context={'latest_question_list': latest_question_list,}
    return render(request, 'index.html', context={'latest_question_list': latest_question_list,
                                                  'f_name': fname,
                                                  'l_name': lname,
                                                  'gender': gender,
                                                  'age': age})
def imgindex(request):
    return render(request, 'imgindex.html')
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "You didn't select a choice.",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
def voterid(request):
    v=request.POST.get('loginid')
    
    try:
        r=Voter.objects.get(pk=v)
        Voter.objects.get(pk=v).voter_email==request.POST.get('email')
    except (KeyError, Voter.DoesNotExist):
        return render(request, 'polls/login.html')
    else:
        m=Voter.objects.get(pk=v)
        fname=m.voter_first_name
        lname=m.voter_last_name
        gender=m.voter_gender
        age=m.voter_age
        return render(request, 'polls/index.html', context={'f_name': fname,
                                                      'l_name': lname,
                                                      'gender': gender,
                                                      'age': age})
        
    



    
def login(request):
    return render(request, 'login.html')
def next(request):
    dob=request.POST.get('year')
    d=dob[0:4]
    dd=int(d)
    age=2020-dd
    v=Voter(voter_first_name = request.POST.get('f_name'),
            voter_last_name = request.POST.get('l_name'),
            voter_gender = request.POST.get('gender'),
            voter_age = age,
            voter_email = request.POST.get('email'),
            registration_date = timezone.now())
    v.save()
    voter_id=v.id
    return render(request, 'next.html', {'voter_id': voter_id,
                                         'first_name': request.POST.get('f_name'),
                                         'last_name': request.POST.get('l_name'),
                                             })
    
def signup(request):
    return render(request, 'signup.html')
    
def tex(request):
    return render(request, 'tex.html')


















def form(request):
    return render(request, 'form.html')

def get_name(request):
    print(request.POST.get('yourname'))
    return render(request, 'name.html')    





















from django.urls import path
from . import views
app_name='polls'
urlpatterns = [
    path('tex', views.tex, name='tex'),
    path('signup', views.signup, name='signup'),
    path('next', views.next, name='next'),
    path('', views.login, name='login'),
    path('index', views.index, name='index'),
    path('img', views.imgindex, name='imgindex'),
    # ex: /polls/5/
    path('specifics/<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('voterid', views.voterid, name='voterid'),
    path('name', views.get_name, name='name'),
    path('form', views.form, name='form'),
    path('update_server/', views.update, name='update'),
]


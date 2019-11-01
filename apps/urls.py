from django.urls import path
from . import views

app_name = 'apps'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('profile/<str:username>', views.profile, name='profile'),
    path('problems', views.problems, name='problems'),
    path('problem/<int:id>', views.problem, name='problem'),
    path('submissions', views.submissions, name='submissions'),
    path('submissions/my', views.submissions_my, name='submissions_my'),
    path('submission/<int:id>', views.submission, name='submission')
]

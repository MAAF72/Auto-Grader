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
    path('problems/manage/', views.problems_manage, name='problems_manage'),
    path('problem/test_case/<int:id>', views.problem_test_case, name='problem_test_case'),
    path('test_case/<int:id>/create/', views.test_case_create, name='test_case_create'),
    path('test_case/edit/<int:id>/', views.test_case_edit, name='test_case_edit'),
    path('test_case/delete/<int:id>/', views.test_case_delete, name='test_case_delete'),
    path('problem/create', views.problem_create, name='problem_create'),
    path('problem/edit/<int:id>', views.problem_edit, name='problem_edit'),
    path('problem/delete/<int:id>', views.problem_delete, name='problem_delete'),
    path('problem/<int:id>', views.problem, name='problem'),
    path('submissions', views.submissions, name='submissions'),
    path('submissions/my', views.submissions_my, name='submissions_my'),
    path('submission/<int:id>', views.submission, name='submission')
]

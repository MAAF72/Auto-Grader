import uuid
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import django.contrib.auth as auth
from django.db.models import Q, Sum, Max
from django.contrib.auth.models import User

from . import models



TC_IN = '../judge/TC-In'
TC_OUT = '../judge/TC-Out'
SUBMISSION = '../judge/Submission'

def index(request):
    context = {
        'Title': 'ULTRAG - Index'
    }

    return render(request, 'apps/index.html', context)

def login(request):
    context = {
        'Title': 'ULTRAG - Login',
        'Message': '',
    }

    if request.user.is_authenticated:
        return redirect('apps:index')
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(request, username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('apps:index')
        else:
            context['Message'] = 'Wrong Credential!'

    return render(request, 'apps/login.html', context)

def register(request):
    context = {
        'Title': 'ULTRAG - Register',
        'Message': '',
    }

    if request.user.is_authenticated:
        return redirect('apps:index')
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        if User.objects.filter(~Q(username__iexact=username), ~Q(email__iexact=email)).exists():
            User.objects.create_user(username=username, email=email, password=password).save()
            user = auth.authenticate(request, username=username, password=password)
            auth.login(request, user)

            return redirect('apps:index')
        else:
            context['Message'] = 'Username or Email Has Already Been Taken!'

    return render(request, 'apps/register.html', context)

def logout(request):
    auth.logout(request)
    return redirect('apps:index')

def profile(request, username):
    user = User.objects.get(username=username)
    submissions = models.Submission.objects.filter(user=user)
    user.score = submissions.values('problem').annotate(greatest=Max('score')).aggregate(total=Sum('greatest'))['total']

    context = {
        'Title': 'ULTRAG - {}\'s Profile'.format(username),
        'User': user,
        'Submissions': submissions
    }

    return render(request, 'apps/profile.html', context)

def submissions(request):
    submissions = models.Submission.objects.all().order_by('-date')

    context = {
        'Title': 'ULTRAG - Submission List',
        'Submissions': submissions
    }

    return render(request, 'apps/submissions.html', context)

@login_required(login_url='/login')
def submissions_my(request):
    submissions = models.Submission.objects.filter(user=request.user).order_by('-date')

    context = {
        'Title': 'ULTRAG - My Submissions',
        'Submissions': submissions
    }

    return render(request, 'apps/submissions_my.html', context)

def submission(request, id):
    submission = models.Submission.objects.get(id=id)
    EXTENSION = {
        'Golang': 'go',
        'C++': 'cpp',
        'C': 'c'
    }

    if request.user == submission.user:
        with open('{}/{}.{}'.format(SUBMISSION, submission.name, EXTENSION[submission.language]), 'r', errors='ignore') as code:
            submission.code = code.read()
    else:
        submission.code = 'You cannot view this submission\'s code'

    context = {
        'Submission': submission
    }

    return render(request, 'apps/submission.html', context)

def problems(request):
    problems = models.Problem.objects.all()

    for problem in problems:
        problem.total = models.Submission.objects.filter(Q(problem_id=problem), ~Q(status='PEN'))
        if problem.total.count() > 0:
            problem.succes = round(problem.total.filter(status='AC').count() / problem.total.count() * 100.0, 2)
        else:
            problem.succes = 0.00

        problem.total = problem.total.count()

    context = {
        'Title': 'ULTRAG - Problem List',
        'Problems': problems
    }

    return render(request, 'apps/problems.html', context)

def problem(request, id):
    if request.method == 'POST' and request.user.is_authenticated:
        if request.FILES['submission'].size <= 256 * 1024:
            extension = str(request.FILES['submission']).lower().rsplit('.', 1)[-1]
            LANGUAGE = {
                'go': 'Golang',
                'cpp': 'C++',
                'c': 'C'
            }

            if extension in LANGUAGE:
                name = str(uuid.uuid4())
                with open('{}/{}.{}'.format(SUBMISSION, name, extension), 'wb+') as file:
                    #check if file.read() contain malicious code
                    for chunk in request.FILES['submission']:
                        file.write(chunk)
                submission = models.Submission.objects.create(user=request.user, name=name, problem=models.Problem.objects.get(id=id), language=LANGUAGE[extension], host=0)
                submission.save()
                return redirect('apps:submission', submission.id)
            return redirect('') #Extension not allowed
        return redirect('') #File Size Limit Exceeded

    else:
        problem = models.Problem.objects.get(id=id)
        samples = models.SampleCase.objects.filter(case__problem=problem) #join
        for sample in samples:
            case = sample.case
            with open('{}/{}.txt'.format(TC_IN, case.name), 'r') as input, open('{}/{}.txt'.format(TC_OUT, case.name), 'r') as output:
                sample.input = input.read()
                sample.output = output.read()

        context = {
            'Title': 'ULTRAG - {}'.format(problem.name),
            'Problem': problem,
            'Samples': samples
        }

    return render(request, 'apps/problem.html', context)

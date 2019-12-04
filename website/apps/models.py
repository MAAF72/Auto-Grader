from os.path import join
from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

JUDGE_STORAGE_ROOT = join('..', '..', 'judge')
judge_storage = FileSystemStorage(location=JUDGE_STORAGE_ROOT)

class Problem(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default=None)
    input_format = models.TextField(default=None)
    output_format = models.TextField(default=None)
    constraints = models.TextField(default=None)
    time_limit = models.PositiveSmallIntegerField()
    memory_limit = models.PositiveSmallIntegerField()
    date = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return '{}'.format(self.name)

class TestCase(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE) #Many to One
    name = models.CharField(max_length=52)
    input = models.FileField(default=None, upload_to='TCIn', storage=judge_storage)
    output = models.FileField(default=None, upload_to='TCOut', storage=judge_storage)
    sample = models.BooleanField(default=False)
    explanation = models.TextField(default='', blank=True)
    date = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return '{}'.format(self.name)

class Submission(models.Model):
    STATUS_CHOICES = {
        ('PEN', 'Pending'),
        ('AC', 'Accepted'),
        ('WA', 'Wrong Answer'),
        ('TLE', 'Time Limit Exceeded'),
        ('RTE', 'Runtime Error'),
        ('CTE', 'Compilation Error'),
        ('ACE', 'Abort Called Error'),
        ('MLE', 'Memory Limit Exceeded'),
        ('UNE', 'Unknown Error')
    }

    user = models.ForeignKey(User, default=None, on_delete=models.DO_NOTHING)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    file = models.FileField(default=None, upload_to='Submission', storage=judge_storage)
    language = models.CharField(max_length=10, editable=False, default='UNKNOWN')
    host = models.PositiveSmallIntegerField(default=0)
    score = models.FloatField(default=0)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='PEN')
    date = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return '{}'.format(self.file)

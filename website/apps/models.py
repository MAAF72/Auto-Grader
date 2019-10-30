from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from martor.models import MartorField


class Problem(models.Model):
    name = models.CharField(max_length=50)
    description = MartorField()
    input = MartorField()
    output = MartorField()
    constraint = MartorField()
    time = models.PositiveSmallIntegerField()
    memory = models.PositiveSmallIntegerField()
    date = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return '{}'.format(self.name)

class TestCase(models.Model):
    name = models.CharField(max_length=52)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE) #Many to One
    date = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return '{}'.format(self.name)

class SampleCase(models.Model):
    case = models.OneToOneField(TestCase, on_delete=models.CASCADE)
    explanation = MartorField(blank=True)
    date = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return '{}'.format(self.case)

class Submission(models.Model):
    STATUS_CHOICES = {
        ('PEN', 'Pending'),
        ('AC', 'Accepted'),
        ('WA', 'Wrong Answer'),
        ('TLE', 'Time Limit Exceeded'),
        ('RTE', 'Runtime Error'),
        ('CTE', 'Compilation Error'),
        ('ACE', 'Abort Called Error'),
        ('UNE', 'Unknown Error')
    }

    user = models.ForeignKey(User, default=None, null=True, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    language = models.CharField(max_length=10, editable=False, default='Unknown')
    host = models.PositiveSmallIntegerField(default=0)
    score = models.FloatField(default=0)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='PEN')
    date = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return '{}'.format(self.name)

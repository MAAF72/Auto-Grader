from django.forms import ModelForm, Textarea
from .models import Problem, TestCase
from os import path


class ProblemForm(ModelForm):
    class Meta:
        model = Problem
        '''
        fields = [
            'name', 
            'statement', 
            'input_format', 
            'output_format', 
            'constraints',
            'time_limit',
            'memory_limit',
            'date_created',
        ]
        '''
        fields = '__all__'
        '''
        labels = {
            'name' : _('Problem Name'),
            'statement' : _('Problem Statement'),
            'input_format' : _('Input Format'),
            'output_format' : _('Output Format'),
            'constraints' : _('Constraints'),
            'time_limit' : _('Time Limit(mili seconds)')
            'memory_limit' : _('Memory Limit(MB)')
        }
        '''

class TestCaseForm(ModelForm):
    class Meta:
        model = TestCase
        exclude = ('problem', 'input', 'output')

    def save(self, input_content, output_content):
        if not self.instance.pk:
            self.instance.problem = self.problem
            self.instance.input.name = self.input
            self.instance.output.name = self.output

        with open('{}.txt'.format(path.join('..', 'judge', 'TCIn', self.instance.input.name)), 'w', newline='') as input, open('{}.txt'.format(path.join('..', 'judge', 'TCOut', self.instance.output.name)), 'w', newline='') as output:
            input.write(input_content)
            output.write(output_content)

        super().save()
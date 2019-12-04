# Generated by Django 2.2.7 on 2019-11-28 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_auto_20191128_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='status',
            field=models.CharField(choices=[('WA', 'Wrong Answer'), ('UNE', 'Unknown Error'), ('PEN', 'Pending'), ('ACE', 'Abort Called Error'), ('AC', 'Accepted'), ('RTE', 'Runtime Error'), ('MLE', 'Memory Limit Exceeded'), ('TLE', 'Time Limit Exceeded'), ('CTE', 'Compilation Error')], default='PEN', max_length=3),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='explanation',
            field=models.TextField(blank=True, default=''),
        ),
    ]

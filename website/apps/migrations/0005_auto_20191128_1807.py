# Generated by Django 2.2.7 on 2019-11-28 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_auto_20191128_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='status',
            field=models.CharField(choices=[('MLE', 'Memory Limit Exceeded'), ('AC', 'Accepted'), ('PEN', 'Pending'), ('ACE', 'Abort Called Error'), ('WA', 'Wrong Answer'), ('RTE', 'Runtime Error'), ('TLE', 'Time Limit Exceeded'), ('CTE', 'Compilation Error'), ('UNE', 'Unknown Error')], default='PEN', max_length=3),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='sample',
            field=models.BooleanField(default=False, null=True),
        ),
    ]

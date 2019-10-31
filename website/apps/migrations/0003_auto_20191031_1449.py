# Generated by Django 2.2.6 on 2019-10-31 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_auto_20191030_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='status',
            field=models.CharField(choices=[('WA', 'Wrong Answer'), ('CTE', 'Compilation Error'), ('MLE', 'Memory Limit Exceeded'), ('UNE', 'Unknown Error'), ('PEN', 'Pending'), ('AC', 'Accepted'), ('RTE', 'Runtime Error'), ('TLE', 'Time Limit Exceeded'), ('ACE', 'Abort Called Error')], default='PEN', max_length=3),
        ),
    ]

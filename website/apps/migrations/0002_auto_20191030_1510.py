# Generated by Django 2.2.6 on 2019-10-30 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='samplecase',
            name='case',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='apps.TestCase'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='status',
            field=models.CharField(choices=[('AC', 'Accepted'), ('UNE', 'Unknown Error'), ('PEN', 'Pending'), ('RTE', 'Runtime Error'), ('CTE', 'Compilation Error'), ('ACE', 'Abort Called Error'), ('WA', 'Wrong Answer'), ('TLE', 'Time Limit Exceeded')], default='PEN', max_length=3),
        ),
    ]

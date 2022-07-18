# Generated by Django 4.0.6 on 2022-07-18 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('day', models.CharField(choices=[('M', 'M-W-F'), ('T', 'T-TH')], default='M', max_length=1)),
                ('time', models.CharField(choices=[('1', '8:00-9:30 am'), ('2', '9:30-11:00 am'), ('3', '12:00-1:30 pm'), ('4', '1:30-3:00 pm')], default='1', max_length=1)),
                ('description', models.TextField(max_length=250)),
                ('teacher', models.CharField(max_length=100)),
                ('prereq', models.CharField(max_length=100)),
            ],
        ),
    ]

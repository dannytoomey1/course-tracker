# Generated by Django 2.2.12 on 2022-07-20 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_auto_20220719_1917'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.TextField(max_length=250)),
                ('assign_date', models.DateField(verbose_name='Assign Date')),
                ('due_date', models.DateField(verbose_name='Due Date')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Lesson')),
            ],
            options={
                'ordering': ['due_date'],
            },
        ),
    ]

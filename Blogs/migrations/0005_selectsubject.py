# Generated by Django 2.0.6 on 2018-07-17 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0004_tutoradmin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Selectsubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[('Statistics', 'STATISTICS'), ('Programming', 'PROGRAMMING'), ('Physics', 'PHYSICS'), ('Chemical Engineering', 'CHEMICAL'), ('Android', 'ANDROID'), ('Biology', 'BIOLOGY'), ('Civil Engineering', 'CIVIL'), ('Chemistry', 'CHEMICAL'), ('Computer Science', 'COMPUTER'), ('English', 'ENGLISH'), ('Economics', 'ECONOMICS'), ('Electrical Engineering', 'ELECTRICAL'), ('Maths', 'MATHS'), ('Matlab', 'MATLAB'), ('Mechanical', 'MECHANICAL'), ('R', 'R')], max_length=35)),
            ],
        ),
    ]
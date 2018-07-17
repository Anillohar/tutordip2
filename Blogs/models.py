from django.db import models

class Blogs(models.Model):
    Title = models.CharField(max_length=50)
    Author = models.CharField(max_length=100)
    Heading =models.CharField(max_length=100)
    Fulltext = models.BooleanField()
    Image = models.ImageField()


class Becometutor(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=100)
    Email =models.EmailField(max_length=100)
    DOB = models.DateField()
    CollegeName = models.CharField(max_length=250)
    Subjects = models.CharField(max_length=150)

class Tutoradmin(models.Model):
    Name = models.CharField(max_length=50)
    University = models.CharField(max_length=250)
    Subjects = models.CharField(max_length=250)
    Stream = models.CharField(max_length=250)
    About = models.CharField(max_length=1000)
    Fullabout = models.CharField(max_length=2500)

SUBJECT_CHOICES = (
    ('STATISTICS','Statistics'),
    ('PROGRAMMING','Programming'),
    ('PHYSICS','Physics'),
    ('CHEMICAL','Chemical Engineering'),
    ('ANDROID','Android'),
    ( 'BIOLOGY','Biology'),
    ('CIVIL','Civil Engineering'),
    ('CHEMICAL','Chemistry'),
    ('COMPUTER','Computer Science'),
    ('ENGLISH','English'),
    ('ECONOMICS','Economics'),
    ('ELECTRICAL','Electrical Engineering'),
    ('MATHS', 'Maths'),
    ('MATLAB', 'Matlab'),
    ('MECHANICAL', 'Mechanical Engineering'),
    ('R', 'R')
)

class Selectsubject(models.Model):
  subject = models.CharField(max_length=35, choices=SUBJECT_CHOICES)
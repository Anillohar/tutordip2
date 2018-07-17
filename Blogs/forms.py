from .models import Blogs,Becometutor,Tutoradmin,Selectsubject
from django import forms

class blogform(forms.ModelForm):

    class Meta:
        model = Blogs
        fields = ('Author' , 'Title' , 'Fulltext' , 'Image' , 'Heading')

class becometutorform(forms.ModelForm):

    class Meta:
        model = Becometutor
        fields = ('Firstname' , 'Lastname' , 'DOB' , 'Email' , 'CollegeName' , 'Subjects')

class tutoradmin(forms.ModelForm):

    class Meta:
        model = Tutoradmin
        fields = ('Name' , 'University' , 'About' , 'Subjects' , 'Stream' , 'Fullabout')

class Selectsubjectform(forms.ModelForm):

    class Meta:
        model = Selectsubject
        fields = ('subject',)
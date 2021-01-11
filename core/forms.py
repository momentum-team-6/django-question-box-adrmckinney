from django import forms
from .models import Post, Answer

class QForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'question_title',
            'question_body',
        ]
    
class AForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = [
            'answer',
        ]

# class Registration(forms.RegistrationForm):
#     class Meta:
#         fields = [
#             'username',
#             'email',
#             'password1',
#             'password2',
#         ]
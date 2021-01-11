from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Post(models.Model):
    question_title = models.CharField(max_length=50)
    question_body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', null=True)
    status = models.BooleanField(default=False)
    



class Answer(models.Model):
    answer = models.TextField()
    post = models.ForeignKey('Post', related_name='answers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer

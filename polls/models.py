import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

# class Company(models.Model):
#     name = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True,null=True)
#     updated_at = models.DateTimeField(auto_now=True,null=True)

#     def __str__(self):
#         return self.name

# class Post(models.Model):
#     name = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True,null=True)
#     updated_at = models.DateTimeField(auto_now=True,null=True)
#     company = models.ForeignKey(Company, verbose_name='投稿', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

# class Post_detail(models.Model):
#     body = models.CharField(max_length=255)
#     kyodo = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     post = models.ForeignKey(Post, verbose_name='投稿詳細', on_delete=models.CASCADE)
#     duedate = models.DateTimeField(null=True)

#     def __str__(self):
#         return self.body
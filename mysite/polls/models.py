import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200) # 문자 필드, max_length 명시 해주어야 함
    pub_date = models.DateTimeField('date published') # 날짜, 시간 필드 함
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # Choice가 하나의 Question에 관계된다.
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) # default = 0
    def __str__(self):
        return self.choice_text

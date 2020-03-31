from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200) # 문자 필드, max_length 명시 해주어야 함
    pub_date = models.DateTimeField('date published') # 날짜, 시간 필드 함
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # Choice가 하나의 Question에 관계된다.
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) # 기본값 = 0
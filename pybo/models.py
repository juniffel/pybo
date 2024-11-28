'''
모델 
질문 모델
제목
내용
일시

답변 모델
질문(외래키 연결)
내용
일시
'''
from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200) # 200자 내
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')  # 추천인 추가     
    def __str__(self):
        return self.subject

class Answer(models.Model):
    # 외래키로 질문모델과 연결, CASCADE : 질문을 삭제하면 해당 답변들도 다 삭제
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE) 
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')

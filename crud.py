from pybo.models import Question, Answer
from django.utils import timezone
import os
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
settings.configure()
# Question 생성
q = Question(subject='pybo가 무엇인가요?', content='pybo에 대해서 알고 싶습니다.', create_date=timezone.now())
q.save()
print(f"q.id:{q.id}")

q = Question(subject='장고 모델 질문입니다.', content='id는 자동으로 생성되나요?', create_date=timezone.now())
q.save()
print(f"q.id:{q.id}")
print(f"Question.objects.all()[모든 데이터 목록]\n{Question.objects.all()}")

# Question 조회
from pybo.models import Question, Answer
print(f"Question.objects.all()[모든 데이터 목록]\n{Question.objects.all()}")
print(f"Question.objects.filter(id=1)[id가 1인 데이터]\n{Question.objects.filter(id=1)}")
print(f"Question.objects.get(id=1)[id가 1인 데이터]\n{Question.objects.get(id=1)}")
print(f"Question.objects.filter(subject__contains='장고')[제목에 장고가 포함된 데이터]\n{Question.objects.filter(subject__contains='장고')}")


# Question 수정
q = Question.objects.get(id=2)
print(f"q:{q}")
q.subject = 'Django Model Question'
q.save()
print(f"q:{q}")


# Question 삭제
q = Question.objects.get(id=1)
print(f"q.delete():{q.delete()}")

print(f"Question.objects.all()[모든 데이터 목록]\n{Question.objects.all()}")

# Answer 작성
q = Question.objects.get(id=2)
print(f"q:{q}")

from django.utils import timezone
a = Answer(question=q, content='네 자동으로 생성됩니다.', create_date=timezone.now())
a.save()

# Answer 조회
a = Answer.objects.get(id=1)
print(f"a:{a}")
print(f"a.question:{a.question}")
print(f"q.answer_set.all()[질문에 연결된 답변 리스트]:{q.answer_set.all()}")


from django.db import models
from django.contrib.auth.models import User

# 질문 모델
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')  # 계정이 삭제되면 계정과 연결된 Question 모델 데이터를 모두 삭제
    subject = models.CharField(max_length=200)      # 글자 수 제한하는 데이터타입은 CharField를 사용
    content = models.TextField()                    # 글자 수 제한이 없는 데이터는 TextField를 사용
    create_date = models.DateTimeField()            # 날짜, 시간 관련 속성은 DateTimeField를 사용
    modify_date = models.DateTimeField(null=True, blank=True)   # null=True는 데이터베이스에서 modify_date 칼럼에 null을 허용한다는 의미이며, blank=True는 form.is_valid()를 통한 입력 폼 데이터 검사 시 값이 없어도 된다는 의미다.
    voter = models.ManyToManyField(User, related_name='voter_question')            # 추천인 voter 필드를 ManyToManyField 관계로 추가

    def __str__(self):
        return self.subject

# 답변 모델
class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)    # Answer 모델은 어떤 질문에 대한 답변이므로 Question 모델을 속성으로 가져야 한다. 어던 모델이 다른 모델을 속성으로 가지면 Foreignkey 사용!
                                                                        # Foreignkey는 다른 모델과의 연결을 의미하며, on_delete=models.CASCADE는 답변에 연결된 질문이 삭제되면 답변도 함께 삭제하라는 의미
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 댓글 글쓴이
    content = models.TextField()                                # 댓글 내용
    create_date = models.DateTimeField()                        # 댓글 작성일시
    modify_date = models.DateTimeField(null=True, blank=True)   # 댓글 수정일시
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)     # 이 댓글이 달린 질문
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)         # 이 댓글이 달린 답변
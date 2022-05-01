from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Faq(models.Model):
    Category = [
        ('NORMAL', '일반'),
        ('ID', '계정'),
        ('OTHER', '기타'),
    ]

    title = models.CharField(verbose_name='제목', max_length=60)
    category = models.CharField(
        verbose_name='카테고리',
        max_length=6,
        choices=Category,
    )
    created_at = models.DateTimeField(verbose_name='생성 일시', auto_now_add=True)
    last_modified_at = models.DateTimeField(verbose_name='최종 수정 일시', auto_now=True)
    question = models.CharField(verbose_name='질문', max_length=100)
    answer = models.TextField(verbose_name='답변')
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE)


class Inquiry(models.Model):
    Category = [
        ('NORMAL', '일반'),
        ('ID', '계정'),
        ('OTHER', '기타'),
    ]

    title = models.CharField(verbose_name='질문 제목', max_length=60)
    category = models.CharField(
        verbose_name='카테고리', 
        max_length=6,
        choices=Category,
    )
    created_at = models.DateTimeField(verbose_name='생성 일시', auto_now_add=True)
    last_modified_at = models.DateTimeField(verbose_name='최종 수정 일시', auto_now=True)
    writer = models.ForeignKey(verbose_name='생성자', to=User, on_delete=models.CASCADE)
    content = models.TextField(verbose_name='질문 내용')
    email = models.EmailField(verbose_name='이메일')
    phone_number = models.CharField(verbose_name='전화번호', max_length=16)


class Answer(models.Model):
    answer = models.TextField(verbose_name='답변')
    inquiry = models.ForeignKey(verbose_name='해당 질문', to='Inquiry', on_delete=models.CASCADE)
    writer = models.ForeignKey(verbose_name='답변자', to=User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='생성 일시', auto_now_add=True)
    last_modified_at = models.DateTimeField(verbose_name='최종 수정 일시', auto_now=True)

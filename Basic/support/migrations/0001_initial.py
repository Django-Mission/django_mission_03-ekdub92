# Generated by Django 4.0.4 on 2022-05-01 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='질문 제목')),
                ('category', models.CharField(choices=[('NORMAL', '일반'), ('ID', '계정'), ('OTHER', '기타')], max_length=6, verbose_name='카테고리')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성 일시')),
                ('last_modified_at', models.DateTimeField(auto_now=True, verbose_name='최종 수정 일시')),
                ('content', models.TextField(verbose_name='질문 내용')),
                ('email', models.EmailField(max_length=254, verbose_name='이메일')),
                ('phone_number', models.CharField(max_length=16, verbose_name='전화번호')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='생성자')),
            ],
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='제목')),
                ('category', models.CharField(choices=[('NORMAL', '일반'), ('ID', '계정'), ('OTHER', '기타')], max_length=6, verbose_name='카테고리')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성 일시')),
                ('last_modified_at', models.DateTimeField(auto_now=True, verbose_name='최종 수정 일시')),
                ('question', models.CharField(max_length=100, verbose_name='질문')),
                ('answer', models.TextField(verbose_name='답변')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(verbose_name='답변')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성 일시')),
                ('last_modified_at', models.DateTimeField(auto_now=True, verbose_name='최종 수정 일시')),
                ('inquiry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='support.inquiry', verbose_name='해당 질문')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='답변자')),
            ],
        ),
    ]

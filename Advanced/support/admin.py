from django.contrib import admin
from .models import Answer, Faq, Inquiry

# Register your models here.
class AnswerInline(admin.TabularInline):
    model = Answer
    min_num = 1
    max_num = 5
    extra = 2
    verbose_name = '답변'
    verbose_name_plural = '답변'

@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'last_modified_at',)
    list_filter = ('category',)
    search_fields = ('title',)
    search_help_text = '카테고리 별 검색이 가능합니다.'
    readonly_fields = ('created_at',)

@admin.register(Inquiry)
class InquiryModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'writer',)
    list_filter = ('category', 'states',)
    search_fields = ('title', 'email', 'phone_number', 'writer__username',)
    search_help_text = '제목, 이메일, 전화번호, 작성자 검색이 가능합니다.'
    readonly_fields = ('created_at',)
    inlines = [AnswerInline,]
    actions = ['send_info',]

    def send_info(modeladmin, request, queryset):
        for item in queryset:
            if item.is_email == True:
                print(item.email)
            if item.is_phone == True:
                print(item.phone_number)
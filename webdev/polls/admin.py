from django.contrib import admin

# Register your models here.
from .models import Question, Choice, DailyItem, DailyContext, DailyComment

class DailyCommentInline(admin.TabularInline):
    model = DailyComment
    extra = 1
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class DailyContexAdmin(admin.StackedInline):
    model = DailyContext
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    list_filter = ['pub_date']
    search_fields = ['question_text']
    fieldsets = [(None,{'fields':['question_text']}),
                 ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
                 ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')

class DailyItemAdmin(admin.ModelAdmin):
    list_filter = ['pub_date']
    search_fields = ['daily_item']
    fieldsets = [(None,{'fields':['daily_item']}),
                 ('Date information', {'fields':['pub_date'],'classes':['collapse']}),
                 ]
    inlines = [DailyContexAdmin, DailyCommentInline]
    list_display = ('daily_item', 'pub_date', 'was_published_recently')


admin.site.register(Question, QuestionAdmin)
admin.site.register(DailyItem, DailyItemAdmin)
#admin.site.register(Choice)
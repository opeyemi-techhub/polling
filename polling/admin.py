from django.contrib import admin

from .models import Question, Choice, Voter

# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
                 ]

    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')

    list_display = ('question_text', 'pub_date')
class VoterAdmin(admin.ModelAdmin):
    list_display = ('voter_first_name', 'voter_last_name','voter_email', 'voter_age', 'voter_gender', 'registration_date')

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Voter, VoterAdmin)


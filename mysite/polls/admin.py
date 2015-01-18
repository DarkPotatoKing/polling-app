from django.contrib import admin
from polls.models import Poll
from polls.models import Choice

#StackedInline
'''
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3
#'''

#TabularInline: less crowded
#'''
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3
#'''

#admin.site.register(Choice)

#collapsed fieldset
#'''
class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        ('info',               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date', 'was_published_recently')
    #list list_filter
    list_filter = ['pub_date']

admin.site.register(Poll, PollAdmin)
#'''


#default
'''
admin.site.register(Poll)
#'''

#customized admin from
'''
class PollAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question']

admin.site.register(Poll, PollAdmin)
#'''

#using fieldsets
'''
class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        ('info',               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Poll, PollAdmin)
#'''

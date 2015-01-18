from django.contrib import admin
from polls.models import Poll

#collapsed fieldset
#'''
class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        ('info',               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

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

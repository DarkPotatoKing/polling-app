from django.contrib import admin
from polls.models import Poll

#default
'''
admin.site.register(Poll)
#'''

#customized admin from
#'''
class PollAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question']

admin.site.register(Poll, PollAdmin)
#'''

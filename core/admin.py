from django.contrib import admin
from core.models import Participant

class DisplayUser(admin.ModelAdmin):
  list_display = ('name','extype' ,'article0', 'article1', 'article2', 'article3', 'article4', 'article5', 'article6', 'article7', 'article8', 'article9', 'article10', 'article11', 'article12', 'article13', 'article14')
# Register your models here.

admin.site.register(Participant, DisplayUser)
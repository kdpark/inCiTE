from django.db import models

# Create your models here.
class Participant(models.Model):

  name = models.CharField(max_length=150, unique=True)
  extype = models.IntegerField(default=0)
  article0 = models.IntegerField(default=0)
  article1 = models.IntegerField(default=0)
  article2 = models.IntegerField(default=0)
  article3 = models.IntegerField(default=0)
  article4 = models.IntegerField(default=0)
  article5 = models.IntegerField(default=0)
  article6 = models.IntegerField(default=0)
  article7 = models.IntegerField(default=0)
  article8 = models.IntegerField(default=0)
  article9 = models.IntegerField(default=0)
  article10 = models.IntegerField(default=0)
  article11 = models.IntegerField(default=0)
  article12 = models.IntegerField(default=0)
  article13 = models.IntegerField(default=0)
  article14 = models.IntegerField(default=0)

  def __unicode__(self):
    return self.name
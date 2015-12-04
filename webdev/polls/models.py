from django.db import models
import datetime
from django.utils import timezone
import PIL
# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date publish')

    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
    def __str__(self):
        return self.choice_text

class DailyItem(models.Model):
    daily_item = models.CharField(max_length=200)
    #daily_body = models.TextField(max_length= 10000)
    pub_date = models.DateTimeField('date publish')

    def __str__(self):
        return self.daily_item

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class DailyContext(models.Model):
    body = models.ForeignKey(DailyItem)
    daily_context = models.TextField(max_length=10000)
    #daily_file= models.FilePathField(path='/photo', match= None,recursive=True)
    daily_image = models.ImageField(upload_to='photo', null=True, blank=True)
    def __str__(self):
        return self.daily_context

class DailyComment(models.Model):
    comment = models.ForeignKey(DailyItem)
    comment_context = models.CharField(max_length=500)
    def __str__(self):
        return self.comment_context
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Post(models.Model):
    # Fields
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    thumbnail = models.ImageField(u'썸네일', upload_to='%Y/%m/%d', blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    # Metadata
    class Meta:
        ordering = ['author']

    # Methods
    def __str__(self):
        Post.objects.filter(date__lte=timezone.now()).order_by('created_date')
        return self.title
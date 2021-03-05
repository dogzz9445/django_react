from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Post(models.Model):
    # Fields
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField()
    thumbnail = models.ImageField(u'썸네일', 
                        upload_to='%Y/%m/%d', blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        Moim.objects.filter(date__lte=timezone.now()).order_by('created_date')
        return self.title

    # Metadata
    class Meta:
        ordering = ['author']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.my_field_name
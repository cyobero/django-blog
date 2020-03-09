from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=80)
    summary = models.CharField(max_length=141)
    body = models.TextField()
    published = models.BooleanField()
    publish_date = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from="title")
    image = models.ImageField(upload_to="images", null=True, blank=True)

    def __unicode__(self):
        return "{}".format(self.title)

    class Meta:
        ordering = ['-publish_date', ]

from django.db import models
from embed_video.fields import EmbedVideoField

class Item(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    video = EmbedVideoField()
    photo = models.ImageField(blank=True, null=True, upload_to='commu_photo')

    def __str__(self):
        return self.title
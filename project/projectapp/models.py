from django.db import models
from embed_video.fields import EmbedVideoField

class Item(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    video = EmbedVideoField()

    def __str__(self):
        return self.title
from django.db import models

class Tags(models.Model):
    tags_id = models.IntegerField()
    tags = models.CharField(max_length=30)


class Store(models.Model):
    url = models.CharField(max_length=50)
    title = models.CharField(max_length=30)
    text = models.TextField()
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE)

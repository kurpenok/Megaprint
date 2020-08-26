from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=300)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title

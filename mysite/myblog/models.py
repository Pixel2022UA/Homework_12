from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} {self.content}, updated at: {self.updated_at}"

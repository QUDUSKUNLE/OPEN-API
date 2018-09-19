from django.db import models
from django.conf import settings


class Articles(models.Model):
    """Articles model"""
    __tablename__ = 'Articles'

    title = models.CharField(max_length=255, null=False, unique=True)
    content = models.TextField(null=False)
    upload = models.FileField(upload_to='uploads/', blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True, editable=False)

    def clean(self):
        self.title = " ".join(self.title.title().split())

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Articles"
        ordering = ['-id']

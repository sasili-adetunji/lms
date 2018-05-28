from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    owner = models.ForeignKey(User, related_name='course', null=True, blank=True, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='Members', null=True, blank=True)
    date_added = models.DateTimeField()

    class Meta:
        verbose_name = "course"
        verbose_name_plural = 'courses'

    def __str__(self):
        return self.title

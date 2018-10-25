from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=31, unique=True)
    last_name = models.CharField(max_length=151, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ('-created_at', )

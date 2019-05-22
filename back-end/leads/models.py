from django.db import models

# Create your models here.


class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Lead'
        verbose_name_plural = "Leads"

    def __str__(self):
        return self.name

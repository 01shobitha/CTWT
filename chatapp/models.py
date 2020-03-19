from django.db import models
from django.urls import reverse

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse("user_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

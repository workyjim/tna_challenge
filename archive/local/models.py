from django.db import models

# Create your models here.
class LocalItem(models.Model):
    arch_id = models.CharField(primary_key=True, max_length=50)
    title = models.CharField(null=True, max_length=200)
    description = models.CharField(null=True, max_length=1000)
    reference = models.CharField(null=True, max_length=200)

    def __str__(self) -> str:
        return self.title or self.description or self.reference or "not sufficient information"

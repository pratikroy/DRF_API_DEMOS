from django.db import models

# Create your models here.
class JobBoard(models.Model):
    company_name = models.CharField(max_length=255, unique=True)
    company_email = models.EmailField()
    job_title = models.CharField(max_length=255)
    job_description = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=6, decimal_places=2)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    created_at = models.DateField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{ self.company_name }, { self.job_title }"

from django.db import models

# Create your models here.
from aplicatie2.models import Companies

job_choices = (('Full-time', 'Full-time'),
               ('Part-time', 'Part-time'),
               ('Project-based', 'Project-based'),
               ('Volunteering', 'Volunteering'))


class Jobs(models.Model):

    type = models.CharField(max_length=50, choices=job_choices)
    url = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    how_to_apply = models.CharField(max_length=500)
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} from {self.companies.name} name  - {self.companies.location} location"

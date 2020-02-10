from django.db import models

# Create your models here.
class Jobs(models.Model):
    job_image=models.ImageField(null=True)
    jobs_name=models.TextField()
    jobs_description=models.TextField()
    jobs_Title=models.TextField()
    location=models.TextField()
    salary=models.IntegerField()

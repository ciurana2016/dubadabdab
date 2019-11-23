from django.db import models



class Offer(models.Model):

    _id = models.CharField(max_length=32, unique=True, default='')
    title = models.CharField(max_length=200, default='')
    city = models.CharField(max_length=100, default='')
    link = models.CharField(max_length=300, default='')
    salaryDescription = models.CharField(max_length=100, default='')
    applied = models.BooleanField(default=False)
    response_text = models.TextField(max_length=4000, default='')

    def __str__(self):
        return f'Oferta en {self.city} | {self.salaryDescription} \
        | applied={self.applied}'

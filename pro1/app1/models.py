from django.db import models

# Create your models here.
class Bike(models.Model):
    series = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    chasis_num = models.IntegerField()
    color = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.series}-----{self.name}-----{self.chasis_num}-----{self.color}"
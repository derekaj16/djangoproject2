from django.db import models


class PlaneModel(models.Model):
  name = models.CharField(max_length=100)
  price = models.CharField(max_length=50)
  notes = models.TextField()
  image = models.TextField()

  def __str__(self):
        return self.name
  
  class Meta :
        db_table = 'planes'
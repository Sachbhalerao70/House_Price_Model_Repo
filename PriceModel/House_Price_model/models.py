from django.db import models
import datetime

# Create your models here.

class Get_Data_From_User_Model(models.Model):
    # user_id = models.IntegerField(primary_key=True)
    username=models.CharField(max_length=20)
    area_type=models.CharField(max_length=20)
    availability=models.CharField(max_length=20)
    location=models.CharField(max_length=40)
    size=models.CharField(max_length=20)
    society=models.CharField(max_length=20)
    total_sqft=models.FloatField()
  #  Date = models.DateField(default=datetime.date)


    bath=models.IntegerField()
    balcony=models.IntegerField()



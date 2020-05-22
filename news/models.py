from django.db import models

# Create your models here.

class News(models.Model):
	source = models.CharField(max_length =100)
	title = models.TextField()
	description = models.CharField(max_length =1000)
	url = models.CharField(max_length =100)
	urlToImage = models.CharField(max_length =100)
	


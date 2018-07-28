from django.db import models

# Create your models here.
class TinyUrl(models.Model):
    longUrl = models.CharField(max_length=20000)
    shortUrl = models.CharField(max_length = 20000)
    pub_date = models.DateTimeField('date published', auto_now_add = True)
    expiryDate = models.DateTimeField('expiryDate')
    private = models.BooleanField()

    def __str__(self):
    	return self.longUrl
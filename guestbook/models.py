from django.db import models

# Create your models here.

class Guestbook(models.Model):
    no = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    data = models.CharField(max_length=500)
    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Guestbook(%s, %s, %s, %s, %s)' %(self.no, self.name, self.password, self.data, self.reg_date)
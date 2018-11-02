from django.db import models

# Create your models here.

class Board(models.Model):
    no = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=10)
    content = models.CharField(max_length=2000)
    hit = models.IntegerField(default=0)
    order_no = models.IntegerField(default=0)
    group_no = models.IntegerField(default=0)
    depth = models.IntegerField(default=0)
    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Board(%s, %s, %s, %s, %s)' %(self.no, self.title, self.name, self.content,self.reg_date)
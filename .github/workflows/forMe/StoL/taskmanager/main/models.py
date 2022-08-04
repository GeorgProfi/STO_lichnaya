from django.db import models

# Create your models here.
class list_of_executed(models.Model):
    title = models.CharField('название', max_length=50)
    Name_from_list = models.TextField('Имя')

    def __str__(self):
        return self.title
from django.db import models


class list_of_executed(models.Model):
    title = models.CharField('название', max_length=50)
    Name_from_list = models.TextField('Имя')

    def __str__(self):
        return self.title


class RegisteredUsers(models.Model):
    email = models.CharField(primary_key=True, max_length=110)
    surname = models.CharField(max_length=110)
    name = models.CharField(max_length=110)
    password = models.CharField(max_length=32)


class Employees(RegisteredUsers):
    pass


class AwaitingEmailConfirming(RegisteredUsers):
    email_confirmed = models.BooleanField()

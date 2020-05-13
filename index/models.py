from django.db import models


class LendBorrow(models.Model):
    lenderusername = models.CharField(default="NONE",max_length=20)
    borrowerusername = models.CharField(default="NONE",max_length=20)
    transaction = models.IntegerField(default=0) 
    duedate = models.DateTimeField(auto_now_add=True)

 
class committee(models.Model):
    committeeName = models.CharField(primary_key=True, max_length=20)
    memberCount = models.IntegerField(default=0)
    money = models.IntegerField(default=0)


class lendcommittee(models.Model):
    committeeName = models.CharField(max_length=20)
    username = models.CharField(default=0, max_length=20)
    moneyLended = models.IntegerField(default=0)
    duedate = models.DateTimeField(auto_now_add=True)


class startStartup(models.Model):
    startup = models.CharField(primary_key=True, max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    moneyNeeded = models.IntegerField(default=0)
    moneyBorrowed = models.IntegerField(default=0)
    Investors = models.IntegerField(default=0)


class lendStartup(models.Model):
    username = models.CharField(max_length=20)
    startup = models.CharField(max_length=20)
    moneyLended = models.IntegerField(default=0)

# Create your models here.

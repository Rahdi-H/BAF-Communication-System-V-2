from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Acknowledgement(models.Model):
    date = models.DateField()
    time = models.TimeField()
    ref = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

class LOS(models.Model):
    serial = models.IntegerField()
    ref = models.CharField(max_length=255)
    originator = models.CharField(max_length=100)
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True , related_name='senderr')
    receiver_unit = models.ManyToManyField(User, related_name='receivers', verbose_name='receiver_unit')
#   main_receiver = models.CharField(max_length=255, blank=True, null=True)
#   file = models.FileField(upload_to='los/')
    date_of_rec = models.DateField()
    time_of_rec = models.TimeField()
    datetime_of_action = models.DateTimeField(auto_now_add=True)
    action_taken_by = models.CharField(max_length=10)
    received_by = models.ManyToManyField(Acknowledgement, related_name='received', verbose_name='User who received', blank=True)
    receiver_receiving_time = models.TimeField(blank=True , null=True)
    dispatched = models.BooleanField(default=False)


    def __str__(self):
        return str(self.ref)

    def written_by(self):
        return ','.join([str(p) for p in self.receiver_unit.all()])
    
    def received_by_fun(self):
        return ','.join([str(p) for p in self.received_by.all()])

class CRPT(models.Model):
    serial = models.IntegerField()
    ref = models.CharField(max_length=255)
    originator = models.CharField(max_length=100)
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True , related_name='senderrr')
    receiver_unit = models.ManyToManyField(User, related_name='receiverss', verbose_name='receiver_unit')
#   main_receiver = models.CharField(max_length=255, blank=True, null=True)
#   file = models.FileField(upload_to='los/')
    date_of_rec = models.DateField()
    time_of_rec = models.TimeField()
    datetime_of_action = models.DateTimeField(auto_now_add=True)
    action_taken_by = models.CharField(max_length=10)
    received_by = models.ManyToManyField(Acknowledgement, related_name='receivedd', verbose_name='User who received', blank=True)
    receiver_receiving_time = models.TimeField(blank=True , null=True)
    group = models.IntegerField()
    security_grade = models.CharField(max_length=50)
    dispatched = models.BooleanField(default=False)


    def __str__(self):
        return str(self.ref)

    def written_by(self):
        return ','.join([str(p) for p in self.receiver_unit.all()])
    
    def received_by_fun(self):
        return ','.join([str(p) for p in self.received_by.all()])
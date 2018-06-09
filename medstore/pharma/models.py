from django.db import models

# Create your models here.
class Order(models.Model):
    cust_id = models.IntegerField()
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    phn_no = models.BigIntegerField()
    med_name = models.CharField(max_length=50)
    qty = models.IntegerField()

    def __str__(self):
        return self.med_name


class Member(models.Model):
    member_id = models.IntegerField()
    lname = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()
    phn_no = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.member_id
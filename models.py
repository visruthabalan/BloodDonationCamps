from django.db import models

class Donor(models.Model):
    BLOOD_GROUPS = [
        ("A+", "A+"), ("A-", "A-"),
        ("B+", "B+"), ("B-", "B-"),
        ("AB+", "AB+"), ("AB-", "AB-"),
        ("O+", "O+"), ("O-", "O-"),
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    hospital_name = models.CharField(max_length=150)
    donation_date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.blood_group})"

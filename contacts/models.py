from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    
    CONTACT_CHOICES = (
        ('P', 'Personal'),
        ('W', 'Work'),
        ('O', 'Other'),
    )
    contact_type = models.CharField(max_length=1, choices=CONTACT_CHOICES)
    
    def __str__(self):
        return self.name


from django.db import models

# Creating a table for the parishes in Jamaica

class Jamaica_Parishes(models.Model):
    Parish_name = models.CharField(max_length = 60, unique = True)

# This tells python were making a table called Jamaica Parishes

class Meta: 
    ordering = ["Parish_name"]
    verbose_name_plural = "parishes"

# This organizes all the parishes in alphabetical order 

def __str__(self): 
       return self.name

# Changes how rows are displayed as text 
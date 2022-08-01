from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

# the category none corresponds
# to the question created by a user
CATEGORIES = (
    ('Animals', 'Animaux'),
    ('History', 'Histoire'),
    ('Countries and Capital', ' pays et capital'),
    ('None', 'Aucun')
)




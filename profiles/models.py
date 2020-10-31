from django.db import models
from django.contrib.auth import get_user_model
from model_utils.models import TimeStampedModel
from django_countries.fields import CountryField


class Profile(TimeStampedModel):
    GENDER_CHOICES = (
        ('m', 'Male'), 
        ('m', 'Female'),
        ('u', 'Better Not Say')
    )
    user = models.OneToOneField(get_user_model(), 
        on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    country = CountryField(blank_label='(select country)')
    user_icon = models.ImageField(default='defaults/user_icon.png', 
        upload_to='user_icons')
    friends = models.ManyToManyField(get_user_model(), 
        blank=True, related_name='friends')
    slug = models.SlugField(unique=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, 
        default=GENDER_CHOICES[2],
        max_length=1)

    def __str__(self):
        return f"{self.user.username}-{self.created}"

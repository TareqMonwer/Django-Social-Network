from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from model_utils.models import TimeStampedModel
from django_countries.fields import CountryField

from .utils import get_random_code


class Profile(TimeStampedModel):
    GENDER_CHOICES = (
        ('m', 'Male'),
        ('m', 'Female'),
        ('u', 'Better Not Say')
    )
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
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
        return f"{self.user.username} - {self.created.strftime('%d %b %Y')}"

    def get_friends(self):
        return self.friends.all()

    def save(self, *args, **kwargs):
        ex = False
        if self.first_name:
            to_slug = slugify(str(self.first_name))
            ex = Profile.objects.filter(slug=to_slug)
            while ex:
                to_slug = slugify(to_slug + ' ' + str(get_random_code()))
                ex = Profile.objects.filter(slug=to_slug).exists()
        else:
            to_slug = slugify(self.user.username)
        self.slug = to_slug
        super().save(*args, **kwargs)


STATUS_CHOICES = (
    ('send', 'send'),
    ('accepted', 'accepted')
)


class Relationship(TimeStampedModel):
    sender = models.ForeignKey(Profile,
                               on_delete=models.CASCADE, related_name='sender')
    reciever = models.ForeignKey(Profile,
                                 on_delete=models.CASCADE, related_name='reciever')
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)

    def __str__(self):
        return (
            f"{self.sender} sent friend request to "
            f"{self.reciever} | status: {self.status}"
        )

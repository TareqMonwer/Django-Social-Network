from django.db import models
from django.core.validators import FileExtensionValidator
from model_utils.models import TimeStampedModel

from profiles.models import Profile


class PostImage(TimeStampedModel):
    image = models.ImageField(
        upload_to='post_images',
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])]
    )
    post = models.ForeignKey('Post', on_delete=models.CASCADE)


class Post(TimeStampedModel):
    content = models.TextField()
    images = models.ManyToManyField(PostImage, blank=True, related_name='post_images')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    likes = models.ManyToManyField(Profile, blank=True, related_name='likes')

    def __str__(self):
        return f"{self.content[:20]}"

    def number_of_likes(self):
        return self.likes.all().count()

    def number_of_comments(self):
        return self.comments.all().count()

    class Meta:
        ordering = ('-created', )


class Comment(TimeStampedModel):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()

    def __str__(self):
        return str(self.pk)


LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)


class Like(TimeStampedModel):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='liked')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, max_length=8)

    def __str__(self):
        return f"{self.user}-{self.post}-{self.value}"

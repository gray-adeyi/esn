from functools import _make_key
from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(
        User, related_name='author', on_delete=models.CASCADE)
    bio = models.TextField(help_text='A little something about you.')


class Category:
    """
    This model holds the post category.
    Note: a `Post` can belong to more than
    one category.
    """
    name = models.CharField(max_length=200)
    about = models.TextField(blank=True)
    poster = models.ImageField()

    def __str__(self) -> str:
        self.name


class Tag(models.Model):
    """
    This model shows the relationship between
    between `Post` instances. a post can have
    more than one `Tag`
    """
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

# Create your models here.


class Post(models.Model):
    """
    This model holds the blog post
    """
    OPTIONS = (
        ('publish', 'Publish'),
        ('draft', 'Draft'),
    )
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
    poster = models.ImageField(blank=True)
    brief = models.CharField(
        max_length=200, help_text="Optional* A summary of what the post is about", blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)
    state = models.CharField(max_length=20, choices=OPTIONS)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self) -> str:
        return self.title


class ContentMixin:
    """
    A mixin to for common functionalities required
    by the content models
    """

    def get_extension(self):
        # TODO: Use regular expressions to get file extension
        print(self.content)


class Text(models.Model):
    """
    This model holds the texts for a post
    """
    post = models.ForeignKey(Post, related_name='texts',
                             on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self) -> str:
        return self.post.title


class Image(models.Model):
    """
    This model holds the images for a post
    """
    post = models.ForeignKey(
        Post, related_name='images', on_delete=models.CASCADE)
    caption = models.CharField(max_length=200)
    content = models.ImageField()

    def __str__(self) -> str:
        return self.post.title


class Video(ContentMixin, models.Model):
    """
    This models holds the videos for a post
    """
    OPTIONS = (
        ('mp4', 'MP4'),
        ('mkv', 'MKV'),
        ('avi', 'AVI'),
        ('webm', 'WEBM'),
        ('others', 'OTHERS'),
    )
    post = models.ForeignKey(
        Post, related_name='videos', on_delete=models.CASCADE)
    caption = models.CharField(max_length=200)
    content = models.FileField()
    extension = models.CharField(
        max_length=20, choices=OPTIONS, default=OPTIONS[4][0])

    def __str__(self) -> str:
        return self.post.title


class Audio(ContentMixin, models.Model):
    """
    This model holds the audios for a post
    """
    OPTIONS = (
        ('mp3', 'mp3'),
        ('m4a', 'm4a'),
        ('others', 'OTHERS'),
    )

    post = models.ForeignKey(
        Post, related_name='audios', on_delete=models.CASCADE)
    caption = models.CharField(max_length=200)
    content = models.FileField()
    extension = models.CharField(
        max_length=20, choices=OPTIONS, default=OPTIONS[2][0])

    def __str__(self) -> str:
        return self.post.title

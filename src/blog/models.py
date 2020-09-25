from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name.title())

    def get_absolute_url(self):
        # return reverse("article_detail", args=(str(self.id)))
        return reverse("home")


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(
        null=True,
        blank=True,
        upload_to='img/profile/'
        )
    website_url = models.CharField(null=True, blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse("home")

    def __str__(self):
        return str(self.user)


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    snippet = models.CharField(max_length=150)
    body = RichTextField(blank=True, null=True)
    # body = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, blank=True)
    likes = models.ManyToManyField(User, related_name='blog_posts', blank=True)

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse("home")

    def __str__(self):
        return self.title + " | " + str(self.author)


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        related_name='comments',
        on_delete=models.CASCADE
        )
    name = models.CharField(max_length=50)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return f'{self.post.title} - {self.name}'

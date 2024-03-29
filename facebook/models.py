from django.db import models


class Article(models.Model):
    author = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    text = models.TextField(max_length=120)
    password = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Page(models.Model):
    master = models.CharField(max_length=120)
    name = models.CharField(max_length=120, default="호날두")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=120)
    text = models.TextField()
    password = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


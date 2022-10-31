from django.db import models

'''
Category
===========
title, slug(url category)

Tag
===========
title, slug(url category)

Post
===========
title, slug(url category), author, content, created_at, photo, views, category, tags
'''


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['title']


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    author = models.CharField(max_length=50, verbose_name='Author')
    content = models.TextField(max_length=255, verbose_name='Author', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Photo')
    views = models.IntegerField(default=0, verbose_name="Count views")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Category', related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_at']

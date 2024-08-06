#from curses.ascii import NUL
#from re import T
#from tabnanny import verbose
#from turtle import title

from distutils.command.upload import upload
from django.urls import reverse
from urllib import request
from django.shortcuts import render, redirect  
from venv import create
from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify

# Create your models here.

User = get_user_model()

class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    slug = models.SlugField(max_length=255, unique=True, blank=True, verbose_name="Slug")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Auteur")
    last_updated = models.DateField(blank=True, null=True, verbose_name="Dernière modification")
    created_on = models.DateField(blank=True, null=True, verbose_name="Créer")
    published = models.BooleanField(default=False, verbose_name="Publié")
    content = models.TextField(blank=True, verbose_name="Contenu")
    thumbnail = models.ImageField(blank=True, null=True, upload_to="blog", verbose_name='Image')

    class Meta:
        ordering = ['-created_on']
        verbose_name = "Article"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, *kwargs)
    
    @property
    def author_or_default(self):
        return self.author.username if self.author else "L'auteur inconnu"

    def get_absolute_url(self):
        return reverse("web:home")



    
        

        
    
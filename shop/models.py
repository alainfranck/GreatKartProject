from django.db import models
from django.utils.text import slugify
# Create your models here.
class Secusigne(models.Model):
    titre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, allow_unicode=True, blank=True)
    resume = models.CharField(max_length=200)
    description = models.TextField(max_length=10000, blank=True)
    image = models.ImageField(upload_to ='media/', null=True)

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titre)
        super(Secusigne, self).save(*args, **kwargs)


class Guide(models.Model):
    titre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, allow_unicode=True, blank=True)
    resume = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to ='media/', null=True)

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titre)
        super(Guide, self).save(*args, **kwargs)
from django.db import models
from django.utils import timezone

from ckeditor_uploader.fields import RichTextUploadingField
from slugify import slugify

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    #text = models.TextField()
    text = RichTextUploadingField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    #image = models.ImageField(upload_to='posts/image')
    slug = models.CharField(unique=True, blank=True, max_length=100)
    
    """   
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Person, self).save(*args, **kwargs)
    """
    def publish(self, *args, **kwargs):
        self.published_date = timezone.now()
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title + " - " + self.title
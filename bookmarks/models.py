from django.db import models

# Create your models here.

class Bookmark(models.Model):
    """Simple Bookmark model"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200, blank=True, default='')
    url = models.URLField()
    is_public = models.BooleanField(default=True)
    owner = models.ForeignKey('auth.User', related_name='bookmarks', on_delete=models.CASCADE)

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        ordering = ('created_at', 'updated_at')
        managed = True
        verbose_name = 'Bookmark'
        verbose_name_plural = 'Bookmarks'
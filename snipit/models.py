import hashlib
from django.db import models
from django.utils import timezone
from datetime import timedelta

class URL(models.Model):
    original_url = models.URLField()  # Original long URL
    short_url = models.CharField(max_length=15, unique=True)  # Shortened URL code
    created_at = models.DateTimeField(auto_now_add=True)  # When the short URL was created
    expiry_date = models.DateTimeField()  # Expiry date, 30 days from creation
    hit_count = models.IntegerField(default=0)  # Count of how many times it was accessed

    def save(self, *args, **kwargs):
        if not self.expiry_date:
            self.expiry_date = timezone.now() + timedelta(days=30)
        super(URL, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.original_url

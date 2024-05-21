import uuid
from django.db import models
from .utils import gen_random_url


class Campaign(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    goal = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name
    

class Offer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    local_url = models.CharField(max_length=10, unique=True)
    redirect_url = models.URLField(null=False, blank=False)
    referrer_url = models.URLField(null=False, blank=False)
    campaign = models.ForeignKey(Campaign, related_name='offers', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.url:
            self.url = f'{gen_random_url()}-redirect-link'
        super().save(*args, **kwargs)
    

class Lead(models.Model): # in this implementation Lead means Links entity and inherits its functionality
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    offer = models.ForeignKey(Offer, related_name='leads', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    browser = models.CharField(max_length=255, null=True, blank=True)
    os = models.CharField(max_length=255, null=True, blank=True)
    ip_address = models.GenericIPAddressField()
    geolocation = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'Lead on {self.offer}'

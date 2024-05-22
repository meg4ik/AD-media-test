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
        if not self.local_url:
            self.local_url = f'{gen_random_url()}-redirect-link'
        super().save(*args, **kwargs)

    
class Lead(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ip_address = models.GenericIPAddressField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Lead {self.ip_address}'
    
    
class Click(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    offer = models.ForeignKey(Offer, related_name='clicks', on_delete=models.CASCADE)
    lead = models.ForeignKey(Lead, related_name='clicks', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    browser = models.CharField(max_length=255, null=True, blank=True)
    os = models.CharField(max_length=255, null=True, blank=True)
    ip_address = models.GenericIPAddressField()
    geolocation = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'Click on {self.offer} by {self.lead}'

class LeadCampaignInterest(models.Model):
    INTEREST_CHOICES = [
        (0, 'Немає інформації'),
        (1, 'Дуже низька зацікавленість'),
        (2, 'Низька зацікавленість'),
        (3, 'Середня зацікавленість'),
        (4, 'Висока зацікавленість'),
        (5, 'Дуже висока зацікавленість'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lead = models.ForeignKey(Lead, related_name='campaign_interests', on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, related_name='lead_interests', on_delete=models.CASCADE)
    interest_score = models.IntegerField(choices=INTEREST_CHOICES, default=0)

    class Meta:
        unique_together = ('lead', 'campaign')

    def __str__(self):
        return f'{self.lead} - {self.campaign}: {self.interest_score}'
    
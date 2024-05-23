from rest_framework import serializers
from .models import Campaign, Offer, Lead, Click, LeadCampaignInterest
from .utils import gen_random_url

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'

class OfferSerializer(serializers.ModelSerializer):
    campaign_name = serializers.SerializerMethodField()

    class Meta:
        model = Offer
        fields = ['id', 'name', 'local_url', 'redirect_url', 'referrer_url', 'campaign', 'campaign_name', 'click_price']
        read_only_fields = ('local_url',)

    def create(self, validated_data):
        if 'local_url' not in validated_data:
            validated_data['local_url'] = gen_random_url()
        return super().create(validated_data)
    
    def get_campaign_name(self, obj):
        return obj.campaign.name

class LeadCampaignInterestSerializer(serializers.ModelSerializer):
    campaign_name = serializers.CharField(source='campaign.name', read_only=True)
    interest_score_display = serializers.CharField(source='get_interest_score_display', read_only=True)

    class Meta:
        model = LeadCampaignInterest
        fields = ['campaign_name', 'interest_score', 'interest_score_display']

class LeadSerializer(serializers.ModelSerializer):
    campaign_interests = LeadCampaignInterestSerializer(many=True, read_only=True)

    class Meta:
        model = Lead
        fields = ['id', 'ip_address', 'created_at', 'campaign_interests']

class ClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Click
        fields = '__all__'
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

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'

class ClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Click
        fields = '__all__'

class LeadCampaignInterestSerializer(serializers.ModelSerializer):
    interest_score_display = serializers.CharField(source='get_interest_score_display', read_only=True)

    class Meta:
        model = LeadCampaignInterest
        fields = '__all__'
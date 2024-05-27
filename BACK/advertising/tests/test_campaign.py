from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from advertising.models import Campaign
from advertising.serializers import CampaignSerializer

class CampaignViewSetTests(APITestCase):
    def setUp(self):
        self.campaign1 = Campaign.objects.create(name="Зимовий розпродаж", start_date="2024-12-01", end_date="2024-12-31", goal="Збільшити продажі зимових товарів на 20%")
        self.campaign2 = Campaign.objects.create(name="Весняна акція", start_date="2024-03-01", end_date="2024-03-31", goal="Привернути нових клієнтів")

    def test_list_campaigns(self):
        url = reverse('campaign-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = []
        while True:
            data += response.data['results']
            if not response.data['next']:
                break
            response = self.client.get(response.data['next'])

        self.assertEqual(len(data), 2)

        campaign_names = [campaign['name'] for campaign in data]
        self.assertIn(self.campaign1.name, campaign_names)
        self.assertIn(self.campaign2.name, campaign_names)

    def test_retrieve_campaign(self):
        url = reverse('campaign-detail', kwargs={'pk': self.campaign1.pk})
        response = self.client.get(url)
        campaign = Campaign.objects.get(pk=self.campaign1.pk)
        serializer = CampaignSerializer(campaign)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_campaign(self):
        url = reverse('campaign-list')
        data = {
            "name": "Літня розпродаж",
            "start_date": "2024-06-01",
            "end_date": "2024-08-31",
            "goal": "Реклама нових товарів"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Campaign.objects.count(), 3)

    def test_delete_campaign(self):
        url = reverse('campaign-detail', kwargs={'pk': self.campaign1.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Campaign.objects.count(), 1)
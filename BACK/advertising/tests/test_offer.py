from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from advertising.models import Offer, Campaign
from advertising.serializers import OfferSerializer

class OfferViewSetTests(APITestCase):
    def setUp(self):
        self.campaign = Campaign.objects.create(name="Зимовий розпродаж", start_date="2024-12-01", end_date="2024-12-31", goal="Збільшити продажі зимових товарів на 20%")
        self.offer1 = Offer.objects.create(name="Знижка 50% на зимові куртки", local_url="example1", redirect_url="https://example.com/winter-sale", referrer_url="https://example.com", campaign=self.campaign)
        self.offer2 = Offer.objects.create(name="Знижка 30% на зимові черевики", local_url="example2", redirect_url="https://example.com/boot-sale", referrer_url="https://example.com", campaign=self.campaign)


    def test_list_offers(self):
        url = reverse('offer-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = []
        while True:
            data += response.data['results']
            if not response.data['next']:
                break
            response = self.client.get(response.data['next'])

        self.assertEqual(len(data), 2)

        offer_names = [offer['name'] for offer in data]
        self.assertIn(self.offer1.name, offer_names)
        self.assertIn(self.offer2.name, offer_names)

    def test_retrieve_offer(self):
        url = reverse('offer-detail', kwargs={'pk': self.offer1.pk})
        response = self.client.get(url)
        offer = Offer.objects.get(pk=self.offer1.pk)
        serializer = OfferSerializer(offer)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_offer(self):
        url = reverse('offer-list')
        data = {
            "name": "Знижка 40% на зимові рукавички",
            "redirect_url": "https://example.com/glove-sale",
            "referrer_url": "https://example.com/offer2",
            "campaign": self.campaign.pk
        }
        response = self.client.post(url, data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Offer.objects.count(), 3)

    def test_delete_offer(self):
        url = reverse('offer-detail', kwargs={'pk': self.offer1.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Offer.objects.count(), 1)

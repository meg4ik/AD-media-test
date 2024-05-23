from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from advertising.models import Campaign, Offer, Lead, Click

class ClickViewSetTests(APITestCase):
    def setUp(self):
        self.campaign = Campaign.objects.create(
            name="Зимовий розпродаж",
            start_date="2024-12-01",
            end_date="2024-12-31",
            goal="Збільшити продажі зимових товарів на 20%"
        )
        self.offer = Offer.objects.create(
            name="Знижка 50% на зимові куртки",
            local_url="example1",
            redirect_url="https://example.com/winter-sale",
            referrer_url="https://example.com",
            campaign=self.campaign
        )
        self.lead = Lead.objects.create(
            ip_address="192.168.0.1"
        )
        self.click = Click.objects.create(
            offer=self.offer,
            lead=self.lead,
            browser="Firefox",
            os="Windows",
            ip_address="192.168.0.1",
            geolocation="Ukraine"
        )

    def test_list_clicks(self):
        url = reverse('click-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = []
        while True:
            data += response.data['results']
            if not response.data['next']:
                break
            response = self.client.get(response.data['next'])

        self.assertEqual(len(data), 1)

        click_ips = [click['ip_address'] for click in data]
        self.assertIn(self.click.ip_address, click_ips)

    def test_retrieve_click(self):
        url = reverse('click-detail', kwargs={'pk': self.click.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['ip_address'], self.click.ip_address)


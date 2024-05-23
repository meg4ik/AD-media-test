import React, { useState, useEffect } from 'react';
import axios from 'axios';
import ClickList from './ClickList';
import ClicksGraph from './ClicksGraph';

const Clicks = () => {
  const [campaigns, setCampaigns] = useState([]);
  const [offers, setOffers] = useState([]);
  const [selectedCampaignId, setSelectedCampaignId] = useState('');
  const [selectedOfferId, setSelectedOfferId] = useState('');

  const fetchCampaigns = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8088/api/campaigns/');
      setCampaigns(response.data.results);
    } catch (error) {
      console.error('Failed to fetch campaigns', error);
    }
  };

  const fetchOffers = async (campaignId) => {
    try {
      const response = await axios.get('http://127.0.0.1:8088/api/offers/', {
        params: {
          campaign: campaignId,
        },
      });
      setOffers(response.data.results);
    } catch (error) {
      console.error('Failed to fetch offers', error);
    }
  };

  useEffect(() => {
    fetchCampaigns();
  }, []);

  useEffect(() => {
    if (selectedCampaignId) {
      fetchOffers(selectedCampaignId);
    } else {
      setOffers([]);
    }
  }, [selectedCampaignId]);

  const handleCampaignChange = (e) => {
    setSelectedCampaignId(e.target.value);
    setSelectedOfferId('');
  };

  const handleOfferChange = (e) => {
    setSelectedOfferId(e.target.value);
  };

  return (
    <div className="container mx-auto p-4">
      <ClickList />
      <div className="mt-4">
        <label htmlFor="campaign-select" className="block mb-2 text-sm font-medium text-gray-900">Select Campaign</label>
        <select
          id="campaign-select"
          value={selectedCampaignId}
          onChange={handleCampaignChange}
          className="block w-full p-2 border border-gray-300 rounded"
        >
          <option value="">All Campaigns</option>
          {campaigns.map(campaign => (
            <option key={campaign.id} value={campaign.id}>
              {campaign.name}
            </option>
          ))}
        </select>
      </div>
      <div className="mt-4">
        <label htmlFor="offer-select" className="block mb-2 text-sm font-medium text-gray-900">Select Offer</label>
        <select
          id="offer-select"
          value={selectedOfferId}
          onChange={handleOfferChange}
          className="block w-full p-2 border border-gray-300 rounded"
          disabled={!selectedCampaignId}
        >
          <option value="">All Offers</option>
          {offers.map(offer => (
            <option key={offer.id} value={offer.id}>
              {offer.name}
            </option>
          ))}
        </select>
      </div>
      <ClicksGraph campaignId={selectedCampaignId} offerId={selectedOfferId} />
    </div>
  );
};

export default Clicks;

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import CampaignForm from './CampaignForm';
import CampaignList from './CampaignList';
import RevenueGraph from './RevenueGraph';

const Campaigns = () => {
  const [refresh, setRefresh] = useState(false);
  const [campaigns, setCampaigns] = useState([]);
  const [selectedCampaignId, setSelectedCampaignId] = useState('');

  const fetchCampaigns = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8088/api/campaigns/');
      setCampaigns(response.data.results);
    } catch (error) {
      console.error('Failed to fetch campaigns', error);
    }
  };

  useEffect(() => {
    fetchCampaigns();
  }, [refresh]);

  const handleAddCampaign = () => {
    setRefresh(!refresh);
  };

  const handleCampaignChange = (e) => {
    setSelectedCampaignId(e.target.value);
  };

  return (
    <div className="container mx-auto p-4">
      <CampaignForm onAddCampaign={handleAddCampaign} />
      <CampaignList key={refresh} />
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
      <RevenueGraph campaignId={selectedCampaignId} />
    </div>
  );
};

export default Campaigns;

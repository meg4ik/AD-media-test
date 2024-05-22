import React, { useState } from 'react';
import CampaignForm from './CampaignForm';
import CampaignList from './CampaignList';

const Campaigns = () => {
  const [refresh, setRefresh] = useState(false);

  const handleAddCampaign = () => {
    setRefresh(!refresh);
  };

  return (
    <div className="container mx-auto p-4">
      <CampaignForm onAddCampaign={handleAddCampaign} />
      <CampaignList key={refresh} />
    </div>
  );
};

export default Campaigns;

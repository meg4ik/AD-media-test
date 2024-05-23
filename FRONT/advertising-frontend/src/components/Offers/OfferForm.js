import React, { useState, useEffect } from 'react';
import axios from 'axios';

const OfferForm = ({ onAddOffer }) => {
  const [name, setName] = useState('');
  const [redirectUrl, setRedirectUrl] = useState('');
  const [referrerUrl, setReferrerUrl] = useState('');
  const [campaign, setCampaign] = useState('');
  const [clickPrice, setClickPrice] = useState('');
  const [campaigns, setCampaigns] = useState([]);

  useEffect(() => {
    const fetchCampaigns = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8088/api/campaigns/');
        setCampaigns(response.data.results);
      } catch (error) {
        console.error('Failed to fetch campaigns', error);
      }
    };

    fetchCampaigns();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:8088/api/offers/', {
        name,
        redirect_url: redirectUrl,
        referrer_url: referrerUrl,
        campaign,
        click_price: clickPrice,
      });
      setName('');
      setRedirectUrl('');
      setReferrerUrl('');
      setCampaign('');
      setClickPrice('');
      onAddOffer(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="mb-4">
      <div className="mb-2">
        <label className="block">Name</label>
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          className="border p-2 w-full"
          required
        />
      </div>
      <div className="mb-2">
        <label className="block">Redirect URL</label>
        <input
          type="url"
          value={redirectUrl}
          onChange={(e) => setRedirectUrl(e.target.value)}
          className="border p-2 w-full"
          required
        />
      </div>
      <div className="mb-2">
        <label className="block">Referrer URL</label>
        <input
          type="url"
          value={referrerUrl}
          onChange={(e) => setReferrerUrl(e.target.value)}
          className="border p-2 w-full"
          required
        />
      </div>
      <div className="mb-2">
        <label className="block">Campaign</label>
        <select
          value={campaign}
          onChange={(e) => setCampaign(e.target.value)}
          className="border p-2 w-full"
          required
        >
          <option value="">Select a campaign</option>
          {campaigns.map((camp) => (
            <option key={camp.id} value={camp.id}>
              {camp.name}
            </option>
          ))}
        </select>
      </div>
      <div className="mb-2">
        <label className="block">Click Price</label>
        <input
          type="number"
          step="0.01"
          value={clickPrice}
          onChange={(e) => setClickPrice(e.target.value)}
          className="border p-2 w-full"
          required
        />
      </div>
      <button type="submit" className="bg-blue-500 text-white p-2 rounded">
        Add Offer
      </button>
    </form>
  );
};

export default OfferForm;

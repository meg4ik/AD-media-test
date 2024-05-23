import React, { useState } from 'react';
import axios from 'axios';

const CampaignForm = ({ onAddCampaign }) => {
  const [name, setName] = useState('');
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');
  const [goal, setGoal] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const newCampaign = { name, start_date: startDate, end_date: endDate, goal };
    try {
      const response = await axios.post('http://127.0.0.1:8088/api/campaigns/', newCampaign);
      onAddCampaign(response.data);
      setName('');
      setStartDate('');
      setEndDate('');
      setGoal('');
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="mb-4 p-4 border rounded shadow">
      <h2 className="text-xl font-bold mb-2">Add New Campaign</h2>
      <div className="mb-2">
        <label className="block text-sm font-medium mb-1">Name</label>
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          className="w-full border p-2"
          required
        />
      </div>
      <div className="mb-2">
        <label className="block text-sm font-medium mb-1">Start Date</label>
        <input
          type="date"
          value={startDate}
          onChange={(e) => setStartDate(e.target.value)}
          className="w-full border p-2"
          required
        />
      </div>
      <div className="mb-2">
        <label className="block text-sm font-medium mb-1">End Date</label>
        <input
          type="date"
          value={endDate}
          onChange={(e) => setEndDate(e.target.value)}
          className="w-full border p-2"
          required
        />
      </div>
      <div className="mb-2">
        <label className="block text-sm font-medium mb-1">Goal</label>
        <input
          type="text"
          value={goal}
          onChange={(e) => setGoal(e.target.value)}
          className="w-full border p-2"
          required
        />
      </div>
      <button type="submit" className="bg-blue-600 text-white p-2 rounded">Add Campaign</button>
    </form>
  );
};

export default CampaignForm;

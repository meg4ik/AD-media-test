import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Pagination from '../Pagination';

const CampaignList = () => {
  const [campaigns, setCampaigns] = useState([]);
  const [loading, setLoading] = useState(true);
  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);
  const [filterInput, setFilterInput] = useState('');
  const [ordering, setOrdering] = useState('');

  const fetchCampaigns = async (page = 1, filter = '', order = '') => {
    setLoading(true);
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/campaigns/', {
        params: {
          page: page,
          search: filter,
          ordering: order,
        },
      });
      setCampaigns(response.data.results);
      setCurrentPage(page);
      setTotalPages(Math.ceil(response.data.count / 10));
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchCampaigns();
  }, []);

  const handleFilterChange = (e) => {
    const value = e.target.value || '';
    setFilterInput(value);
    fetchCampaigns(1, value, ordering);
  };

  const handlePageChange = (page) => {
    fetchCampaigns(page, filterInput, ordering);
  };

  const handleSortChange = (e) => {
    const value = e.target.value || '';
    setOrdering(value);
    fetchCampaigns(1, filterInput, value);
  };

  return (
    <div className="mt-4">
      <h2 className="text-xl font-bold mb-2">Campaigns List</h2>
      <input
        value={filterInput}
        onChange={handleFilterChange}
        placeholder="Search"
        className="mb-4 border p-2 w-full"
      />
      <select
        value={ordering}
        onChange={handleSortChange}
        className="mb-4 border p-2 w-full"
      >
        <option value="">Sort By</option>
        <option value="start_date">Start Date (Ascending)</option>
        <option value="-start_date">Start Date (Descending)</option>
        <option value="end_date">End Date (Ascending)</option>
        <option value="-end_date">End Date (Descending)</option>
      </select>
      <table className="w-full border-collapse border">
        <thead>
          <tr>
            <th className="border p-2">Name</th>
            <th className="border p-2">Start Date</th>
            <th className="border p-2">End Date</th>
            <th className="border p-2">Goal</th>
          </tr>
        </thead>
        <tbody>
          {campaigns.map(campaign => (
            <tr key={campaign.id}>
              <td className="border p-2">{campaign.name}</td>
              <td className="border p-2">{campaign.start_date}</td>
              <td className="border p-2">{campaign.end_date}</td>
              <td className="border p-2">{campaign.goal}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <Pagination
        currentPage={currentPage}
        totalPages={totalPages}
        onPageChange={handlePageChange}
      />
    </div>
  );
};

export default CampaignList;

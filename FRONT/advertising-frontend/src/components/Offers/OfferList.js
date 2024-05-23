import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Pagination from '../Pagination';

const OfferList = () => {
  const [offers, setOffers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);
  const [filterInput, setFilterInput] = useState('');
  const [ordering, setOrdering] = useState('');

  const fetchOffers = async (page = 1, filter = '', order = '') => {
    setLoading(true);
    try {
      const response = await axios.get('http://127.0.0.1:8088/api/offers/', {
        params: {
          page: page,
          search: filter,
          ordering: order,
        },
      });
      setOffers(response.data.results);
      setCurrentPage(page);
      setTotalPages(Math.ceil(response.data.count / 10));
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchOffers();
  }, []);

  const handleFilterChange = (e) => {
    const value = e.target.value || '';
    setFilterInput(value);
    fetchOffers(1, value, ordering);
  };

  const handlePageChange = (page) => {
    fetchOffers(page, filterInput, ordering);
  };

  const handleSortChange = (e) => {
    const value = e.target.value || '';
    setOrdering(value);
    fetchOffers(1, filterInput, value);
  };

  return (
    <div className="mt-4">
      <h2 className="text-xl font-bold mb-2">Offers List</h2>
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
        <option value="name">Name (A-Z)</option>
        <option value="-name">Name (Z-A)</option>
        <option value="click_price">Click Price (Ascending)</option>
        <option value="-click_price">Click Price (Descending)</option>
      </select>
      <table className="w-full border-collapse border">
        <thead>
          <tr>
            <th className="border p-2">Name</th>
            <th className="border p-2">Redirect URL</th>
            <th className="border p-2">Referrer URL</th>
            <th className="border p-2">Campaign</th>
            <th className="border p-2">Click Price</th>
            <th className="border p-2">Local URL</th>
          </tr>
        </thead>
        <tbody>
          {offers.map(offer => (
            <tr key={offer.id}>
              <td className="border p-2">{offer.name}</td>
              <td className="border p-2">{offer.redirect_url}</td>
              <td className="border p-2">{offer.referrer_url}</td>
              <td className="border p-2">{offer.campaign_name}</td>
              <td className="border p-2">{offer.click_price}</td>
              <td className="border p-2">
                <a href={`http://127.0.0.1:8088/r/${offer.local_url}`} className="text-blue-500 hover:underline">
                  {`http://127.0.0.1:8088/r/${offer.local_url}`}
                </a>
              </td>
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

export default OfferList;

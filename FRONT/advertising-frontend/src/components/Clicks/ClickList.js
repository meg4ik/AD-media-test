import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Pagination from '../Pagination';

const ClickList = () => {
  const [clicks, setClicks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);

  const fetchClicks = async (page = 1) => {
    setLoading(true);
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/clicks/', {
        params: {
          page: page,
        },
      });
      setClicks(response.data.results);
      setCurrentPage(page);
      setTotalPages(Math.ceil(response.data.count / 10));
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchClicks();
  }, []);

  const handlePageChange = (page) => {
    fetchClicks(page);
  };

  return (
    <div className="mt-4">
      <h2 className="text-xl font-bold mb-2">Clicks List</h2>
      <table className="w-full border-collapse border">
        <thead>
          <tr>
            <th className="border p-2">Timestamp</th>
            <th className="border p-2">IP Address</th>
            <th className="border p-2">Browser</th>
            <th className="border p-2">OS</th>
            <th className="border p-2">Geolocation</th>
            <th className="border p-2">Campaign</th>
            <th className="border p-2">Offer</th>
          </tr>
        </thead>
        <tbody>
          {clicks.map(click => (
            <tr key={click.id}>
              <td className="border p-2">{new Date(click.timestamp).toLocaleString()}</td>
              <td className="border p-2">{click.ip_address}</td>
              <td className="border p-2">{click.browser}</td>
              <td className="border p-2">{click.os}</td>
              <td className="border p-2">{click.geolocation}</td>
              <td className="border p-2">{click.campaign_name}</td>
              <td className="border p-2">{click.offer_name}</td>
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

export default ClickList;

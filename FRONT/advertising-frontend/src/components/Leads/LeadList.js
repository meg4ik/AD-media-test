import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Pagination from '../Pagination';

const LeadList = () => {
  const [leads, setLeads] = useState([]);
  const [loading, setLoading] = useState(true);
  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);

  const fetchLeads = async (page = 1) => {
    setLoading(true);
    try {
      const response = await axios.get('/api/leads/', {
        params: {
          page: page,
        },
      });
      setLeads(response.data.results);
      setCurrentPage(page);
      setTotalPages(Math.ceil(response.data.count / 10));
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchLeads();
  }, []);

  const handlePageChange = (page) => {
    fetchLeads(page);
  };

  return (
    <div className="mt-4">
      <h2 className="text-xl font-bold mb-2">Leads List</h2>
      <table className="w-full border-collapse border">
        <thead>
          <tr>
            <th className="border p-2">IP Address</th>
            <th className="border p-2">Created At</th>
          </tr>
        </thead>
        <tbody>
          {leads.map(lead => (
            <tr key={lead.id}>
              <td className="border p-2">{lead.ip_address}</td>
              <td className="border p-2">{new Date(lead.created_at).toLocaleString()}</td>
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

export default LeadList;

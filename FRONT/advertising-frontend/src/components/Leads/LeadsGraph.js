import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Line } from 'react-chartjs-2';

import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
  } from 'chart.js';
  
  ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
  );

const LeadsGraph = () => {
  const [graphData, setGraphData] = useState({ labels: [], datasets: [] });

  useEffect(() => {
    const fetchGraphData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8088/graphs/leads/');
        const data = response.data;
        
        const labels = data.map(entry => entry.day);
        const leadCounts = data.map(entry => entry.count);
        
        setGraphData({
          labels: labels,
          datasets: [
            {
              label: 'Leads',
              data: leadCounts,
              borderColor: 'rgba(75, 192, 192, 1)',
              backgroundColor: 'rgba(75, 192, 192, 0.2)',
              fill: true,
            },
          ],
        });
      } catch (error) {
        console.error('Failed to fetch graph data', error);
      }
    };

    fetchGraphData();
  }, []);

  return (
    <div className="mt-8">
      <h2 className="text-xl font-bold mb-2">Leads Over Time</h2>
      <Line data={graphData} />
    </div>
  );
};

export default LeadsGraph;

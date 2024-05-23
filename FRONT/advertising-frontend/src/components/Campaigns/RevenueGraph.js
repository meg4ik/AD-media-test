import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import axios from 'axios';
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

const RevenueGraph = ({ campaignId }) => {
  const [graphData, setGraphData] = useState({ labels: [], datasets: [] });

  useEffect(() => {
    const fetchGraphData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/graphs/revenue/', {
          params: {
            campaign_id: campaignId,
          },
        });
        const data = response.data;
        
        const labels = data.map(entry => entry.day);
        const revenueAmounts = data.map(entry => entry.revenue);
        
        setGraphData({
          labels: labels,
          datasets: [
            {
              label: 'Revenue',
              data: revenueAmounts,
              borderColor: 'rgba(255, 99, 132, 1)',
              backgroundColor: 'rgba(255, 99, 132, 0.2)',
              fill: true,
            },
          ],
        });
      } catch (error) {
        console.error('Failed to fetch graph data', error);
      }
    };

    fetchGraphData();
  }, [campaignId]);

  return (
    <div className="mt-8">
      <h2 className="text-xl font-bold mb-2">Revenue Over Time</h2>
      <Line data={graphData} />
    </div>
  );
};

export default RevenueGraph;

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

const ClicksGraph = ({ campaignId, offerId }) => {
  const [graphData, setGraphData] = useState({ labels: [], datasets: [] });

  useEffect(() => {
    const fetchGraphData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:808/graphs/clicks/', {
          params: {
            campaign_id: campaignId,
            offer_id: offerId,
          },
        });
        const data = response.data;
        
        const labels = data.map(entry => entry.day);
        const clickCounts = data.map(entry => entry.count);
        
        setGraphData({
          labels: labels,
          datasets: [
            {
              label: 'Clicks',
              data: clickCounts,
              borderColor: 'rgba(54, 162, 235, 1)',
              backgroundColor: 'rgba(54, 162, 235, 0.2)',
              fill: true,
            },
          ],
        });
      } catch (error) {
        console.error('Failed to fetch graph data', error);
      }
    };

    fetchGraphData();
  }, [campaignId, offerId]);

  return (
    <div className="mt-8">
      <h2 className="text-xl font-bold mb-2">Clicks Over Time</h2>
      <Line data={graphData} />
    </div>
  );
};

export default ClicksGraph;

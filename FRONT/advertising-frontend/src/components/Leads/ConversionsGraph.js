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

const ConversionsGraph = () => {
  const [graphData, setGraphData] = useState({ labels: [], datasets: [] });

  useEffect(() => {
    const fetchGraphData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/graphs/conversions/');
        const data = response.data;
        
        const labels = data.map(entry => entry.day);
        const conversionCounts = data.map(entry => entry.count);
        
        setGraphData({
          labels: labels,
          datasets: [
            {
              label: 'Conversions',
              data: conversionCounts,
              borderColor: 'rgba(153, 102, 255, 1)',
              backgroundColor: 'rgba(153, 102, 255, 0.2)',
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
      <h2 className="text-xl font-bold mb-2">Conversions Over Time</h2>
      <Line data={graphData} />
    </div>
  );
};

export default ConversionsGraph;

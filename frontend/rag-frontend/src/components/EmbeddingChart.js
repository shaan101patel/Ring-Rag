// src/components/EmbeddingsChart.js
import React from 'react';
import { Scatter } from 'react-chartjs-2';

function EmbeddingsChart() {
  // Example data for embeddings in 2D
  const data = {
    datasets: [
      {
        label: 'Embeddings',
        data: [
          { x: 10, y: 20 },
          { x: 15, y: 10 },
          { x: 20, y: 40 },
          { x: 25, y: 30 }
        ],
        backgroundColor: 'rgba(75,192,192,1)'
      }
    ]
  };

  const options = {
    scales: {
      x: { title: { display: true, text: 'X Axis' } },
      y: { title: { display: true, text: 'Y Axis' } }
    }
  };

  return <Scatter data={data} options={options} />;
}

export default EmbeddingsChart;

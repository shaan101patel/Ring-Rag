// src/pages/Queries.js
import React, { useState } from 'react';

function Queries() {
  const [query, setQuery] = useState('');
  const [currentStep, setCurrentStep] = useState('Idle');
  const [result, setResult] = useState('');

  const handleQueryChange = (e) => {
    setQuery(e.target.value);
  };

  const handleSearch = async () => {
    // Show initial step
    setCurrentStep('Sending query to backend...');
    setResult('');

    try {
      // POST the query text to your Flask endpoint
      const response = await fetch('http://localhost:5000/query', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query_text: query }),
      });

      if (!response.ok) {
        throw new Error(`Server error: ${response.status}`);
      }

      // Backend returns JSON with "answer" field
      const data = await response.json();
      setResult(data.answer || 'No answer returned.');
      setCurrentStep('Complete');
    } catch (error) {
      console.error('Error during query:', error);
      setCurrentStep('Error');
      setResult('Something went wrong.');
    }
  };

  return (
    <div style={styles.container}>
      <h2>User Queries</h2>
      <div style={styles.queryContainer}>
        <input
          type="text"
          placeholder="Enter your query..."
          value={query}
          onChange={handleQueryChange}
          style={styles.queryInput}
        />
        <button onClick={handleSearch}>Search</button>
      </div>

      <div style={styles.statusContainer}>
        <h4>Current Step: {currentStep}</h4>
      </div>

      <div style={styles.resultContainer}>
        {result && <p>Final Result: {result}</p>}
      </div>
    </div>
  );
}

const styles = {
  container: {
    padding: '1rem',
  },
  queryContainer: {
    display: 'flex',
    gap: '1rem',
    marginBottom: '1rem',
  },
  queryInput: {
    flex: '1',
  },
  statusContainer: {
    margin: '1rem 0',
  },
  resultContainer: {
    margin: '1rem 0',
  },
};

export default Queries;

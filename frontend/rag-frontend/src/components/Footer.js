// src/components/Footer.js
import React from 'react';
import { useNavigate } from 'react-router-dom';

function Footer() {
  const navigate = useNavigate();

  return (
    <div className="footer">
      <button onClick={() => navigate('/')}>
        Go to Home
      </button>
    </div>
  );
}

export default Footer;

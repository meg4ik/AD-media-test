import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './components/Home';
import Campaigns from './components/Campaigns/Campaigns';
import Offers from './components/Offers/Offers';
import Leads from './components/Leads/Leads';
import Clicks from './components/Clicks';

const App = () => {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/campaigns" element={<Campaigns />} />
        <Route path="/offers" element={<Offers />} />
        <Route path="/leads" element={<Leads />} />
        <Route path="/clicks" element={<Clicks />} />
      </Routes>
    </Router>
  );
};

export default App;

import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="bg-blue-600 p-4 text-white">
      <div className="container mx-auto flex justify-between">
        <Link to="/" className="text-lg font-bold">Advertising App</Link>
        <div className="flex space-x-4">
          <Link to="/campaigns" className="hover:underline">Campaigns</Link>
          <Link to="/offers" className="hover:underline">Offers</Link>
          <Link to="/leads" className="hover:underline">Leads</Link>
          <Link to="/clicks" className="hover:underline">Clicks</Link>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;

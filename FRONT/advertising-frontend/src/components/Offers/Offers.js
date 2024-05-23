import React, { useState } from 'react';
import OfferForm from './OfferForm';
import OfferList from './OfferList';

const Offers = () => {
  const [refresh, setRefresh] = useState(false);

  const handleAddOffer = () => {
    setRefresh(!refresh);
  };

  return (
    <div className="container mx-auto p-4">
      <OfferForm onAddOffer={handleAddOffer} />
      <OfferList key={refresh} />
    </div>
  );
};

export default Offers;

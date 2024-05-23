import React from 'react';
import LeadList from './LeadList';
import LeadsGraph from './LeadsGraph';
import ConversionsGraph from './ConversionsGraph';

const Leads = () => {
  return (
    <div className="container mx-auto p-4">
      <LeadList />
      <LeadsGraph />
      <ConversionsGraph />
    </div>
  );
};

export default Leads;

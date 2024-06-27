// src/components/Results.js

import React, { useEffect, useState } from 'react';

function Results() {
  const [allocations, setAllocations] = useState([]);

  useEffect(() => {
    fetch('/get-allocations')
      .then(response => response.json())
      .then(data => setAllocations(data));
  }, []);

  return (
    <div>
      <h2>Room Allocations</h2>
      <table>
        <thead>
          <tr>
            <th>Group ID</th>
            <th>Hostel Name</th>
            <th>Room Number</th>
            <th>Members Allocated</th>
          </tr>
        </thead>
        <tbody>
          {allocations.map((allocation, index) => (
            <tr key={index}>
              <td>{allocation.group_id}</td>
              <td>{allocation.hostel_name}</td>
              <td>{allocation.room_number}</td>
              <td>{allocation.members_allocated}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Results;

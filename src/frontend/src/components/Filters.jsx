import React from "react";

export default function Filters({ startDate, endDate, setStartDate, setEndDate }) {
  return (
    <div style={{ marginBottom: 20 }}>
      <label style={{ marginRight: 10 }}>Start Date:</label>
      <input type="date" value={startDate} onChange={e => setStartDate(e.target.value)} />
      <label style={{ margin: "0 10px" }}>End Date:</label>
      <input type="date" value={endDate} onChange={e => setEndDate(e.target.value)} />
    </div>
  );
}

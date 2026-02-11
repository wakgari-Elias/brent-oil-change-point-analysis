import React from "react";

export default function EventOverlay({ data }) {
  if (!data || data.length === 0) return <p>No events loaded</p>;

  return (
    <div style={{ marginTop: 20 }}>
      <h3 style={{ fontSize: 18 }}>Events</h3>
      <ul>
        {data.map((e, i) => (
          <li key={i} style={{ marginBottom: 5 }}>
            <strong>{e.Date}</strong>: {e.Event}
          </li>
        ))}
      </ul>
    </div>
  );
}

import React from "react";
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

export default function PriceChart({ data }) {
  if (!data || data.length === 0) return <p>Loading prices...</p>;

  return (
    <div style={{ width: "100%", height: 400, marginBottom: 50 }}>
      <ResponsiveContainer>
        <LineChart data={data}>
          <XAxis dataKey="Date" />
          <YAxis />
          <Tooltip />
          <Line type="monotone" dataKey="Price" stroke="#8884d8" dot={false} />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}

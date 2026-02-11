import React from "react";
import { ScatterChart, Scatter, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

export default function ChangePointChart({ data }) {
  if (!data || data.length === 0) return <p>No change points data...</p>;

  return (
    <div style={{ width: "100%", height: 200 }}>
      <ResponsiveContainer>
        <ScatterChart>
          <XAxis dataKey="Date" />
          <YAxis />
          <Tooltip />
          <Scatter name="Change Points" data={data} fill="red" />
        </ScatterChart>
      </ResponsiveContainer>
    </div>
  );
}

import React, { useState, useEffect } from "react";
import { fetchPrices, fetchChangePoints, fetchEvents } from "../services/api";
import PriceChart from "../components/PriceChart";
import ChangePointChart from "../components/ChangePointChart";
import EventOverlay from "../components/EventOverlay";
import Filters from "../components/Filters";

export default function Dashboard() {
  const [prices, setPrices] = useState([]);
  const [changePoints, setChangePoints] = useState([]);
  const [events, setEvents] = useState([]);
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");

  useEffect(() => {
    fetchPrices().then(setPrices);
    fetchChangePoints().then(setChangePoints);
    fetchEvents().then(setEvents);
  }, []);

  const filteredPrices = prices.filter(p => {
    if (!startDate || !endDate) return true;
    return p.Date >= startDate && p.Date <= endDate;
  });

  const filteredChangePoints = changePoints.filter(cp => {
    if (!startDate || !endDate) return true;
    return cp.Date >= startDate && cp.Date <= endDate;
  });

  const filteredEvents = events.filter(ev => {
    if (!startDate || !endDate) return true;
    return ev.Date >= startDate && ev.Date <= endDate;
  });

  return (
    <div style={{ padding: 20 }}>
      <h1 style={{ textAlign: "center" }}>Brent Oil Price Dashboard</h1>
      <Filters
        startDate={startDate}
        endDate={endDate}
        setStartDate={setStartDate}
        setEndDate={setEndDate}
      />
      <PriceChart data={filteredPrices} />
      <ChangePointChart data={filteredChangePoints} />
      <EventOverlay data={filteredEvents} />
    </div>
  );
}

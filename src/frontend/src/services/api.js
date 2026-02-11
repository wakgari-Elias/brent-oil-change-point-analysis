import axios from "axios";

const BASE_URL = "http://127.0.0.1:5000/api";

export const fetchPrices = async () => {
  const res = await axios.get(`${BASE_URL}/prices/`);
  return res.data;
};

export const fetchChangePoints = async () => {
  const res = await axios.get(`${BASE_URL}/changepoints/`);
  return res.data;
};

export const fetchEvents = async () => {
  const res = await axios.get(`${BASE_URL}/events/`);
  return res.data;
};

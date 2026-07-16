import api from "./api";

export const getDonations = () =>
  api.get("/donations");

export const getDonation = (id) =>
  api.get(`/donations/${id}`);

export const createDonation = (data) =>
  api.post("/donations", data);

export const updateDonation = (id, data) =>
  api.put(`/donations/${id}`, data);

export const deleteDonation = (id) =>
  api.delete(`/donations/${id}`);
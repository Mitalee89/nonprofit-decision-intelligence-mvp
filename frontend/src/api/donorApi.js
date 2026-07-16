import api from "./api";

export const getDonors = () => api.get("/donors");

export const getDonor = (id) =>
    api.get(`/donors/${id}`);

export const createDonor = (data) =>
    api.post("/donors", data);

export const updateDonor = (id, data) =>
    api.put(`/donors/${id}`, data);

export const deleteDonor = (id) =>
    api.delete(`/donors/${id}`);
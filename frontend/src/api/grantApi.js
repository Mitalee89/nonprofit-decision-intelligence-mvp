import api from "./api";

export const getGrants = () =>
    api.get("/grants");

export const getGrant = (id) =>
    api.get(`/grants/${id}`);

export const createGrant = (data) =>
    api.post("/grants", data);

export const updateGrant = (id, data) =>
    api.put(`/grants/${id}`, data);

export const deleteGrant = (id) =>
    api.delete(`/grants/${id}`);
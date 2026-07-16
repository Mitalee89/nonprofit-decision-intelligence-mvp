import api from "./api";

export const getFunds = () =>
    api.get("/funds");

export const getFund = (id) =>
    api.get(`/funds/${id}`);
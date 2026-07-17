import api from "./api";

export const getGrants = async () => {
    return await api.get("/grants");
};

export const createGrant = async (grant) => {
    return await api.post("/grants", grant);
};

export const updateGrant = async (id, grant) => {
    return await api.put(`/grants/${id}`, grant);
};

export const deleteGrant = async (id) => {
    return await api.delete(`/grants/${id}`);
};

export const recommendGrants = async (campaignId) => {
    return await api.post(
        `/ai/recommend-grants/${campaignId}`
    );
};
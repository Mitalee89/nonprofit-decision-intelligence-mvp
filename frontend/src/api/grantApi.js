import api from "./api";

export const recommendGrants = async (campaignId) => {
    const response = await api.post(
        `/ai/recommend-grants/${campaignId}`
    );

    return response.data;
};
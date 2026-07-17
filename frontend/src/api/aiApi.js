import api from "./api";

export const recommendDonors = async (campaignId) => {
    const response = await api.post(
        `/ai/recommend-donors/${campaignId}`
    );

    return response.data;
};
import { useEffect, useState } from "react";

import WorkflowTimeline from "../components/workflow/WorkflowTimeline";
import RecommendationCard from "../components/workflow/RecommendationCard";
import RecommendationTable from "../components/workflow/RecommendationTable";

import { getCampaigns } from "../api/campaignApi";
import { recommendDonors } from "../api/aiApi";

import GrantRecommendationTable from "../components/workflow/GrantRecommendationTable";
import { recommendGrants } from "../api/grantApi";

export default function Workflow() {
    const [campaigns, setCampaigns] = useState([]);
    const [selectedCampaign, setSelectedCampaign] = useState("");

    const [recommendations, setRecommendations] = useState([]);
    const [loading, setLoading] = useState(false);

    const [grantRecommendations, setGrantRecommendations] = useState([]);
    const [grantLoading, setGrantLoading] = useState(false);

    useEffect(() => {
        loadCampaigns();
    }, []);

    async function loadCampaigns() {
    try {

        const response = await getCampaigns();

        const campaigns = Array.isArray(response)
            ? response
            : response.data;

        setCampaigns(campaigns);

        if (campaigns.length > 0) {
            setSelectedCampaign(campaigns[0].id);
        }

    } catch (err) {

        console.error(err);
        alert("Unable to load campaigns.");

    }
}

    async function runRecommendation() {

        if (!selectedCampaign) return;

        setLoading(true);

        try {

            const response = await recommendDonors(selectedCampaign);

            const recommendations =
                response?.data ??
                response ??
                [];

            setRecommendations(
                Array.isArray(recommendations)
                    ? recommendations
                    : []
            );

        } catch (err) {

            console.error(err);

            alert(
                err.response?.data?.detail ??
                err.message ??
                "Unable to generate donor recommendations."
            );

            setRecommendations([]);

        } finally {

            setLoading(false);

        }
    }

    async function runGrantRecommendation() {

    if (!selectedCampaign) return;

    setGrantLoading(true);

    try {

        const response = await recommendGrants(selectedCampaign);

        const recommendations =
            response?.data ??
            response ??
            [];

        setGrantRecommendations(
            Array.isArray(recommendations)
                ? recommendations
                : []
        );

    } catch (err) {

        console.error(err);

        alert(
            err.response?.data?.detail ??
            err.message ??
            "Unable to generate grant recommendations."
        );

        setGrantRecommendations([]);

    } finally {

        setGrantLoading(false);

    }
}
    return (
        <div className="space-y-8 p-6">

            <h1 className="text-3xl font-bold">
                AI Workflow
            </h1>

            <WorkflowTimeline />

            <div className="bg-white rounded-xl shadow p-6">

                <h2 className="text-xl font-semibold mb-4">
                    Select Campaign
                </h2>

                <select
                    value={selectedCampaign}
                    onChange={(e) =>
                        setSelectedCampaign(Number(e.target.value))
                    }
                    className="w-full border rounded-lg p-3"
                >
                    {campaigns.map((campaign) => (
                        <option
                            key={campaign.id}
                            value={campaign.id}
                        >
                            {campaign.name}
                        </option>
                    ))}
                </select>

            </div>

            <RecommendationCard
                title="AI Donor Recommendation"
                description="Find the most suitable donors for the selected campaign using the LLM recommendation engine."
                buttonText={
                    loading
                        ? "Generating..."
                        : "Recommend Donors"
                }
                onClick={runRecommendation}
            />

            <RecommendationCard
                title="AI Grant Recommendation"
                description="Find the most suitable grants for the selected campaign using the LLM recommendation engine."
                buttonText={
                    grantLoading
                        ? "Generating..."
                        : "Recommend Grants"
                }
                onClick={runGrantRecommendation}
            />

            {loading && (
                <div className="bg-blue-50 border border-blue-200 rounded-lg p-4 text-blue-700 font-medium">
                    Generating donor recommendations...
                </div>
            )}

            {grantLoading && (
                <div className="bg-green-50 border border-green-200 rounded-lg p-4 text-green-700 font-medium">
                    Generating grant recommendations...
                </div>
            )}

            <RecommendationTable
                recommendations={recommendations}
            />

            <GrantRecommendationTable
                recommendations={grantRecommendations}
            />

        </div>
    );
}
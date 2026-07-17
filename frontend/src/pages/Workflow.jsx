import { useEffect, useState } from "react";

import WorkflowTimeline from "../components/workflow/WorkflowTimeline";
import RecommendationCard from "../components/workflow/RecommendationCard";
import RecommendationTable from "../components/workflow/RecommendationTable";

import { getCampaigns } from "../api/campaignApi";
import { recommendDonors } from "../api/aiApi";

export default function Workflow() {
    const [campaigns, setCampaigns] = useState([]);
    const [selectedCampaign, setSelectedCampaign] = useState("");

    const [recommendations, setRecommendations] = useState([]);
    const [loading, setLoading] = useState(false);

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

        const recommendations = await recommendDonors(selectedCampaign);

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
console.log("Current recommendations state:", recommendations);
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

            {loading && (
                <div className="bg-blue-50 border border-blue-200 rounded-lg p-4 text-blue-700 font-medium">
                    Generating donor recommendations...
                </div>
            )}

            <RecommendationTable
                recommendations={recommendations}
            />

        </div>
    );
}
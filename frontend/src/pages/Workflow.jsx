import WorkflowTimeline from "../components/workflow/WorkflowTimeline";

import RecommendationCard from "../components/workflow/RecommendationCard";

import RecommendationTable from "../components/workflow/RecommendationTable";

export default function Workflow(){

    return(

        <div className="space-y-6">

            <h1 className="text-3xl font-bold">

                AI Workflow

            </h1>

            <WorkflowTimeline/>

            <div className="grid grid-cols-2 gap-6">

                <RecommendationCard

                    title="Donor Recommendation Engine"

                    description="Find the best donors for a campaign."

                    buttonText="Recommend Donors"

                    onClick={()=>{}}

                />

                <RecommendationCard

                    title="Grant Recommendation Engine"

                    description="Find the best grants for a campaign."

                    buttonText="Recommend Grants"

                    onClick={()=>{}}

                />

            </div>

            <RecommendationTable

                title="Recommendations"

            />

        </div>

    )

}
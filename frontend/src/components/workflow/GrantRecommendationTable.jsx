function getBadgeColor(score) {

    if (score >= 90)
        return "bg-green-100 text-green-700";

    if (score >= 75)
        return "bg-yellow-100 text-yellow-700";

    return "bg-red-100 text-red-700";
}

export default function GrantRecommendationTable({
    recommendations,
}) {

    if (!Array.isArray(recommendations))
        recommendations = [];

    if (recommendations.length === 0) {

        return (

            <div className="text-gray-500 text-center py-8">

                No grant recommendations generated yet.

            </div>

        );

    }

    return (

        <div className="bg-white rounded-lg shadow">

            <table className="w-full">

                <thead>

                    <tr className="border-b">

                        <th className="text-left p-4">
                            Grant
                        </th>

                        <th className="text-left p-4">
                            Confidence
                        </th>

                        <th className="text-left p-4">
                            Reasoning
                        </th>

                    </tr>

                </thead>

                <tbody>

                    {recommendations.map((recommendation) => (

                        <tr
                            key={recommendation.grant_id}
                            className="border-b"
                        >

                            <td className="p-4">

                                {recommendation.grant_name}

                            </td>

                            <td className="p-4">

                                <span
                                    className={`px-3 py-1 rounded-full text-sm font-medium ${getBadgeColor(
                                        recommendation.confidence_score
                                    )}`}
                                >

                                    {recommendation.confidence_score}%

                                </span>

                            </td>

                            <td className="p-4">

                                {recommendation.reasoning}

                            </td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </div>

    );

}
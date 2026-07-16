export default function RecommendationTable({
    title,
}) {

    return (

        <div className="bg-white rounded-xl shadow p-6">

            <h2 className="text-xl font-semibold mb-4">
                {title}
            </h2>

            <p className="text-gray-500">
                No recommendations generated yet.
            </p>

        </div>

    );

}
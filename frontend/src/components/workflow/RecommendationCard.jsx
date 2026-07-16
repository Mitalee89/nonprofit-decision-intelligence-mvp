export default function RecommendationCard({

    title,

    description,

    buttonText,

    onClick,

}){

    return(

        <div className="bg-white rounded-xl shadow p-6">

            <h2 className="text-xl font-semibold">

                {title}

            </h2>

            <p className="text-gray-600 mt-3">

                {description}

            </p>

            <button

                onClick={onClick}

                className="mt-5 bg-blue-600 text-white px-4 py-2 rounded"

            >

                {buttonText}

            </button>

        </div>

    )

}
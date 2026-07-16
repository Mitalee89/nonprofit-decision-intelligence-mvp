export default function WorkflowTimeline() {

    const steps = [

        "Campaign Created",

        "Fund Created",

        "Donations Received",

        "Recommend Donors",

        "Recommend Grants"

    ];

    return (

        <div className="bg-white rounded-xl shadow p-6">

            <h2 className="text-xl font-semibold mb-6">
                Workflow
            </h2>

            <div className="flex justify-between items-center">

                {steps.map((step,index)=>(

                    <div
                        key={index}
                        className="flex flex-col items-center flex-1"
                    >

                        <div className="w-10 h-10 rounded-full bg-blue-600 text-white flex items-center justify-center">

                            {index+1}

                        </div>

                        <p className="mt-2 text-center text-sm">

                            {step}

                        </p>

                    </div>

                ))}

            </div>

        </div>

    );

}
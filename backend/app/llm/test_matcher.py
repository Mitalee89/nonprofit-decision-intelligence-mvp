from app.llm.donor_matcher import recommend_donors

campaign = {
    "name": "Education For All",
    "description": "Provide digital education to children.",
    "goal_amount": 500000,
    "amount_raised": 100000,
    "status": "ACTIVE",
}

donors = [

    {
        "id": 1,
        "name": "Infosys Foundation",
        "preferred_cause": "Education",
        "interests": "Education, Women Empowerment",
        "capacity": 500000,
        "city": "New York",
    },

    {
        "id": 2,
        "name": "Mike Bay",
        "preferred_cause": "Healthcare",
        "interests": "Hospitals",
        "capacity": 50000,
        "city": "Chicago",
    },

    {
        "id": 3,
        "name": "Susy Thomas",
        "preferred_cause": "Education",
        "interests": "Education, Child Welfare",
        "capacity": 150000,
        "city": "Los Angeles",
    },

]

recommendations = recommend_donors(
    campaign,
    donors,
)

print()

for recommendation in recommendations.recommendations:

    print("--------------------------------")

    print(
        recommendation.donor_id
    )

    print(
        recommendation.confidence
    )

    print(
        recommendation.reasoning
    )

print()
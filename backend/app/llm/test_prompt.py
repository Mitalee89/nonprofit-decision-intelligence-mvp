from app.llm.client import generate
from app.llm.prompts import donor_recommendation_prompt
from app.llm.parser import parse_json

campaign = {
    "name": "Education For All",
    "description": "Provide digital education for underprivileged children.",
    "goal_amount": 500000,
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
]

prompt = donor_recommendation_prompt(
    campaign,
    donors,
)

print(prompt)

response = generate(prompt)

print(response)

parsed = parse_json(response)

print(parsed)
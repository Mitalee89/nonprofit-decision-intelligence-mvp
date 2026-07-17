import json


def donor_recommendation_prompt(campaign: dict, donors: list[dict]) -> str:
    """
    Builds the prompt for donor recommendations.
    """

    campaign_json = json.dumps(campaign, indent=2)

    donors_json = json.dumps(donors, indent=2)

    return f"""
You are an AI fundraising advisor for a non-profit organization.

Your task is to recommend the BEST donors for the campaign.

Evaluate every donor using:

1. Preferred Cause
2. Interests
3. Donation Capacity
4. City (minor factor)
5. Overall campaign alignment

Campaign

{campaign_json}

Available Donors

{donors_json}

Rules

- Evaluate every donor.
- Return every donor exactly once.
- Sort by confidence descending.
- Confidence must be between 0 and 100.
- Matching preferred cause is the strongest factor.
- Matching interests are the second strongest factor.
- Donation capacity is the third strongest factor.
- City is a minor factor.
- Never invent donors.
- Never omit donors.
- Use only donor IDs from the provided list.
- Keep reasoning under 30 words.

Return ONLY valid JSON.

Expected Output

{{
    "recommendations": [
        {{
            "donor_id": 1,
            "confidence": 95,
            "reasoning": "Excellent alignment with education and high giving capacity."
        }}
    ]
}}

Do not include markdown.

Do not explain.

Return only JSON.
"""


def grant_recommendation_prompt(
    campaign: dict,
    grants: list[dict],
) -> str:
    """
    Builds the prompt for grant recommendations.
    """

    campaign_json = json.dumps(campaign, indent=2)

    grants_json = json.dumps(grants, indent=2)

    return f"""
You are an AI grant advisor for a non-profit organization.

Your task is to recommend the BEST grants for the campaign.

Evaluate every grant using:

1. Eligibility requirements
2. Campaign cause/category alignment
3. Grant amount
4. Grant status (prefer OPEN grants)
5. Overall campaign fit

Campaign

{campaign_json}

Available Grants

{grants_json}

Rules

- Evaluate every grant.
- Return every grant exactly once.
- Sort by confidence descending.
- Confidence must be between 0 and 100.
- Eligibility matching is the strongest factor.
- Campaign cause alignment is the second strongest factor.
- Grant amount is the third strongest factor.
- Prefer grants that are OPEN.
- Never invent grants.
- Never omit grants.
- Use only grant IDs from the provided list.
- Keep reasoning under 30 words.

Return ONLY valid JSON.

Expected Output

{{
    "recommendations": [
        {{
            "grant_id": 1,
            "confidence": 95,
            "reasoning": "Excellent eligibility match with sufficient funding."
        }}
    ]
}}

Do not include markdown.

Do not explain.

Return only JSON.
"""
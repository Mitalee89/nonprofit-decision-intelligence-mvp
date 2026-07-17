from app.models.campaign import Campaign
from app.models.donor import Donor
from app.models.grant import Grant


def campaign_to_llm(campaign: Campaign) -> dict:
    """
    Converts a Campaign entity into an LLM-friendly dictionary.
    """

    return {
        "id": campaign.id,
        "name": campaign.name,
        "description": campaign.description,
        "goal_amount": float(campaign.goal_amount),
        "amount_raised": float(campaign.amount_raised),
        "status": campaign.status.value,
    }


def donor_to_llm(donor: Donor) -> dict:
    """
    Converts a Donor entity into an LLM-friendly dictionary.
    """

    return {
        "id": donor.id,
        "name": donor.name,
        "preferred_cause": donor.preferred_cause,
        "interests": donor.interests,
        "capacity": float(donor.capacity),
        "city": donor.city,
    }


def grant_to_llm(grant: Grant) -> dict:
    """
    Converts a Grant entity into an LLM-friendly dictionary.
    """

    return {
        "id": grant.id,
        "title": grant.title,
        "organization": grant.organization,
        "amount": float(grant.amount),
        "eligibility": grant.eligibility,
        "status": grant.status.value,
    }


def donors_to_llm(donors: list[Donor]) -> list[dict]:
    """
    Converts a list of Donor entities.
    """

    return [
        donor_to_llm(donor)
        for donor in donors
    ]


def grants_to_llm(grants: list[Grant]) -> list[dict]:
    """
    Converts a list of Grant entities.
    """

    return [
        grant_to_llm(grant)
        for grant in grants
    ]
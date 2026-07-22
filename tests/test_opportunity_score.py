from scripts.calculate_opportunity_score import calculate


def test_calculate_opportunity_score() -> None:
    opportunity = {
        "business_value_score": 5,
        "workflow_suitability_score": 4,
        "technical_feasibility_score": 4,
        "deployment_readiness_score": 3,
        "time_to_value_score": 4,
        "risk_score": 2,
    }
    assert calculate(opportunity) == 3.9

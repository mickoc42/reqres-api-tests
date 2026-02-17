import pytest

from utils.test_data import USER_ID_SCENARIOS


class TestParametrize:
    @pytest.mark.parametrize(
        "user_id, expected_status, scenario_id",
        USER_ID_SCENARIOS,
        ids=[s[2] for s in USER_ID_SCENARIOS],
    )
    def test_get_user_by_id(self, api_client, user_id, expected_status, scenario_id):
        response = api_client.get(f"/users/{user_id}")
        assert response.status_code == expected_status, (
            f"expected {expected_status}, received {response.status_code}"
        )

import pytest

from utils.test_data import (
    LOGIN_NEGATIVE_CASES,
    REGISTER_NEGATIVE_CASES,
    VALID_LOGIN,
    VALID_REGISTER_DATA,
)


class TestUserRegistration:
    @pytest.mark.authentication
    def test_register_user_with_valid_data(self, api_client):
        response = api_client.post("/register", data=VALID_REGISTER_DATA)

        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        body = response.json()
        assert "token" in body
        assert isinstance(body["token"], str)
        assert len(body["token"]) > 0

    @pytest.mark.negative
    @pytest.mark.parametrize("payload, expected_error", REGISTER_NEGATIVE_CASES)
    def test_register_negative(self, api_client, payload, expected_error):
        response = api_client.post("/register", data=payload)
        assert response.status_code == 400
        assert response.json()["error"] == expected_error


class TestLogin:
    @pytest.mark.authentication
    def test_login_user_with_valid_data(self, api_client):
        response = api_client.post("/login", data=VALID_LOGIN)

        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        body = response.json()
        assert "token" in body
        assert isinstance(body["token"], str)
        assert len(body["token"]) > 0

    @pytest.mark.negative
    @pytest.mark.parametrize("payload, expected_error", LOGIN_NEGATIVE_CASES)
    def test_login_negative(self, api_client, payload, expected_error):
        response = api_client.post("/login", data=payload)
        assert response.status_code == 400
        assert response.json()["error"] == expected_error

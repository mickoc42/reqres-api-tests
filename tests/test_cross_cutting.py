class TestCrossCutting:
    def test_content_type_is_valid(self, api_client):
        response = api_client.get("/users")
        assert "application/json" in response.headers.get("Content-Type")

    def test_response_time_below_threshold(self, api_client):
        response = api_client.get("/users/2")
        assert response.elapsed.total_seconds() < 2

    def test_response_time_list__below_threshold(self, api_client):
        response = api_client.get("/users")
        assert response.elapsed.total_seconds() < 2

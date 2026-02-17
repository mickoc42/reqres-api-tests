import pytest
from email_validator import EmailNotValidError, validate_email
from jsonschema import Draft7Validator

from utils.schemas import (
    CREATED_USER_SCHEMA,
    SINGLE_USER_SCHEMA,
    UPDATED_USER_SCHEMA,
    USERS_LIST_SCHEMA,
)
from utils.test_data import (
    DEFAULT_PER_PAGE,
    EMPTY_PAGE,
    EXISTING_USER_ID,
    NON_EXISTING_USER_ID,
    PARTIAL_UPDATE_USER,
    SECOND_PAGE,
    UPDATED_USER,
    USER_EMPTY_BODY,
    USER_ONLY_NAME,
    VALID_USER,
)

# ============================================================
# GET /api/users
# ============================================================


class TestGetUsersList:
    @pytest.mark.smoke
    @pytest.mark.crud
    def test_get_users_list_default_page(self, api_client):

        # ACT
        response = api_client.get("/users")

        # ASSERT
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

        body = response.json()

        assert "page" in body, "'page' not present in body"
        assert "per_page" in body, "per_page' not present in body"
        assert "total" in body, "'total' not present in body"
        assert "data" in body, " 'data' not present in body"

        assert body["page"] == 1, f"Expected page 1, got {body['page']}"

        assert isinstance(body["data"], list), "Expected data to be a tyep List"
        assert len(body["data"]) > 0, "Expected users lists to not be empty"

    @pytest.mark.crud
    def test_get_users_list_second_page(self, api_client):

        response = api_client.get("/users", params={"page": SECOND_PAGE})

        assert response.status_code == 200

        body = response.json()
        assert body["page"] == SECOND_PAGE, (
            f"Expected page {SECOND_PAGE}, got {body['page']}"
        )
        assert isinstance(body["data"], list)

    @pytest.mark.schema
    @pytest.mark.crud
    def test_get_users_list_schema_validation(self, api_client):

        response = api_client.get("/users")
        body = response.json()

        errors = list(Draft7Validator(USERS_LIST_SCHEMA).iter_errors(body))
        assert len(errors) == 0, f"Schema errors: {[e.message for e in errors]}"

    @pytest.mark.crud
    def test_get_users_list_per_page_default(self, api_client):

        response = api_client.get("/users")
        body = response.json()

        assert body["per_page"] == DEFAULT_PER_PAGE, (
            f"Expected per_page={DEFAULT_PER_PAGE}, got {body['per_page']}"
        )
        assert len(body["data"]) == DEFAULT_PER_PAGE, (
            f"Expected {DEFAULT_PER_PAGE} users, got {len(body['data'])}"
        )

    @pytest.mark.crud
    @pytest.mark.negative
    def test_get_users_list_empty_page(self, api_client):

        response = api_client.get("/users", params={"page": EMPTY_PAGE})

        assert response.status_code == 200
        body = response.json()
        assert body["data"] == [], f"Expected empty list, got {body['data']}"

    @pytest.mark.crud
    def test_get_users_list_data_types_validation(self, api_client):

        response = api_client.get("/users")
        body = response.json()

        for user in body["data"]:
            assert isinstance(user["id"], int), (
                f"User id should be int, got {type(user['id'])}"
            )

            try:
                validate_email(user["email"])
            except EmailNotValidError as e:
                pytest.fail(f"Invalid email format: {user['email']} — {e}")

            assert user["avatar"].startswith("http"), (
                f"Avatar should be URL, got: {user['avatar']}"
            )


# ============================================================
# GET /api/users/{id}
# ============================================================


class TestGetSingleUser:
    @pytest.mark.smoke
    @pytest.mark.crud
    def test_get_single_user_existing(self, api_client):

        response = api_client.get(f"/users/{EXISTING_USER_ID}")

        assert response.status_code == 200

        body = response.json()
        assert "data" in body, "'data' not present in body"
        assert body["data"]["id"] == EXISTING_USER_ID, (
            f"Expected user id={EXISTING_USER_ID}, got {body['data']['id']}"
        )

    @pytest.mark.smoke
    @pytest.mark.crud
    @pytest.mark.negative
    def test_get_single_user_not_found(self, api_client):

        response = api_client.get(f"/users/{NON_EXISTING_USER_ID}")

        assert response.status_code == 404, (
            f"Expected 404 for non-existing user, got {response.status_code}"
        )

        body = response.json()
        assert body == {}, f"Expected empty body {{}}, got {body}"

    @pytest.mark.schema
    @pytest.mark.crud
    def test_get_single_user_schema_validation(self, api_client):

        response = api_client.get(f"/users/{EXISTING_USER_ID}")
        body = response.json()

        errors = list(Draft7Validator(SINGLE_USER_SCHEMA).iter_errors(body))
        assert len(errors) == 0, f"Schema errors: {[e.message for e in errors]}"


# ============================================================
# POST /api/users
# ============================================================


class TestCreateUser:
    @pytest.mark.smoke
    @pytest.mark.crud
    def test_post_create_user_valid_data(self, api_client):

        response = api_client.post("/users", data=VALID_USER)

        assert response.status_code == 201, f"Expected 201, got {response.status_code}"

        body = response.json()

        assert body["name"] == VALID_USER["name"], (
            f"Expected name '{VALID_USER['name']}', got '{body['name']}'"
        )
        assert body["job"] == VALID_USER["job"], (
            f"Expected job '{VALID_USER['job']}', got '{body['job']}'"
        )

        assert "id" in body, "'id' not present in body"
        assert "createdAt" in body, "'createdAt' not present in body "

    @pytest.mark.crud
    @pytest.mark.negative
    def test_post_create_user_only_name(self, api_client):

        response = api_client.post("/users", data=USER_ONLY_NAME)

        assert response.status_code == 201

        body = response.json()
        assert body["name"] == USER_ONLY_NAME["name"]
        assert "id" in body
        assert "createdAt" in body

    @pytest.mark.crud
    @pytest.mark.negative
    def test_post_create_user_empty_body(self, api_client):

        response = api_client.post("/users", data=USER_EMPTY_BODY)

        assert response.status_code == 201

        body = response.json()
        assert "id" in body, "'id' not present in body"
        assert "createdAt" in body, "'createdAt' not present in body"

    @pytest.mark.crud
    @pytest.mark.schema
    def test_post_create_user_schema_validation(self, api_client):

        response = api_client.post("/users", data=VALID_USER)
        body = response.json()

        errors = list(Draft7Validator(CREATED_USER_SCHEMA).iter_errors(body))
        assert len(errors) == 0, f"Schema errors: {[e.message for e in errors]}"

        assert "T" in body["createdAt"], (
            f"createdAt not in  ISO 8601 standard: {body['createdAt']}"
        )


# ============================================================
# PUT /api/users/{id}
# ============================================================


class TestUpdateUser:
    @pytest.mark.smoke
    @pytest.mark.crud
    def test_put_update_user_full_data(self, api_client):

        response = api_client.put(f"/users/{EXISTING_USER_ID}", data=UPDATED_USER)

        assert response.status_code == 200

        body = response.json()
        assert body["name"] == UPDATED_USER["name"]
        assert body["job"] == UPDATED_USER["job"]
        assert "updatedAt" in body

    @pytest.mark.crud
    @pytest.mark.schema
    def test_put_update_user_schema_and_timestamp(self, api_client):

        response = api_client.put(f"/users/{EXISTING_USER_ID}", data=UPDATED_USER)
        body = response.json()

        errors = list(Draft7Validator(UPDATED_USER_SCHEMA).iter_errors(body))
        assert len(errors) == 0, f"Schema errors: {[e.message for e in errors]}"

        assert "T" in body["updatedAt"], (
            f"updatedAt not in  ISO 8601 standard: {body['updatedAt']}"
        )


# ============================================================
# PATCH /api/users/{id}
# ============================================================


class TestPatchUser:
    @pytest.mark.smoke
    @pytest.mark.crud
    def test_patch_update_single_field(self, api_client):

        response = api_client.patch(
            f"/users/{EXISTING_USER_ID}", data=PARTIAL_UPDATE_USER
        )

        assert response.status_code == 200

        body = response.json()
        assert body["job"] == PARTIAL_UPDATE_USER["job"], (
            f"Expected job '{PARTIAL_UPDATE_USER['job']}', got '{body['job']}'"
        )
        assert "updatedAt" in body


# ============================================================
# DELETE /api/users/{id}
# ============================================================


class TestDeleteUser:
    @pytest.mark.smoke
    @pytest.mark.crud
    def test_delete_user_existing(self, api_client):

        response = api_client.delete(f"/users/{EXISTING_USER_ID}")

        assert response.status_code == 204, (
            f"Expected 204 No Content, got {response.status_code}"
        )

        assert response.text == "", (
            f"Expected empty body for 204, got: '{response.text}'"
        )

    @pytest.mark.crud
    @pytest.mark.negative
    def test_delete_user_non_existing(self, api_client):

        response = api_client.delete(f"/users/{NON_EXISTING_USER_ID}")

        assert response.status_code == 204

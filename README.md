# 🧪 Reqres API Tests — Python + pytest

Automated API test suite for [reqres.in](https://reqres.in/) — a fake REST API for testing and prototyping.


## 🏗️ Project Structure

```
reqres-api-tests/
├── tests/
│   ├── test_users_crud.py        # CRUD operations on /users
│   ├── test_authentication.py    # Login & Register 
│   └── test_cross_cutting.py     # Headers, timeouts 
├── utils/
│   ├── api_client.py             # HTTP client wrapper
│   ├── schemas.py                # JSON Schemas for validation
│   └── test_data.py              # Centralized test data
├── conftest.py                   # Global pytest fixtures
├── pytest.ini                    # pytest configuration
├── requirements.txt              # Dependencies
└── README.md
```

## 🚀 Quick Start

```bash
# 1. Clone & enter directory
cd reqres-api-tests

# 2. Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run all tests
pytest

# 5. Run with detailed output
pytest -v -s
```

## 🎯 Running Specific Tests

```bash
# Run only smoke tests (critical path)
pytest -m smoke

# Run only CRUD tests
pytest -m crud

# Run only negative tests
pytest -m negative

# Run only schema validation tests
pytest -m schema

# Run specific test file
pytest tests/test_users_crud.py

# Run specific test class
pytest tests/test_users_crud.py::TestGetUsersList

# Run specific test
pytest tests/test_users_crud.py::TestGetUsersList::test_get_users_list_default_page
```

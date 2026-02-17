



VALID_LOGIN = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"    
}

LOGIN_NO_PASSWORD = {"email": "eve.holt@reqres.in"}
LOGIN_NO_EMAIL = {"password": "cityslicka"}
LOGIN_INVALID_EMAIL = {"email": "test@example.com", "password": "cityslicka"}


REGISTER_NO_PASSWORD = {
  "email": "test@example.com",
}


REGISTER_NO_EMAIL = {
  "password": "test1234"
}



REGISTER_INVALID_EMAIL = {
  "email": "testexample.com",
  "password": "test1234"
}

VALID_REGISTER_DATA = {
  "email": "eve.holt@reqres.in",
  "password": "pistol"
}


VALID_USER = {
    "name": "Jan Kowalski",
    "job": "QA Engineer"
}


UPDATED_USER = {
    "name": "Jan Kowalski",
    "job": "Senior QA Engineer" 
}


PARTIAL_UPDATE_USER = {
    "job": "QA Automation Engineer"
}


USER_ONLY_NAME = {"name": "Anna Nowak"}      
USER_ONLY_JOB = {"job": "Developer"}           
USER_EMPTY_BODY = {}                           


EXISTING_USER_ID = 2       
NON_EXISTING_USER_ID = 999  

DEFAULT_PAGE = 1
DEFAULT_PER_PAGE = 6  
SECOND_PAGE = 2
EMPTY_PAGE = 999      


LOGIN_NEGATIVE_CASES = [
    (LOGIN_NO_PASSWORD, "Missing password"),
    (LOGIN_INVALID_EMAIL, "user not found"),
    (LOGIN_NO_EMAIL, "Missing email or username"),
    (None, "Empty request body"),
]


REGISTER_NEGATIVE_CASES = [
    (REGISTER_NO_PASSWORD, "Missing password"),
    (REGISTER_INVALID_EMAIL, "Note: Only defined users succeed registration"),
    (REGISTER_NO_EMAIL, "Missing email or username"),
    (None, "Empty request body"),
]

USER_ID_SCENARIOS = [
    (1, 200, "existing_user_1"),
    (2, 200, "existing_user_2"),
    (12, 200, "last_existing_user"),
    (999, 404, "non_existing_user"),
    (0, 404, "zero_id"),
]
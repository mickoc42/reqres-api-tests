USER_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "email": {"type": "string", "format": "email"},
        "first_name": {"type": "string", "minLength": 1},
        "last_name": {"type": "string", "minLength": 1},
        "avatar": {"type": "string", "format": "uri"},
    },
    "required": ["id", "email", "first_name", "last_name", "avatar"],
    "additionalProperties": False,
}


USERS_LIST_SCHEMA = {
    "type": "object",
    "properties": {
        "page": {"type": "integer", "minimum": 1},
        "per_page": {"type": "integer", "minimum": 1},
        "total": {"type": "integer", "minimum": 0},
        "total_pages": {"type": "integer", "minimum": 0},
        "data": {"type": "array", "items": USER_SCHEMA},
        "support": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "format": "uri"},
                "text": {"type": "string"},
            },
            "required": ["url", "text"],
        },
    },
    "required": ["page", "per_page", "total", "total_pages", "data", "support"],
}


SINGLE_USER_SCHEMA = {
    "type": "object",
    "properties": {
        "data": USER_SCHEMA,
        "support": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "format": "uri"},
                "text": {"type": "string"},
            },
            "required": ["url", "text"],
        },
    },
    "required": ["data", "support"],
}


CREATED_USER_SCHEMA = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "id": {"type": "string"},
        "createdAt": {"type": "string"},
    },
    "required": ["id", "createdAt"],
}


UPDATED_USER_SCHEMA = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "updatedAt": {"type": "string"},
    },
    "required": ["updatedAt"],
}

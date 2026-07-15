import uuid


def generate_user_data():
    unique_id = uuid.uuid4().hex[:8]
    return {
        "first_name": "Test",
        "last_name": "User",
        "username": f"testuser_{unique_id}",
        "email": f"testuser_{unique_id}@yandex.ru",
        "password": "TestPass123!",
    }

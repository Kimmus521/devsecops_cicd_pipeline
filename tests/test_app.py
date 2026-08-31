from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.data == b"DevSecOps CI/CD Pipeline"


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_message():
    client = app.test_client()

    response = client.get("/api/message")

    assert response.status_code == 200
    assert response.json["version"] == "1.0"

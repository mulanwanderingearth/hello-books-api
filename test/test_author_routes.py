# def test-import pytest
from app.models.book import Book
from app.routes.route_utilities import validate_models
from werkzeug.exceptions import HTTPException

def test_get_all_authors_with_no_records(client):
    # Act
    response = client.get("/authors")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []
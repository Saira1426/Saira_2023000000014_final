import pytest
import requests

# Base URL (Mock API Endpoint)
BASE_URL = "https://jsonplaceholder.typicode.com/posts"


# 1. GET Request: Fetching Data
def test_get_endpoint():
    response = requests.get(f"{BASE_URL}/1")
    
    # Assertions
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    json_data = response.json()
    assert json_data["id"] == 1
    assert "title" in json_data


# 2. POST Request: Creating New Resource
def test_post_endpoint():
    payload = {
        "title": "CSE 474 Automation",
        "body": "API integration via Python requests",
        "userId": 101
    }
    headers = {"Content-Type": "application/json; charset=UTF-8"}
    
    response = requests.post(BASE_URL, json=payload, headers=headers)
    
    # Assertions
    assert response.status_code == 201
    json_data = response.json()
    assert json_data["title"] == "CSE 474 Automation"
    assert json_data["userId"] == 101


# 3. PUT Request: Full Update of Resource
def test_put_endpoint():
    payload = {
        "id": 1,
        "title": "Completely Replaced Title",
        "body": "Replaced Content Body",
        "userId": 1
    }
    
    response = requests.put(f"{BASE_URL}/1", json=payload)
    
    # Assertions
    assert response.status_code == 200
    assert response.json()["title"] == "Completely Replaced Title"


# 4. PATCH Request: Partial Update of Resource
def test_patch_endpoint():
    payload = {
        "title": "Only Title Updated"
    }
    
    response = requests.patch(f"{BASE_URL}/1", json=payload)
    
    # Assertions
    assert response.status_code == 200
    assert response.json()["title"] == "Only Title Updated"


# 5. DELETE Request: Removing Resource
def test_delete_endpoint():
    response = requests.delete(f"{BASE_URL}/1")
    
    # Assertions
    assert response.status_code == 200
    
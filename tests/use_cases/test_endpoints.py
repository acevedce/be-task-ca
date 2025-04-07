from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_customer_endpoint():
    response = client.post("/customers", json={
        "name": "John Doe",
        "email": "john@example.com"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "John Doe"
    assert data["email"] == "john@example.com"

    # Duplicate email should fail
    response = client.post("/customers", json={
        "name": "John Doe",
        "email": "john@example.com"
    })
    assert response.status_code == 409

def test_add_to_cart_endpoint():
    # Create a new customer first
    client.post("/customers", json={
        "name": "Cart Tester",
        "email": "cart@example.com"
    })

    # Add item to cart
    response = client.post("/customers/1/cart", json={
        "item_id": 1,
        "quantity": 2
    })
    assert response.status_code == 200
    data = response.json()
    assert data["customer_id"] == 1
    assert len(data["items"]) == 1
    assert data["items"][0]["item_id"] == 1
    assert data["items"][0]["quantity"] == 2

def test_items_endpoints():
    # Add new item
    response = client.post("/items", json={
        "name": "Banana",
        "description": "Fresh bananas",
        "price": 1.5,
        "quantity": 100
    })
    assert response.status_code == 200
    item = response.json()
    assert item["name"] == "Banana"
    assert item["price"] == 1.5
    assert item["quantity"] == 100

    # Get all items
    response = client.get("/items")
    assert response.status_code == 200
    items = response.json()
    assert isinstance(items, list)
    assert any(i["name"] == "Banana" for i in items)

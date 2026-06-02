# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a RESTful API using the FastAPI framework to manage a simple resource collection (Items). Learn routing, Pydantic models, request validation, and automatic API documentation.

## 📝 Tasks

### 🛠️ Create a CRUD API

#### Description
Implement a command-line runnable FastAPI application that provides Create, Read, Update, and Delete (CRUD) operations for an `Item` resource. Use an in-memory store (Python dict) for persistence during development.

#### Requirements
Completed program should:

- Expose endpoints: `GET /items`, `GET /items/{item_id}`, `POST /items`, `PUT /items/{item_id}`, `DELETE /items/{item_id}`.
- Use a Pydantic model for request validation and response serialization.
- Return appropriate HTTP status codes (e.g., `201` for created, `404` for not found).
- Validate input (e.g., name length, price >= 0) and return clear error messages.

### 🛠️ Add documentation and run the server

#### Description
Run the app locally with `uvicorn` and use FastAPI's interactive docs to explore and test the API.

#### Requirements

- Start the server using `uvicorn starter_app:app --reload` and verify the interactive docs are available at `/docs`.
- Demonstrate the API with example `curl` commands or HTTP client screenshots.

#### Example usage
```
# List items
curl -s http://127.0.0.1:8000/items

# Create an item
curl -X POST http://127.0.0.1:8000/items -H "Content-Type: application/json" \
  -d '{"name":"T-shirt","description":"Cotton","price":19.99}'

# Get an item
curl http://127.0.0.1:8000/items/1
```

**Skills practiced:** REST API design, FastAPI basics, Pydantic validation, routing, and local development with `uvicorn`.

**Starter files:** `starter_app.py`, `requirements.txt`

# API Reference

**Summary:** This document provides a comprehensive reference for our REST API. All endpoints are versioned and follow standard RESTful conventions.

**Base URL:** `https://api.yourproject.com/v1`

## Authentication

All API requests must be authenticated using a Bearer token in the `Authorization` header.

`Authorization: Bearer <YOUR_JWT_TOKEN>`

Tokens can be obtained via the `/auth/token` endpoint.

## Endpoints

### 1. Users

#### `GET /users/{id}`
Retrieves a specific user by their unique ID.

- **Parameters:**
  - `id` (string, path, required): The UUID of the user.

- **Responses:**
  - `200 OK`: Successful response.
    ```json
    {
      "id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
      "email": "user@example.com",
      "role": "admin",
      "created_at": "2023-10-27T10:00:00Z"
    }
    ```
  - `404 Not Found`: If the user with the specified ID does not exist.
    ```json
    {
      "detail": "User not found"
    }
    ```

#### `POST /users`
Creates a new user.

- **Request Body:**
  ```json
  {
    "email": "newuser@example.com",
    "password": "a-very-strong-password"
  }
  ```

- **Responses:**
  - `201 Created`: User created successfully.
    ```json
    {
      "id": "d4c3b2a1-f6e5-0987-4321-fedcba098765",
      "email": "newuser@example.com",
      "role": "user"
    }
    ```
  - `422 Unprocessable Entity`: If the request body is invalid (e.g., invalid email).

### 2. Projects

#### `GET /projects`
Retrieves a list of projects for the authenticated user.

- **Responses:**
  - `200 OK`: A list of projects.
    ```json
    [
      {
        "id": "p1a2b3c4-e5f6-7890-1234-567890abcdef",
        "name": "My First Project",
        "created_at": "2023-10-27T11:00:00Z"
      }
    ]
    ```

---
*For a guided tour of the implementation, see the [Code Walkthroughs](./code-walkthroughs/README.md).*

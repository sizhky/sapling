# Code Walkthroughs

**Summary:** This document provides guided tours of the key parts of our codebase. The goal is to help new developers understand the structure, logic, and patterns used in this project.

## 1. Project Structure Overview

Our project follows a standard structure to ensure consistency and ease of navigation.

```
/src
|-- /api
|   |-- /v1
|   |   |-- endpoints.py  # API route definitions
|   |   `-- schemas.py    # Pydantic models for request/response
|-- /core
|   |-- config.py       # Configuration management
|   `-- security.py     # Auth and security helpers
|-- /db
|   |-- models.py       # SQLAlchemy ORM models
|   `-- session.py      # Database session management
|-- /services
|   `-- data_service.py # Business logic
`-- main.py             # Application entry point
```

## 2. Walkthrough: Adding a New API Endpoint

This walkthrough explains how to add a new endpoint to retrieve a user by their ID.

### Step 1: Define the Schema
First, define the response model in `src/api/v1/schemas.py`. This ensures our API responses are consistent and well-documented.

```python
# src/api/v1/schemas.py

// ...existing code...
class UserBase(BaseModel):
    email: EmailStr

class UserRead(UserBase):
    id: UUID
    role: str

    class Config:
        orm_mode = True
// ...existing code...
```

### Step 2: Add the Business Logic
Next, add the logic to fetch the user from the database in `src/services/data_service.py`.

```python
# src/services/data_service.py

// ...existing code...
from .db import models

def get_user_by_id(db: Session, user_id: UUID) -> models.User | None:
    """Fetches a user by their unique ID."""
    return db.query(models.User).filter(models.User.id == user_id).first()
// ...existing code...
```

### Step 3: Create the Endpoint
Finally, create the endpoint in `src/api/v1/endpoints.py`. This connects the HTTP route to our business logic.

```python
# src/api/v1/endpoints.py

// ...existing code...
from . import schemas
from .services import data_service

@router.get("/users/{user_id}", response_model=schemas.UserRead)
def read_user(user_id: UUID, db: Session = Depends(get_db)):
    db_user = data_service.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
// ...existing code...
```

This structured approach ensures separation of concerns and makes the codebase easier to maintain and test.

---
*For more details on our API, see the [API Reference](../api-reference/README.md).*
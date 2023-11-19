"""
Example FastAPI module for user management.

This module defines a FastAPI application and includes a sample database of users.
"""
from typing import List
from uuid import UUID, uuid4

from models import Gender, Role, User, UpdateUser

from fastapi import FastAPI
from fastapi import HTTPException


app = FastAPI()

db: List[User] = [
    User(
    id=uuid4(),
    first_name="John",
    last_name="Doe",
    gender=Gender.MALE,
    roles=[Role.USER],
    ),

    User(
    id=uuid4(),
    first_name="Jane",
    last_name="Doe",
    gender=Gender.FEMALE,
    roles=[Role.USER],
    ),

    User(
    id=uuid4(),
    first_name="James",
    last_name="Gabriel",
    gender=Gender.MALE,
    roles=[Role.USER],
    ),

    User(
    id=uuid4(),
    first_name="Eunit",
    last_name="Eunit",
    gender=Gender.MALE,
    roles=[Role.ADMIN, Role.USER],
    ),
]

@app.get("/api/v1/users")
async def get_users():
    """
    Retrieve a list of users.

    Returns:
    - List[dict]: A list of dictionaries representing user data.

    This endpoint retrieves and returns a list of users from the database.
    """
    return db


@app.post("/api/v1/users")
async def create_user(user: User):
    """
    Create a new user.

    Parameters:
    - user (User): The user data to be created.

    Returns:
    - dict: A dictionary containing the ID of the newly created user.

    This endpoint receives user data as input, adds the user to the database, and returns
    a dictionary containing the ID of the newly created user.
    """
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{id}")
async def delete_user(uid: UUID):
    """
    Delete a user by ID.
    Parameters:
    - id (UUID): The unique identifier of the user to be deleted.
    Raises:
    - HTTPException: If the user with the specified ID is not found, a 404 error is raised.
    This endpoint deletes a user from the database based on the provided user ID.
    If the user is not found, a 404 error is raised. No content is returned 
    upon successful deletion.
    """
    # Iterate through a copy of the list to avoid modification during iteration
    for user in db.copy():
        if user.id == uid:
            db.remove(user)
            return

    raise HTTPException(
        status_code=404, detail=f"Delete user failed, id {id} not found."
    )

@app.put("/api/v1/users/{id}")
async def update_user(user_update: UpdateUser, uid: UUID):
    """
    Update user information by ID.

    Parameters:
    - user_update (UpdateUser): The data to update the user, as provided in the request body.
    - id (UUID): The unique identifier of the user to be updated.

    Returns:
    - UUID: The ID of the updated user.

    Raises:
    - HTTPException: If the user with the specified ID is not found, a 404 error is raised.
    """
    # Iterate through the database to find the user by ID
    for user in db:
        if user.id == uid:
            # Update user information based on the provided UpdateUser data
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.roles is not None:
                user.roles = user_update.roles

            # Return the ID of the updated user
            return user.id

    # If no user is found with the specified ID, raise a 404 error
    raise HTTPException(status_code=404, detail=f"Could not find user with id: {id}")

from fastapi import APIRouter, Path, Query, status, HTTPException

from user.request import UserCreateRequest, UserUpdateRequest
from user.response import UserResponse

router = APIRouter(tags=["User"])

users = [
    {"id": 1, "name": "alex", "job": "student"},
    {"id": 2, "name": "bob", "job": "sw engineer"},
    {"id": 3, "name": "chris", "job": "barista"},
]

@router.get("/users", status_code=status.HTTP_200_OK)
def get_users_handler():
    return users

@router.get("/users/search")
def search_user_handler(
    name: str | None = Query(None),
    job: str | None = Query(None),
):
    if name is None and job is None:
        return {"msg": "조회에 사용할 QueryParam이 필요합니다."}

    results = users

    if name is not None:
        results = [user for user in results if name.lower() in user["name"].lower()]

    if job is not None:
        results = [user for user in results if job.lower() in user["job"].lower()]

    return results

@router.get("/users/{user_id}")
def get_user_handler(user_id: int = Path(..., ge=1)):
    for user in users:
        if user["id"] == user_id:
            return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User Not Found",
    )

@router.post(
    "/users",
    status_code=status.HTTP_201_CREATED,
    response_model=UserResponse,
)
def create_user_handler(body: UserCreateRequest):
    new_user = {
        "id": len(users) + 1,
        "name": body.name,
        "job": body.job,
    }
    users.append(new_user)
    return new_user

@router.patch(
    "/users/{user_id}",
    response_model=UserResponse,
)
def update_user_handler(
    user_id: int = Path(..., ge=1),
    body: UserUpdateRequest = ...,
):
    for user in users:
        if user["id"] == user_id:
            user["job"] = body.job
            return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User Not Found",
    )

@router.delete(
    "/users/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_user_handler(user_id: int = Path(..., ge=1)):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User Not Found",
    )
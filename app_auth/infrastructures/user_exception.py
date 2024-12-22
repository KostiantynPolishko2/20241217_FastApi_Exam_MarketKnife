from fastapi import HTTPException, status

new_user_exc400 = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="User with this email already exist"
)

user_exc404 = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="User with this nane did not found"
)

new_user_exc406 = HTTPException(
    status_code=status.HTTP_406_NOT_ACCEPTABLE,
    detail="failed to add new username to db"
)
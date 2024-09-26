import logging
from fastapi import APIRouter, Path, Depends, FastAPI, HTTPException, status
from env_config import *
# from LoginAPI.model.user import User
import base64
import secrets
from typing import Annotated
from fastapi.security import HTTPBasic, HTTPBasicCredentials

router = APIRouter(prefix="/auth", tags=["Auth API"])

security = HTTPBasic()

def get_current_username(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
):
    current_username_bytes = credentials.username.encode("utf8")
    correct_username_bytes = b"localuser"
    is_correct_username = secrets.compare_digest(
        current_username_bytes, correct_username_bytes
    )
    current_password_bytes = credentials.password.encode("utf8")
    correct_password_bytes = b"localpasswd"
    is_correct_password = secrets.compare_digest(
        current_password_bytes, correct_password_bytes
    )
    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@router.post("/login", description="Login Auth")
async def login(username: Annotated[str, Depends(get_current_username)]):
    # print(token)
    username = 'localuser'
    passward = 'localpasswd'

    bytes = (username + ':' + passward).encode('UTF-8')

    accessToken = base64.b64encode(bytes)
    result_str = accessToken.decode('ascii')
    print(result_str)
    print(accessToken)
    return { "accessToken": accessToken, "refreshToken": "refreshToken" }
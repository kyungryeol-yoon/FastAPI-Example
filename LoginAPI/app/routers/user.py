import logging
from fastapi import APIRouter, Path, Depends, FastAPI, HTTPException, status
from env_config import *
# from LoginAPI.model.user import User

from typing import Annotated
from fastapi.security import OAuth2PasswordBearer

router = APIRouter(prefix="/user", tags=["User API"])



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.get("/current", description="Current User")
async def current_user(token: str = Depends(oauth2_scheme)):
    return {"userId": "내_아이디_뭐게_맞춰보게나", "name": "내_이름_뭐게_맞춰보게나", "profile": "profileTest" }

import logging
from fastapi import APIRouter
from env_config import *
from model.board import Board

router = APIRouter(prefix="/board", tags=["Board API"])

board_list = []

@router.get("", description="Read Board")
async def read_board():
    return board_list

@router.get("/{board_id}")
async def read_board_item(board_id: int):
    for board_item in board_list:
        if board_item.no == board_id:
            return board_item
    return {
        "message": "Todo with supplied ID dosen't exist."
    }

@router.post("")
def insert_board(board_item: Board) -> dict:
    board_list.append(board_item)
    return {"message": "Added successfully"}

@router.put("")
def update_board():
    return {"Hello": "World"}

@router.delete("")
def delete_board():
    return {"Hello": "World"}

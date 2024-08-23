import logging
from fastapi import APIRouter, Path
from env_config import *
from model.board import Board

router = APIRouter(prefix="/board", tags=["Board API"])

board_list = []

@router.get("", description="Read Board")
async def read_all_board():
    return board_list

@router.get("/{board_id}")
async def read_board_item(board_id: int):
    for board_item in board_list:
        if board_item.no == board_id:
            return board_item
    return { "message": "ID dosen't exist." }

@router.post("")
async def insert_board(board_item: Board) -> dict:
    board_list.append(board_item)
    return {"message": "Added successfully"}

@router.put("/{board_id}")
async def update_board(board_item: Board, board_id: int = Path(..., title="The Id of the board to be updated")) -> dict:
    for board in board_list:
        if board.no == board_id:
            board.title = board_item.title
            board.content = board_item.content
            return { "message": "Updated successfully" }
    return { "message": "ID doesn't exist." }

@router.delete("/{board_id}")
async def delete_board_item(board_id: int):
    board_item = board_list[board_id]
    if board_item.no == board_id:
        board_list.pop(board_id)
        return { "message": "Deleted successfully" }
    return { "message": "ID dosen't exist" }

@router.delete("")
async def delete_all_board():
    board_list.clear()
    return { "message": "Deleted successfully" }
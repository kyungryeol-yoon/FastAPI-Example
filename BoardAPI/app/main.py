from fastapi import FastAPI, Request
from app import board_api
# from helper.log_helper import setup_logger
# from browsepy import app as flask_app
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
# from fastapi.middleware.wsgi import WSGIMiddleware

app = FastAPI(
    title="Test API",
    description="Test 용도입니다.",
    version="0.0.1"
    )

origins = [
    # "http://localhost.tiangolo.com",
    # "https://localhost.tiangolo.com",
    "http://localhost",
    "http://0.0.0.0",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.add_middleware(LoggingMiddleware)

app.include_router(board_api.router)

# Swagger 숨김
@app.get("/", include_in_schema=False)
async def index(request: Request):
    current_url = str(request.url)
    url = f"{current_url}docs"

    return RedirectResponse(url)

@app.get(
    "/healthCheck",
    responses={
        200: {
            "title":"healthCheck",
            "description":"Health Check OK!",
        }
    },
    )
async def healthCheck():
    #logging.info("")
    return {"OK"}


# app.mount("/file-manager", WSGIMiddleware(flask_app))
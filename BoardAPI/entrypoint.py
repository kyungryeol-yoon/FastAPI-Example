import uvicorn
from app import main
from env_config import *

if __name__ == "__main__":
    uvicorn.run(main.app, host=SWAGGER_HOST, port=int(SWAGGER_PORT))

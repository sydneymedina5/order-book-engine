import uvicorn
import logging
from fastapi import FastAPI


def main():
    logging.info("Order book engine running")
    app = FastAPI()
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
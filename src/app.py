import logging
import uvicorn
from fastapi import FastAPI


def main():
    """Runner code for Ordering Book App"""
    
    logging.info("Order book engine running")
    app = FastAPI()
    uvicorn.run(app, host="0.0.0.0", port=8080)

if __name__ == "__main__":
    main()
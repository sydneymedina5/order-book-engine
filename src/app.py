import os
import logging
import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


def main():
    """Runner code for Ordering Book App"""
    
    logging.info("Order book engine running")
    app = FastAPI()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(base_dir, "../frontend/build")

    app.mount("/static", StaticFiles(directory=os.path.join(build_dir, "static")), name="static")

    # Serve HTML
    @app.get("/")
    def index():
        return FileResponse("frontend/build/index.html")
    
    @app.get("/api/orders")
    def get_orders():
        return [
            {"price": 101.0, "amount": 5},
            {"price": 100.5, "amount": 10},
            {"price": 100.0, "amount": 20},
        ]

    # Allow requests from your mobile app
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],    
    )

    uvicorn.run(app, host="0.0.0.0", port=8080)

if __name__ == "__main__":
    main()
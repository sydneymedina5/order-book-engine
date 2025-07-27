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
    
    # Serve JS/CSS from /static
    app.mount("/", StaticFiles(directory="static", html=True), name="static")

    # Serve HTML
    @app.get("/")
    def index():
        return FileResponse("frontend/build/index.html")

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
from pydantic_settings import BaseSettings
from pydantic import Field

class SimSettings(BaseSettings):
    """Settings"""
    
    url: str = Field(default="URL")
    
    class Config:
        """Sets ENV File to point to .env.sim"""
        
        env_file = ".env.sim"
    

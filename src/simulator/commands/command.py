from abc import ABC, abstractmethod


class Command(ABC):
    """Interface For a Command"""
    
    @abstractmethod
    def rest_request(self):
        """REST API Request"""
        pass
    
    @abstractmethod
    def execute(self):
        """Command Executeable Code"""
        pass
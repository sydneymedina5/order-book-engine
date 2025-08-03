import logging 
from queue import Queue
from threading import Thread, Event
from src.simulator.commands.command import Command
from src.simulator.engine.cmd_factory import CommandFactory, CommandEnum


class SimEngine(Thread):
    """Single Threaded Engine For Placing/Canceling Orders"""
    
    def __init__(self):
        super().__init__()
        self._event_queue = Queue()
        self._stop_event = Event()
        
    def run(self):
        """Running Event Loop To Generate and Execute Random Commands"""
        while not self._stop_event.is_set():
            try:
                # Generate Random Command Object 
                cmd: Command = CommandFactory().create(CommandEnum.RANDOM)
                # Execute Command
                cmd.execute()
            except Exception as e_x:
                logging.error(f"Exception In Sim Engine {e_x}")
        

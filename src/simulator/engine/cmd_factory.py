import random
import logging
from enum import Enum
from src.simulator.commands.command import Command
from src.simulator.commands.trade import Trade
from src.simulator.commands.new_order import NewOrder
from src.simulator.commands.cancel_order import CancelOrder
from src.simulator.commands.modify_order import ModifyOrder


class CommandEnum(Enum):
    """List Of Sim Commands"""
    RANDOM = "RANDOM" # Generates a random cmd below
    TRADE = "TRADE"
    CANCEL = "CANCEL"
    MODIFY = "MODIFY"
    NEW_ORDER = "NEW_ORDER"


class CommandFactory:
    """Generates a command object for simulator engine to execute"""
    
    def __init__(self) -> None:
        """Command Factory To Generate Commands"""
        # Generates a list of Valid Commands
        self._eligible_cmds = [cmd for cmd in CommandEnum if cmd != CommandEnum.RANDOM] 

    
    def create(self, cmd_enum: CommandEnum) -> Command:
        """Creates Command Object"""
        if cmd_enum == CommandEnum.RANDOM:
            # Generate a random command below 
            # Assign cmd enum to the generated cmd
            cmd_enum = random.choice(self._eligible_cmds)
        
        if cmd_enum == CommandEnum.TRADE:
            return Trade()
        
        elif cmd_enum == CommandEnum.CANCEL:
            return CancelOrder()
        
        elif cmd_enum == CommandEnum.MODIFY:
            return ModifyOrder()
        
        elif cmd_enum == CommandEnum.NEW_ORDER:
            return NewOrder()
        
        else:
            logging.error("Valid Command Option Not Selected. Try Again.")
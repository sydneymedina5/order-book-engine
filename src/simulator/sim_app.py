import json
import logging
from simulator.config import SimSettings


def configure_logging():
    """Configure Logging"""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )
    
def main():
    """Main"""
    configure_logging()
    
    logging.info("Setting Up Config")
    sim_settings = SimSettings()
    
    logging.info(f"Loaded Configuration {json.dumps(sim_settings.model_dump(), indent=2)}")
    
    logging.info("Starting Order Book Simulator")
    
    

if __name__ == "__main__":
    main()
    
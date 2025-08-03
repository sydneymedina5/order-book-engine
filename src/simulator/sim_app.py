import logging


def configure_logging():
    """Configure Logging"""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )
    
def main():
    """Main"""
    configure_logging()
    
    logging.info("Starting Order Book Simulator")

if __name__ == "__main__":
    main()
    
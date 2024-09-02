import logging

def setup_logger(log_file_path):
    """Sets up the logger to write logs to both a file and the console."""
    
    # Configure the logging system
    logging.basicConfig(
        level=logging.INFO,  # Set the logging level to INFO
        format='%(asctime)s - %(levelname)s - %(message)s',  # Define the log message format
        handlers=[
            logging.FileHandler(log_file_path),  # Log messages will be written to the specified file
            logging.StreamHandler()  # Log messages will also be output to the console
        ]
    )

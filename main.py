import time
import os
import logging
from cli import parse_arguments
from logger import setup_logger
from sync import sync_folders

def main():
    try:
        # Capture and process command-line arguments
        args = parse_arguments()
        source_path = args.source_path
        replica_path = args.replica_path
        sync_interval = args.sync_interval
        log_path = args.log_path

        # Set up the logger
        setup_logger(log_path)

        logging.info(f"Starting script with the following parameters:")
        logging.info(f"Source Path: {source_path}")
        logging.info(f"Replica Path: {replica_path}")
        logging.info(f"Sync Interval: {sync_interval} seconds")
        logging.info(f"Log Path: {log_path}")

        # Check if the source path exists
        if not os.path.exists(source_path):
            logging.error(f"Source path does not exist: {source_path}")
            raise FileNotFoundError(f"Source path does not exist: {source_path}")

        # Create the replica path if it does not exist
        if not os.path.exists(replica_path):
            try:
                os.makedirs(replica_path)
                logging.info(f"Replica path created: {replica_path}")
            except OSError as e:
                # Log an error and raise an exception if the directory creation fails
                logging.error(f"Failed to create replica path: {replica_path}, Error: {e}")
                raise

        logging.info(f"Starting folder synchronization every {sync_interval} seconds")

        while True:
            try:
                logging.info("Starting synchronization")
                # Synchronize the folders
                sync_folders(source_path, replica_path)
                logging.info("Synchronization completed successfully")
            except Exception as e:
                # Log an error if synchronization fails
                logging.error(f"Error during folder synchronization: {e}")

            # Wait for the synchronization interval
            try:
                time.sleep(sync_interval)
            except InterruptedError:
                # Log an informational message and exit if the sleep is interrupted
                logging.info("Synchronization interval interrupted.")
                break

    except KeyboardInterrupt:
        # Log an informational message if synchronization is stopped manually
        logging.info("Synchronization stopped manually.")
    except FileNotFoundError as e:
        # Log file not found errors
        logging.error(f"File not found error: {e}")
    except PermissionError as e:
        # Log permission errors
        logging.error(f"Permission error: {e}")
    except OSError as e:
        # Log OS-related errors
        logging.error(f"OS error: {e}")
    except Exception as e:
        # Log any unexpected errors
        logging.error(f"Unexpected error: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()

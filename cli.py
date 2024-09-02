import argparse
import os

def parse_arguments():
    parser = argparse.ArgumentParser(description="Synchronize two folders.")
    parser.add_argument('--source_path', required=True, help="Path to the source folder")
    parser.add_argument('--replica_path', required=True, help="Path to the replica folder")
    parser.add_argument('--sync_interval', type=int, required=True, help="Synchronization interval in seconds")
    parser.add_argument('--log_path', required=True, help="Path to the log file")

    # Parse the arguments provided by the user
    args = parser.parse_args()

    # Check if synchronization interval is a positive integer
    if args.sync_interval <= 0:
        parser.error("Synchronization interval must be a positive integer.")

    # Additional validation to check if the provided paths are valid
    if not os.path.isdir(args.source_path):
        parser.error(f"Source path does not exist or is not a directory: {args.source_path}")

    if not os.path.isdir(os.path.dirname(args.log_path)):
        parser.error(f"Directory for log path does not exist: {os.path.dirname(args.log_path)}")

    return args

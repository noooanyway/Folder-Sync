import os
import shutil
import hashlib
import logging

def calculate_file_hash(file_path):
    """Calculates the MD5 hash of a file to detect changes."""
    hash_md5 = hashlib.md5()
    try:
        # Open the file in binary mode and read it in chunks
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
    except IOError as e:
        # Log an error if the file cannot be read
        logging.error(f"Failed to read file for hashing: {file_path}, Error: {e}")
        return None
    return hash_md5.hexdigest()

def sync_folders(source, replica):
    """Synchronizes the contents of the source folder to the replica folder."""
    try:
        # Get the list of files and directories in both source and replica
        source_files = set(os.listdir(source))
        replica_files = set(os.listdir(replica))
    except OSError as e:
        # Log an error if there is an issue listing directory contents
        logging.error(f"Failed to list directory contents: {e}")
        return

    # Copy or update files and directories from source to replica
    for item in source_files:
        source_item_path = os.path.join(source, item)
        replica_item_path = os.path.join(replica, item)

        if os.path.isdir(source_item_path):
            # If the item is a directory and does not exist in the replica, copy it
            if not os.path.exists(replica_item_path):
                try:
                    shutil.copytree(source_item_path, replica_item_path)
                    logging.info(f"Directory created: {replica_item_path}")
                except Exception as e:
                    # Log an error if the directory creation fails
                    logging.error(f"Failed to create directory {replica_item_path}: {e}")
            else:
                # Recursively synchronize subdirectories
                sync_folders(source_item_path, replica_item_path)
        else:
            # If the item is a file
            if not os.path.exists(replica_item_path):
                # If the file does not exist in the replica, copy it
                try:
                    shutil.copy2(source_item_path, replica_item_path)
                    logging.info(f"File copied: {source_item_path} to {replica_item_path}")
                except Exception as e:
                    # Log an error if the file copy fails
                    logging.error(f"Failed to copy file {source_item_path} to {replica_item_path}: {e}")
            else:
                # If the file exists in both source and replica, check for changes
                source_hash = calculate_file_hash(source_item_path)
                replica_hash = calculate_file_hash(replica_item_path)

                if source_hash is None or replica_hash is None:
                    # If hash calculation fails, skip the file
                    continue

                if source_hash != replica_hash:
                    # If the file has changed, update it in the replica
                    try:
                        shutil.copy2(source_item_path, replica_item_path)
                        logging.info(f"File updated: {source_item_path} to {replica_item_path}")
                    except Exception as e:
                        # Log an error if the file update fails
                        logging.error(f"Failed to update file {source_item_path} to {replica_item_path}: {e}")

    # Remove files and directories in the replica that are not in the source
    for item in replica_files:
        if item not in source_files:
            replica_item_path = os.path.join(replica, item)
            try:
                if os.path.isdir(replica_item_path):
                    # Remove directories that are not in the source
                    shutil.rmtree(replica_item_path)
                    logging.info(f"Directory removed: {replica_item_path}")
                else:
                    # Remove files that are not in the source
                    os.remove(replica_item_path)
                    logging.info(f"File removed: {replica_item_path}")
            except Exception as e:
                # Log an error if removal fails
                logging.error(f"Failed to remove {replica_item_path}: {e}")

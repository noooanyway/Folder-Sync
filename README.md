# Folder Synchronizer
Python script designed to synchronize two folders at regular intervals.
Ensures that a replica folder is kept up-to-date with the content of a source folder.

## Synchronization Process
File and Directory Listing: The script lists the contents of both the source and replica folders.

   ### Synchronization
   
   For Directories: 
      If a directory exists in the source but not in the replica, it is copied. If the directory exists in both, its contents are recursively      synchronized.

   Files:
      If a file exists in the source but not in the replica, it is copied.
      If a file exists in both locations, its integrity is checked by comparing MD5 hashes. If the files differ, the file in the replica is updated.

   Cleanup:
      Files and directories present in the replica but not in the source are removed to ensure the replica remains an accurate reflection of the source.

## Structure
   folder_sync/
   
   ├── main.py           # Main script
   
   ├── sync.py           # Synchronization module
   
   ├── logger.py         # Logging module
   
   ├── cli.py            # Command-line arguments module
   
   └── README.md         # Project documentation

## Requirements
Make sure you have Python installed. This project uses standard Python libraries, so there is no need to install any dependencies. 

## How to Use
1) Clone the Repository to local machine.

   git clone https://github.com/noooanyway/folder-sync.git
   cd folder_sync

2) Run the Program
Execute the script with the following:

   python main.py --source_path "C:\path\to\source" --replica_path "C:\path\to\replica" --sync_interval 60 --log_path ".\sync.log"

Replace the placeholder paths with your actual paths

### Command-Line Descriptions
   --source_path: The path to the source folder you want to synchronize.
   
   --replica_path: The path to the folder where you want to create a replica.
   
   --sync_interval: The interval in seconds between each synchronization.
   
   --log_path: The path to the log file where synchronization logs will be saved.
   

NOTE: ".\sync.log" will write to the folder where its been executed. You can always use a path to write somewhere else. 

### Example
If you want to synchronize a folder at C:\Users\User\Desktop\source_folder with another folder at C:\Users\User\Desktop\replica_folder, and log the output to sync.log, you would use:

   python main.py --source_path "C:\Users\orest\Desktop\source_folder" --replica_path "C:\Users\orest\Desktop\replica_folder" --sync_interval 60 --log_path ".\sync.log"

## Contact
For further information or support, please contact orestmartyn00@gmail.com

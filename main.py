import os
import shutil
import logging
import time

def sync_folders(source_folder, replica_folder):
    """
    A function that synchronizes files between a source folder and a replica folder.
    
    parameters:
    - source_folder: The path to the source folder.
    - replica_folder: The path to the replica folder.
    
    this function iterates through the files in the source folder and checks if they exist in the replica folder. 
    If a file is missing in the replica folder or if it's different, it copies the file. 
    It also removes files from the replica folder that don't exist in the source folder.
    """
    # create the replica folder if it doesn't exist
    if not os.path.exists(replica_folder):
        os.makedirs(replica_folder)
    
    # iterate through files in source folder
    for root, _, files in os.walk(source_folder):
        for file in files:
            source_file_path = os.path.join(root, file)
            replica_file_path = os.path.join(replica_folder, os.path.relpath(source_file_path, source_folder))

            # If file doesn't exist in replica folder or it's different, copy it
            if not os.path.exists(replica_file_path) or \
               os.stat(source_file_path).st_mtime > os.stat(replica_file_path).st_mtime:
                shutil.copy2(source_file_path, replica_file_path)
                logging.info(f"Copied {source_file_path} to {replica_file_path}")
    
    # remove files from replica folder that don't exist in source folder
    for root, _, files in os.walk(replica_folder):
        for file in files:
            replica_file_path = os.path.join(root, file)
            source_file_path = os.path.join(source_folder, os.path.relpath(replica_file_path, replica_folder))
            
            if not os.path.exists(source_file_path):
                os.remove(replica_file_path)
                logging.info(f"Removed {replica_file_path}")

def setup_logging(log_file):
    """
    A function to set up logging configuration.

    Parameters:
    - log_file: The path to the log file.

    """
    # configure logging
    logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

    # create a handler for printing log messages to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)  # set the level to INFO to print only INFO messages
    formatter = logging.Formatter('Date:%(asctime)s  %(message)s', '%Y-%m-%d %H:%M:%S')  # format the log messages
    console_handler.setFormatter(formatter)

    # add the console handler to the root logger
    logging.getLogger().addHandler(console_handler)

def main():
    """
    A function that initializes variables, sets up logging, gets source and replica folder paths from user input,
    syncs the folders initially, and then enters a loop to periodically sync the folders based on the interval.
    """
    # directly assign values to interval and log_file
    interval = 30  # it syncs the folders every 30sec
    log_file = "sync_log.txt"  # example log file path

    setup_logging(log_file)

    # get source and replica folder paths from user input
    source_folder = input("Enter the path to the source folder: ")
    replica_folder = input("Enter the path to the replica folder: ")

    # initial synchronization of folders
    sync_folders(source_folder, replica_folder)

    # use a simple loop for periodic synchronization
    while True:
        sync_folders(source_folder, replica_folder)
        time.sleep(interval)

if __name__ == "__main__":
    main()

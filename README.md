# Folder Synchronization Program

This program synchronizes files between a source folder and a replica folder.

## Functionality:

The program iterates through the files in the source folder and checks if they exist in the replica folder. If a file is missing in the replica folder or if it's different, it copies the file. It also removes files from the replica folder that don't exist in the source folder.

## Dependencies:

- Python 3.x
- No third-party libraries are required. The program utilizes built-in Python libraries:
  - os
  - shutil
  - logging
  - time

## Usage:

1. Run the program.
2. Enter the path to the source folder when prompted.
3. Enter the path to the replica folder when prompted.
4. The program will sync the folders initially.
5. It will then enter a loop to periodically sync the folders based on the specified interval.

## Logging:

The program logs the synchronization actions to a log file.

### Log Format:

- Each log entry includes a timestamp and the action taken (e.g., file copied or removed).

## Example Usage:

Open a terminal in the folder where the program is located and run:

```
python main.py
```

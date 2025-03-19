# # Import the os module to work with files
# import os

# # pwd - print the current working directory
# print("Current working directory:", os.getcwd())


# # File paths

# TEXT_FILE_NAME = "data.txt"

# file_path = os.getcwd() + '/' + TEXT_FILE_NAME

# # May not work across all OSs
# # Using os.path.join helps put here
# # BETTER!
# file_path = os.path.join(os.getcwd() + '/' + TEXT_FILE_NAME)

# print(file_path)

from pathlib import Path

# Get the current working directory
current_dir = Path.cwd()

# Define the text file name
TEXT_FILE_NAME = "demo_files/data.txt"

# Create the full file path
file_path = current_dir / TEXT_FILE_NAME

print(file_path)

# Check if a file exists

# if(os.path.exists(file_path)):
#   print("File exists!")

if (Path.exists(file_path)):
    print("File exists!")
else:
    print("File not found!")

# Make a new directory

Path.mkdir("new_directory", )

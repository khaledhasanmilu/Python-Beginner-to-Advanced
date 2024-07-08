import os

def list_directory_contents(path):
    try:
        # List all files and directories in the given path
        contents = os.listdir(path)
        print(f"Contents of '{path}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory '{path}'.")

# Specify the directory you want to list
directory_path = "/New Folder"  # You can change this to any directory path you want to list

list_directory_contents(directory_path)

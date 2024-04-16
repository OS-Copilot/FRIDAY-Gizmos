import os
import zipfile
from pathlib import Path


def zip_files(folder_path, zip_name, working_directory=None):
    """
    Create a zip archive of all files in the specified folder.

    Args:
        folder_path (str): The path to the folder whose files are to be zipped.
        zip_name (str): The name of the resulting zip file.
        working_directory (str, optional): The working directory where the folder is located. 
            If not provided, the current working directory is used.

    Returns:
        None: This method performs a task and does not return a value.
    """
    # Use the provided working directory or the current working directory if not provided
    working_directory = working_directory or os.getcwd()
    
    # Change the current working directory to the specified path
    os.chdir(working_directory)
    
    # Ensure the folder path is a Path object for compatibility
    folder_path = Path(folder_path)
    
    # Construct the full path for the zip file
    zip_file_path = folder_path.parent / f"{zip_name}.zip"
    
    # Create a zip file and add all files from the specified folder
    with zipfile.ZipFile(zip_file_path, 'w') as zipf:
        for file in folder_path.glob('*'):
            if file.is_file():
                zipf.write(file, arcname=file.name)
    
    print(f"Task completed: '{zip_file_path}' has been created with all files from '{folder_path}'.")



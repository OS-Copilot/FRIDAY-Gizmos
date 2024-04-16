
import json
import os
import kwargs

def extract_jsonl_content(jsonl_file_path):
    """
    Extract the full text content of the specified JSON Lines file and return its content.

    Args:
        jsonl_file_path (str): The absolute path to the JSON Lines file to be read.

    Returns:
        list: A list of dictionaries, each representing a line in the JSON Lines file.
    """
    try:
        # Change the current working directory to the specified path if provided
        working_dir = kwargs.get('working_dir', os.getcwd())
        os.chdir(working_dir)

        # Ensure the JSON Lines file exists
        if not os.path.isfile(jsonl_file_path):
            print(f"The JSON Lines file {jsonl_file_path} does not exist.")
            return

        # Read the JSON Lines file
        content = []
        with open(jsonl_file_path, 'r', encoding='utf-8') as file:
            for line in file:
                content.append(json.loads(line.strip()))

        print(f"Task execution complete. Content of the JSON Lines file {jsonl_file_path} extracted successfully.")
        return content
    except FileNotFoundError:
        print(f"The JSON Lines file {jsonl_file_path} does not exist.")
    except json.JSONDecodeError as e:
        print(f"An error occurred while parsing the JSON Lines file {jsonl_file_path}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


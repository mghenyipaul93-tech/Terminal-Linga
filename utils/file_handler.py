import os
import json


def ensure_directory(path):
    """
    Ensure the directory for a file exists.
    """
    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)


def file_exists(path):
    """
    Check if a file exists.
    """
    return os.path.exists(path)


def read_file(path):
    """
    Read a text file.
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return None


def write_file(path, content):
    """
    Write content to a text file (overwrite).
    """
    ensure_directory(path)
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)


def append_file(path, content):
    """
    Append content to a file.
    """
    ensure_directory(path)
    with open(path, "a", encoding="utf-8") as file:
        file.write(content + "\n")


def read_json(path):
    """
    Read JSON data from a file.
    """
    if not file_exists(path):
        return {}

    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {}


def write_json(path, data):
    """
    Write JSON data to a file.
    """
    ensure_directory(path)
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def delete_file(path):
    """
    Delete a file if it exists.
    """
    if file_exists(path):
        os.remove(path)
        return True
    return False
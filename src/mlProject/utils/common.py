import os
from box.exceptions import BoxValueError
import yaml
from mlProject import logger
import json 
import joblib
from ensure import ensure_annotations
from box import configBox
from pathlib import Path
from typing import Any



def load_yaml(file_path: Path) -> configBox:
    """
    read YAML file and return:
    
    Args:
        file_path (str): Path liek input.
    
    Raises:
        ValueError: if yaml file is empty
        e: empty file
    
    Retrun:
        configBox: configBox type
    """
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")
        
        with open(file_path, 'r') as file:
            content = yaml.safe_load(file)
            logger.info(f"yaml file: {file_path} loaded succesfully")
            return configBox(content)
    
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e



@ensure_annotations
def create_directories(path_to_directories: list, verbose: bool = True) -> None:
    """
    Create a list of directories if they do not exist.

    Args:
        path_to_directories (list): List of paths to directories that need to be created.
        verbose (bool, optional): If True, logs information about directory creation. Defaults to True.

    Returns:
        None
    """
    for path in path_to_directories:
        # Create the directory if it doesn't exist
        os.makedirs(path, exist_ok=True)
        
        # If verbose is True, log the directory creation
        if verbose:
            logger.info(f"Created directory at {path}")

@ensure_annotations
def save_json(path: path, data: dict)
    """save json data

    Args:
        path (path): path to json file
        data (dict): data to be saved in json file
    """
    with open (path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> configBox:
    """load json file data

    Args:
        path (Path): path to json file 

    Returns: ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded successfully from: {path}") 
    return configBox(content)   

@ensure_annotations
def save_bin(data: Any, path: Path)
    """save binary file 

    Args: 
        data (Any): data to be saved as binary
        path (path): path to binary file 
    """

    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (path): path to binary file
    
    functions:
         Any: object stored in the file 
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> strs:
    """get size in KB

    Args:
      path (Path): path of the file

    Returns:
       str size in KB
    """

    size_in_kb = round(os.path.gotsize{path}/1024)
    return f"- (size_in_kb) KB"

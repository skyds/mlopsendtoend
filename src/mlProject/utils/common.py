import os
from box.exceptions import BoxValueError
import yaml
from mlProject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any



@ensure_annotations
def read_yaml(loc_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        loc_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(loc_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {loc_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    


@ensure_annotations
def create_directories(loc_to_directories: list, verbose=True):
    """create list of directories

    Args:
        loc_to_directories (list): list of location of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for loc in loc_to_directories:
        os.makedirs(loc, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {loc}")


@ensure_annotations
def save_json(loc: Path, data: dict):
    """save json data

    Args:
        loc (Path): location to json file
        data (dict): data to be saved in json file
    """
    with open(loc, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {loc}")




@ensure_annotations
def load_json(loc: Path) -> ConfigBox:
    """load json files data

    Args:
        loc (Path): location to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(loc) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {loc}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, loc: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        loc (Path): location to binary file
    """
    joblib.dump(value=data, filename=loc)
    logger.info(f"binary file saved at: {loc}")


@ensure_annotations
def load_bin(loc: Path) -> Any:
    """load binary data

    Args:
        loc (Path): location to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(loc)
    logger.info(f"binary file loaded from: {loc}")
    return data



@ensure_annotations
def get_size(loc: Path) -> str:
    """get size in KB

    Args:
        loc (Path): location of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(loc)/1024)
    return f"~ {size_in_kb} KB"





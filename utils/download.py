import os
import gdown
import zipfile
import logging

def check_dir(dir_name: str) -> bool:
    return os.path.isdir(dir_name)

def download_data(dir_name: str = "data") -> None:
    if not check_dir(dir_name=dir_name):
        os.mkdir(dir_name)
    os.chdir(dir_name)
    logging.info("Downloading data....")
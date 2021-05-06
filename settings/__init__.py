import os
import yaml

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def download_config():
    with open(os.path.join(os.path.dirname(__file__), "hh.yaml"), "r") as f:
        conf = yaml.load(f, Loader=yaml.FullLoader)
    return conf


config = download_config()

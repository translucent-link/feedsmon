from yaml import load
import os

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def load_config():

    cfg_path = os.environ.get("FEEDSMON_CONFIG")
    if cfg_path is None:
        cfg_path = "./feedsmon.yml"

    with open(cfg_path, "r") as f:
        return load(f, Loader=Loader)

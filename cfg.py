from yaml import load

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def load_config():
    with open("feedsmon.yml", "r") as f:
        return load(f, Loader=Loader)

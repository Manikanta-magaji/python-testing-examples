import json

class MysteryError(Exception):
    pass


def add(a, b):
    if a == 99:
        raise MysteryError()
    return a + b


def read_json(some_file_path):
    with open(some_file_path) as f:
        return json.load(f)

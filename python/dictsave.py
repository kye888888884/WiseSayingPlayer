from inspect import _void
import json


def save(dict: dict, filename: str) -> None:
    with open(filename, 'w', encoding='UTF-8') as f:
        json.dump(dict, f, indent=2)


def get(filename: str) -> dict:
    with open(filename, 'r', encoding='UTF-8') as f:
        return json.loads(f.read())

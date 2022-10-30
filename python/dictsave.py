import json


def save(dict):
    with open('data/wordchain.json', 'w', encoding='UTF-8') as f:
        json.dump(dict, f, indent=2)


def get():
    with open('data/wordchain.json', 'r', encoding='UTF-8') as f:
        return json.loads(f.read())

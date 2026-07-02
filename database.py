import json
from pathlib import Path

DATABASE = "data.json"


def load_data():
    if not Path(DATABASE).exists():
        with open(DATABASE, "w") as file:
            json.dump([], file, indent=4)

    with open(DATABASE, "r") as file:
        return json.load(file)


def save_data(data):
    with open(DATABASE, "w") as file:
        json.dump(data, file, indent=4)
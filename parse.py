import csv
from dataclasses import dataclass

@dataclass
class Hotkey():
    name: str
    key: str

@dataclass
class HotkeyCategory():
    name: str
    hotkeys: list[Hotkey]


def build_hotkeys(csv_path: str) -> list[HotkeyCategory]:
    categories = []
    with open(csv_path, "r", encoding="utf8") as file:
        reader = csv.reader(file)

        # skip header
        next(reader)

        # get categories
        for column in next(reader):
            if column:
                categories.append(HotkeyCategory(column, []))

        # get hotkeys
        for row in reader:
            sectionIndex = 0
            definition = None
            for column in row:
                if column:
                    if not definition:
                        definition = column
                    else:
                        categories[sectionIndex].hotkeys.append(Hotkey(definition, column))
                        definition = None
                        sectionIndex += 1


    return categories


if __name__ == "__main__":
    print(str(build_hotkeys("shortcuts.csv")))
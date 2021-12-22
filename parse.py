import csv
from dataclasses import dataclass


@dataclass
class KeyData:
    raw: str
    # isNice determines whether you use raw or combination
    isNice: bool
    combination: list[str]


@dataclass
class Hotkey():
    name: str
    key: KeyData


@dataclass
class HotkeyCategory():
    name: str
    hotkeys: list[Hotkey]
    position: int


def gen_keydata(raw: str) -> KeyData:
    raw = raw.strip()

    def strip_array(arr: list[str]) -> list[str]:
        return [x.strip() for x in arr]

    if not " " in raw:
        return KeyData(raw, True, [raw.strip()])

    elif "+" in raw or "then" in raw:
        return KeyData(raw, True, strip_array(raw.replace("+", "DELIMITERPY").replace("then", "DELIMITERPY").split("DELIMITERPY")))

    else:
        return KeyData(raw, False, [raw.strip()])


def build_hotkeys(csv_path: str) -> list[HotkeyCategory]:
    categories = []
    with open(csv_path, "r", encoding="utf8") as file:
        reader = csv.reader(file)

        # skip header
        next(reader)

        # get categories
        indexes = []

        skip = False
        for index, column in enumerate(next(reader)):
            if column:
                if skip:
                    skip = False
                    continue

                categories.append(HotkeyCategory(column, [], index))
                indexes.append({"name": index, "data": index + 2})
                skip = True

        # get hotkeys
        for row in reader:
            for index in indexes:
                if row[index["name"]] and row[index["data"]]:
                    for hotkeyCategory in categories:
                        if hotkeyCategory.position == index["name"]:
                            hotkeyCategory.hotkeys.append(Hotkey(row[index["name"]], gen_keydata(row[index["data"]])))

    return categories


if __name__ == "__main__":
    print(str(build_hotkeys("shortcuts.csv")))

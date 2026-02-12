import json
import os
import sys
import PyInstaller.__main__

file_list = [
    "all.qss", "main.py", "settings.json", "designes_py", "translations",
    "design.py", "findText.py", "modules.py", "settingsWindow.py", "eng.qm", "ru.qm"
]

path = "\\".join(os.path.abspath(os.path.dirname(__file__)).split("\\")[:-1]) + "\\"

if hasattr(sys, "_MEIPASS"):
    path = os.path.join(sys._MEIPASS) + "\\"

def make_exe() -> bool:
    try:
        temp = os.listdir(path) + os.listdir(path + "designes_py") + os.listdir(path + "translations")
    except FileNotFoundError:
        return False
    for file in file_list:
        if file not in temp:
            return False
    try:
        PyInstaller.__main__.run([
            path + "main.py", "-w", "--onefile", "--add-data", path + "all.qss;.", "--add-data", 
            path + "settings.json;.", "--add-data", path + "designes_py;designes_py", "--add-data",
            path + "translations;translations"
        ])
    except Exception:
        return False
    return True

def _get_qss() -> dict[str, list[str]]:
    code = []
    key = None
    result = {}
    _isfind = False
    with open(path + "all.qss", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if "}" in line:
                _isfind = False
                result[key] = code.copy()
                code.clear()

            elif _isfind:
                code.append(line)

            elif "Q" in line:
                _isfind = True
                key = line.split("{")[0].strip()
                result[key] = None
    return result

def parse_qss(name: str) -> str:
    soup = _get_qss()
    result = ""
    keys = [_name for _name in soup.keys() if name in _name]
    for key in keys:
        result += key + " {"
        for token in soup[key]:
            result += "\n\t" + token
        result += "\n}\n\n"
    result = result[:-2]
    return result

def generate_basic_settings() -> dict[str, bool]:
    settings = {
        "File-numeration": False,
        "StatusBar-info": True,
        "Self-clear": False,
        "Confirmation": True,
        "QSS-styles": True,
        "Auto-save": False,
        "Save_seconds": 0,
        "Clear_seconds": 0
    }
    return settings

def updateFileConfig(settings: dict[str, bool]) -> None:
    with open(path + "settings.json", "w", encoding="utf-8") as f:
        json.dump(settings, f, ensure_ascii=False, indent=4)

def get_settings() -> dict[str, bool] | None:
    try:
        with open(path + "settings.json", "r", encoding="utf-8") as f:
            settings = json.load(f)
            return settings
    except FileNotFoundError:
        return None

def multiply_parser(*names) -> str:
    result = ""
    for name in names:
        result += parse_qss(name)
        result += "\n\n"
    return result[:-2]


if __name__ == "__main__":
    print(make_exe())

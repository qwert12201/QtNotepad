import os
import shutil

def future():
    os.system("pyuic6 designes_ui/design.ui -o designes_py/design.py")
    os.system("pyuic6 designes_ui/findText.ui -o designes_py/findText.py")
    dir_list = os.listdir()
    if "test" in dir_list:
        shutil.rmtree("test")
        os.mkdir("test")
        for i in range(0, 11):
            with open(f"test/testFile_{i}.txt", "w", encoding="utf-8"): pass
        print("We will be together once again my love")

def _get_qss() -> dict[str, list[str]]:
    code = []
    key = None
    result = {}
    _isfind = False
    with open("all.qss", "r", encoding="utf-8") as f:
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


if __name__ == "__main__":
    pass

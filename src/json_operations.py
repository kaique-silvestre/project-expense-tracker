import json
import pathlib


class JsonOperations:
    struct = {
        1: {"Limite": None, "Total": None},
        2: {"Limite": None, "Total": None},
        3: {"Limite": None, "Total": None},
        4: {"Limite": None, "Total": None},
        5: {"Limite": None, "Total": None},
        6: {"Limite": None, "Total": None},
        7: {"Limite": None, "Total": None},
        8: {"Limite": None, "Total": None},
        9: {"Limite": None, "Total": None},
        10: {"Limite": None, "Total": None},
        11: {"Limite": None, "Total": None},
        12: {"Limite": None, "Total": None},
    }

    @staticmethod
    def create(path_file: pathlib.Path, custom_indent=4,):
        struct = {
        1: {"Limite": None, "Total": None},
        2: {"Limite": None, "Total": None},
        3: {"Limite": None, "Total": None},
        4: {"Limite": None, "Total": None},
        5: {"Limite": None, "Total": None},
        6: {"Limite": None, "Total": None},
        7: {"Limite": None, "Total": None},
        8: {"Limite": None, "Total": None},
        9: {"Limite": None, "Total": None},
        10: {"Limite": None, "Total": None},
        11: {"Limite": None, "Total": None},
        12: {"Limite": None, "Total": None},
        }


        if not pathlib.Path(path_file).exists():
            path_file.touch()
            with open(path_file, "w", encoding='utf-8') as file:
                json.dump([struct], file, indent=custom_indent)
        else:
            with open(path_file, "r+", encoding='utf-8') as file:
                try:
                    json_object = json.load(file)
                except Exception:
                    json.dump([struct], file, indent=custom_indent)


    @staticmethod
    def return_json(path_file):
        with open(path_file, "r", encoding='utf-8') as file:
            json_object = json.load(file)
            return list(json_object)
    
    @staticmethod
    def send_json(path_file, database, custom_ident=4):
        with open(path_file, "w+", encoding='utf-8') as file:
            json.dump(database, file, indent=custom_ident)
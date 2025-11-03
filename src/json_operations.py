import json
import pathlib


class JsonOperations:
    JSON_FOLDER_PATH = pathlib.Path(__file__).parent.parent / "jsons"
    BUDGET_FILE = JSON_FOLDER_PATH / "budget_data.json"
    DATABASE_FILE = JSON_FOLDER_PATH / "budget_data.json"
    

    def create_folder(self, folder_path):
        pathlib.Path(folder_path).mkdir(exist_ok=True)
    
    def create_file(self, file_path):
        pathlib.Path(file_path).touch(exist_ok=True)
    
    def send_budget(self, file_path):
        if not pathlib.Path(file_path).exists():
            JsonOperations.send_json(file_path, self.STRUCT)
        else:
            try:
                json_object = JsonOperations.return_json(file_path)
            except Exception:
                JsonOperations.send_json(file_path, self.STRUCT)

                

    
    @staticmethod
    def return_json(path_file):
        with open(path_file, "r", encoding='utf-8') as file:
            json_object = json.load(file)
            return list(json_object)
    
    @staticmethod
    def send_json(path_file, database, custom_ident=4):
        with open(path_file, "w+", encoding='utf-8') as file:
            json.dump(database, file, indent=custom_ident)


    


    """
    @staticmethod
    def create_file(path_file: pathlib.Path, custom_indent=4,):
        if not pathlib.Path(path_file).exists():
            path_file.touch()
            with open(path_file, "w", encoding='utf-8') as file:
                json.dump([], file, indent=custom_indent)
        else:
            with open(path_file, "r+", encoding='utf-8') as file:
                try:
                    json_object = json.load(file)
                except Exception:
                    json.dump([], file, indent=custom_indent)

    @staticmethod
    def create_folder(folder_path):
        pathlib.Path(folder_path).mkdir(exist_ok=True)

    @staticmethod
    def insert_budget(folder_path, database):
        struct = [{
            "01" : {"budget": None},
            "02" : {"budget": None},
            "03" : {"budget": None},
            "04" : {"budget": None},
            "05" : {"budget": None},
            "06" : {"budget": None},
            "07" : {"budget": None},
            "08" : {"budget": None},
            "09" : {"budget": None},
            "10" : {"budget": None},
            "11" : {"budget": None},
            "12" : {"budget": None},
        }]

"""
import pathlib
import json

class JsonOperations:
    database_folder_name = "model"
    folder_path = pathlib.Path(__file__).parent.parent
    model_folder = folder_path / database_folder_name
    BUDGET_FILE = model_folder / "budget.json"
    DATABASE_FILE = model_folder / "database.json"
    EXPORT_PATH = pathlib.Path(__file__).parent.parent / "model" / "expeneses.csv"

    STRUCT = \
    {
        1 : None,
        2 : None,
        3 : None,
        4 : None,
        5 : None,
        6 : None,
        7 : None,
        8 : None,
        9 : None,
        10: None,
        11: None,
        12: None,
    }



    @classmethod
    def creation(cls):
        cls.create_folders(cls.model_folder)
        cls.create_files(cls.BUDGET_FILE, cls.DATABASE_FILE)
        cls.send_budget_keys()
        cls.send_database_keys()

    @classmethod
    def create_files(cls, *file_list):
        for file in file_list:
            file.touch(exist_ok=True)

    @classmethod
    def create_folders(cls, *folders: pathlib.Path):
        for folder in folders:
            folder.mkdir(exist_ok=True, parents=True)

    @classmethod
    def send_budget_keys(cls):
        with open(cls.BUDGET_FILE, "r+", encoding="UTF-8") as file:
            try: 
                data = json.load(file)
            except json.JSONDecodeError:
                json.dump([cls.STRUCT], file, indent=4)

    @classmethod
    def send_database_keys(cls):
        with open(cls.DATABASE_FILE, "r+", encoding="UTF-8") as file:
            try: 
                data = json.load(file)
            except json.JSONDecodeError:
                json.dump([], file, indent=4)

    @staticmethod
    def return_json(path_file):
        with open(path_file, "r", encoding='utf-8') as file:
            json_object = json.load(file)
            return list(json_object)
    
    @staticmethod
    def send_json(path_file, database):
        with open(path_file, "w+", encoding='utf-8') as file:
            json.dump(database, file, indent=4)


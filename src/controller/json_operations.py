import pathlib
import json

class JsonOperations:
    database_folder_name = "model"
    folder_path = pathlib.Path(__file__).parent.parent
    model_folder = folder_path / database_folder_name
    BUDGET_FILE = model_folder / "budget.json"
    DATABASE_FILE = model_folder / "database.json"

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

    def creation(self):
        self.create_folder()
        self.create_file()
        self.send_keys_budget()
        self.send_keys_database()


    def create_file(self):
        self.model_folder.mkdir(exist_ok=True)
        self.BUDGET_FILE.touch(exist_ok=True)
        self.DATABASE_FILE.touch(exist_ok=True)

    def send_keys_budget(self):
        with open(self.BUDGET_FILE, "r+", encoding="UTF-8") as file:
            try: 
                data = json.load(file)
            except json.JSONDecodeError:
                json.dump([self.STRUCT], file, indent=4)

    def send_keys_database(self):
        with open(self.DATABASE_FILE, "r+", encoding="UTF-8") as file:
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





        

    def create_folder(self):...

if __name__ == "__main__":
    jsons = JsonOperations()

    jsons.create_file()
    jsons.send_keys_budget()
    jsons.send_keys_database()
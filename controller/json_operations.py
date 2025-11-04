import pathlib
import json

class JsonOperations:
    def __init__(self):
        self.database_folder_name = "model"
        self.folder_path = pathlib.Path(__file__).parent.parent
        self.model_folder = self.folder_path / self.database_folder_name
        self.BUDGET_FILE = self.model_folder / "budget.json"
        self.DATABASE_FILE = self.model_folder / "database.json"

        self.STRUCT = \
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


    def create_file(self):
        self.model_folder.mkdir(exist_ok=True)
        self.BUDGET_FILE.touch(exist_ok=True)
        self.DATABASE_FILE.touch(exist_ok=True)

    def send_keys_budget(self):
        with open(self.BUDGET_FILE, "r+", encoding="UTF-8") as file:
            try: 
                data = json.load(file)
            except json.JSONDecodeError:
                json.dump([], file, indent=4)

    def send_keys_database(self):
        with open(self.DATABASE_FILE, "r+", encoding="UTF-8") as file:
            try: 
                data = json.load(file)
            except json.JSONDecodeError:
                json.dump([self.STRUCT], file, indent=4)




        

    def create_folder(self):...

if __name__ == "__main__":
    jsons = JsonOperations()

    jsons.create_file()
    jsons.send_keys_budget()
    jsons.send_keys_database()
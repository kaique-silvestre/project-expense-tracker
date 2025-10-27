from src.json_operations import JsonOperations
from src.validations import Validation
from datetime import datetime

class Add:
    @staticmethod
    def add(path_file, database: list, args):
        if args.date:
            date_type_str = Validation.correctly_datatype_str(args.date)
        else:
            date_type_str = datetime.strftime(datetime.today(), "%d/%m/%Y")

        values = {"id": 1, "amount": args.amount, "category": args.category, "date": date_type_str, "description": args.description}
        if len(database) >= 1:
            real_id = database[-1]["id"] + 1
            values["id"] = real_id
        database.append(values)
        JsonOperations.send_json(path_file, database)
        print(f"\n# Expense added successfully (ID: {values['id']})\n")
            
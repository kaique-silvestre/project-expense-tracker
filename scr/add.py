from json_operations import JsonOperations
from validations import Validation

class Add:
    @staticmethod
    def add(path_file, database: list, args):
        Validation.is_positive(args.amount)
        if args.date:
            Validation.date_validation(args.date)
            

        values = {"id": 0, "amount": args.amount, "category": args.category, "date": args.date, "description": args.description}
        if len(database) >= 1:
            real_id = database[-1]["id"] + 1
            values["id"] = real_id
        database.append(values)
        JsonOperations.send_json(path_file, database)
        print(f"\n# Expense added successfully (ID: {values['id']})\n")
            
from controller.json_operations import JsonOperations
from controller.budget import Budget
from datetime import datetime
from controller.validation import Validation


# Verificar a adição de zero

class Add:
    date_format = "%d/%m/%Y"

    @classmethod
    def add(cls, database, args):  
        values = {"id": 1, "amount": args.amount, "category": args.category, "date": cls.date_validation(args.date), "description": args.description}

        # Validating if the amount added in the month blows the budget, it will become a function

        Validation.budget_validation(database, values)

        if len(database) >= 1:
            real_id = database[-1]["id"] + 1
            values["id"] = real_id
        database.append(values)
        JsonOperations.send_json(JsonOperations.DATABASE_FILE, database)
        print(f"\n# Expense added successfully (ID: {values['id']})\n")


    @classmethod
    def date_validation(cls, date):
        if date is None:
            date_today_date = datetime.date(datetime.today())
            date_today_str = datetime.strftime(date_today_date, cls.date_format)
            return date_today_str
        else:
            date_date = datetime.strptime(date, cls.date_format)
            date_str = datetime.strftime(date_date, cls.date_format)
            return date_str
        
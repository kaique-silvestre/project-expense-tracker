from controller.json_operations import JsonOperations
from controller.budget import Budget
from datetime import datetime


# Verificar a adição de zero

class Add:
    date_format = "%d/%m/%Y"

    def add_flow(self, database, args, budget_file):
        # Correção de data 
        # Adição
        self.add(database, args)


    def add(self, database, args):  
        values = {"id": 1, "amount": args.amount, "category": args.category, "date": self.date_validation(args.date), "description": args.description}

        # Validating if the amount added in the month blows the budget, it will become a function
        total_budget = values["amount"]
        ty = datetime.strptime(values["date"], self.date_format)
        if ty.year == datetime.today().year:
            budget_value = JsonOperations.return_json(JsonOperations.BUDGET_FILE)
            if budget_value[0][str(ty.month)] is not None:
                for item in database:
                    ty2 = datetime.strptime(item["date"], self.date_format)
                    if ty.month == ty2.month:
                        total_budget += item["amount"]
                if total_budget > budget_value[0][str(ty.month)]:
                    print("ERRO", total_budget, budget_value[0][str(ty.month)])

        if len(database) >= 1:
            real_id = database[-1]["id"] + 1
            values["id"] = real_id
        database.append(values)
        JsonOperations.send_json(JsonOperations.DATABASE_FILE, database)
        print(f"\n# Expense added successfully (ID: {values['id']})\n")


    def date_validation(self, date):
        if date is None:
            date_today_date = datetime.date(datetime.today())
            date_today_str = datetime.strftime(date_today_date, self.date_format)
            return date_today_str
        else:
            date_date = datetime.strptime(date, self.date_format)
            date_str = datetime.strftime(date_date, self.date_format)
            return date_str
        
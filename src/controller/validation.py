from datetime import datetime
from controller.json_operations import JsonOperations


class Validation:

    def date_validation():...

    @classmethod
    def date_to_str(cls, date, date_format="%d/%m/%Y"):
        date = datetime.strftime(date, date_format)
        return date

    @classmethod
    def str_to_date(cls, string, date_format="%d/%m/%Y"):
        date = datetime.strptime(string, date_format).date()
        return date

    @classmethod
    def budget_validation(self, database, values):
        total_spends = values["amount"]
        expense_date = Validation.str_to_date(values["date"])
        if expense_date.year == datetime.today().year:
            budget_value = JsonOperations.return_json(JsonOperations.BUDGET_FILE)
            if budget_value[0][str(expense_date.month)] is not None:
                for item in database:
                    database_expense =  Validation.str_to_date(item["date"])
                    if expense_date.month == database_expense.month:
                        total_spends += item["amount"]
                if total_spends >= budget_value[0][str(expense_date.month)]:
                    print(f"\n[ERROR]: Monthly budget exceeded. Total spends/Monthly Budget: {total_spends}/{budget_value[0][str(expense_date.month)]}")


if __name__ == "__main__":
    date = Validation.str_to_date("31/10/2025")
    print(date)
    date = Validation.date_to_str(date)
    print(date)
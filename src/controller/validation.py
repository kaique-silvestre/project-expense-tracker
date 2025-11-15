from datetime import datetime
from controller.json_operations import JsonOperations
from controller.error import *


class Validation:

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

    # Upper Level
    def add_validation(self, args):
        try:
            self.amount_validations(args.amount)
            self.category_validation(args.category)
            self.description_validation(args.description)
        except NegativeNumbersError:
            print("\n[ERROR] The number provided cannot be negative.\n")
            exit()
        except StringIsTooLongError:
            print("\n[ERROR] The input string is too long. Please use a shorter one.\n")
            exit()
        except ValueIsTooHighError:
            print("\n[ERROR] The value provided is too high. Please enter a smaller value.\n")
            exit()
        except MonthDoesntExistError:
            print("\n[ERROR] The value provided is too high. Please enter a smaller value.\n")
            exit()





    def delete_validation(self, args):
        try: 
            self.are_positivies(args.id)
        except NegativeNumbersError:
            print("\n[ERROR] The number provided cannot be negative.\n")
            exit()
        except StringIsTooLongError:
            print("\n[ERROR] The input string is too long. Please use a shorter one.\n")
            exit()
        except ValueIsTooHighError:
            print("\n[ERROR] The value provided is too high. Please enter a smaller value.\n")
            exit()
        except MonthDoesntExistError:
            print("\n[ERROR] The value provided is too high. Please enter a smaller value.\n")
            exit()


    def update_validation(self, args):
        try: 
            # id
            self.are_positivies(args.id)
            # amount
            self.amount_validations(args.amount)
            # category
            self.category_validation(args.category)
            # description
            self.description_validation(args.description)
        except NegativeNumbersError:
            print("\n[ERROR] The number provided cannot be negative.\n")
            exit()
        except StringIsTooLongError:
            print("\n[ERROR] The input string is too long. Please use a shorter one.\n")
            exit()
        except ValueIsTooHighError:
            print("\n[ERROR] The value provided is too high. Please enter a smaller value.\n")
            exit()
        except MonthDoesntExistError:
            print("\n[ERROR] The value provided is too high. Please enter a smaller value.\n")
            exit()

    def list_validation(self, args):
        try:
            self.year_validation(args.year)
            self.month_validation(args.month)
            self.category_validation(args.category)
            self.is_positive(args.less)
            self.is_positive(args.greater)
            self.amount_validations(args.amount)
        except NegativeNumbersError:
            print("\n[ERROR] The number provided cannot be negative.\n")
            exit()
        except StringIsTooLongError:
            print("\n[ERROR] The input string is too long. Please use a shorter one.\n")
            exit()
        except ValueIsTooHighError:
            print("\n[ERROR] The value provided is too high. Please enter a smaller value.\n")
            exit()
        except MonthDoesntExistError:
            print("\n[ERROR] The value provided is too high. Please enter a smaller value.\n")
            exit()

    def budget_set_validation(self, args):
        try:
            self.is_positive(args.value)
            self.month_validation(args.month)
        except NegativeNumbersError:
            print("\n[ERROR] The number provided cannot be negative.\n")
            exit()
        except StringIsTooLongError:
            print("\n[ERROR] The input string is too long. Please use a shorter one.\n")
            exit()
        except ValueIsTooHighError:
            print("\n[ERROR] The value provided is too high. Please enter a smaller value.\n")
            exit()
        except MonthDoesntExistError:
            print("\n[ERROR] The value provided is too high. Please enter a smaller value.\n")
            exit()

    def budget_delete_validation(self, args):
        self.month_validation(args.month)

    # middle level
    def year_validation(self, year):
        if year is not None:
            self.is_positive(year)
            self.int_len_validation(year, 2099)

    def month_validation(self, month):
        if month is not None:
            if month not in [i for i in range(1, 13)]:
                raise MonthDoesntExistError()

    def amount_validations(self, amount):
        if amount is not None:
            self.is_positive(amount)
            self.int_len_validation(amount, 1_000_000_000)



    def category_validation(self, category):
        if category is not None:
            self.str_lenght_validationn(category, 20)


    def description_validation(self, description):
        if description is not None:
            self.str_lenght_validationn(description, 100)




    # low level
    def are_positivies(self, numbers):
        for number in numbers:
            if number <= 0:
                raise NegativeNumbersError()
    

    def is_positive(self, number):
        if number is not None:
            if number <= 0:
                raise NegativeNumbersError()
    
    def str_lenght_validationn(self, string, max_lenght):
        if len(string) > max_lenght:
            raise StringIsTooLongError()
        
    def int_len_validation(self, num, max_lenght):
        if num > max_lenght:
            raise ValueIsTooHighError()
            



if __name__ == "__main__":
    date = Validation.str_to_date("31/10/2025")
    print(date)
    date = Validation.date_to_str(date)
    print(date)
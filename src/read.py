from datetime import datetime
from copy import deepcopy

class Read:
    @staticmethod
    def list(database):
        if not database:
            print("# Nenhum gasto registrado ainda.")
        else:
            print("-" * 80)
            print(f"{'ID':<5} {'AMOUNT':<15} {'DATE':<15} {'CATEGORY':<15} {'DESCRIPTION'}")
            print("-" * 80)
            for line in database:
                print(f"{line['id']:<5} {line['amount']:<15.2f} {line['date'] if line['date'] else "-":<15} {line['category'] if line['category'] else "-":<15}  {line['description'] if line['description'] else "-"}")
            print("-" * 80)
    
    
    @staticmethod
    def total_summary(database, args):
        total_spends = 0
        for expense in database:
            if args.category is not None:
                if expense['category'] == args.category:
                    total_spends += expense['amount']
            else: 
                    total_spends += expense['amount']
        print(f"Total expenses:{total_spends}")

    def year_summary(database, args):
        total_sepnds = 0
        print(type(args.year))
        for expenses in database:
            year_datetime_type = datetime.strptime(expenses['date'], "%d/%m/%Y")
            if year_datetime_type == args.year:
                print(True)

    @staticmethod
    def filter(database, args):
        total_spends = 0
        new_list = deepcopy(database)
        for expenses in new_list:
            if args.category is not None:
                if expenses.get("category") == args.category:
                    expenses["Marker"] = True
        
        
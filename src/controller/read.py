from datetime import datetime
from controller.json_operations import JsonOperations
from controller.validation import Validation


class Read:
    
    @classmethod
    def list(cls, database):
        if not database:
            print("\n# No expenses recorded yet.")
        else:
            print("-" * 80)
            print(f"{'ID':<5} {'AMOUNT':<15} {'DATE':<15} {'CATEGORY':<15} {'DESCRIPTION'}")
            print("-" * 80)
            for line in database:
                print(f"{line['id']:<5} {line['amount']:<15.2f} {line['date'] if line['date'] else "-":<15} {line['category'] if line['category'] else "-":<15}  {line['description'] if line['description'] else "-"}")
            print("-" * 80)


    @classmethod
    def list_flow(cls, database, args):
        datas = []
        amount = quantity = 0

        datas, amount, quantity = cls.filter(database, args)
       
        Read.list(datas)

        if args.summary is not None:
            print(f"Results: {quantity} | Total amount: {amount}")
        
            
    
    @classmethod 
    def filter(cls, database, args):
        datas = []
        amount = quantity = 0

        for expense in database:
            date = Validation.str_to_date(expense["date"])

            if args.id is not None:
                if expense['id'] not in list(args.id):
                    continue


            if args.year is not None:
                if date.year not in list(args.year):
                    continue
            
            if args.month is not None:
                if date.month not in list(args.month):
                    continue
            
            if args.category is not None:
                if args.category != expense['category']:
                    continue
            
            if args.less is not None:
                if args.less <= expense['amount']:
                    continue
            
            if args.greater is not None:
                if args.greater >= expense['amount']:
                    continue
                      
            if args.amount is not None:
                if args.amount != expense['amount']:
                    continue
        
            amount += expense["amount"] 
            quantity += 1

            datas.append(expense)
        return datas, amount, quantity



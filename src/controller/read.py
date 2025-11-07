from datetime import datetime
from controller.json_operations import JsonOperations
from controller.validation import Validation
import csv

class Read:
    
    @staticmethod
    def list(database):
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
    def filter(cls, database, args):
        datas = []
        amount = quantity = 0

        for expense in database:
            date = Validation.str_to_date(expense["date"])


            if args.year is not None:
                if args.year != date.year:
                    continue
            
            if args.month is not None:
                if args.month != date.month:
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
       
        Read.list(datas)

        if args.summary is not None:
            print(f"Results: {quantity} | Total amount: {amount}")
        
        if args.export is not None:
            cls.export(datas) 

    @classmethod
    def export(cls, database):
        JsonOperations.EXPORT_PATH.touch(exist_ok=True)
        with open(JsonOperations.EXPORT_PATH, "w+", encoding="UTF-8", newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(["ID", "AMOUNT", "DATE", "CATEGORY", "DESCRIPTION"])
            for line in database:
                csv_writer.writerow([line["id"] if line['id'] else '-', line["amount"] if line['amount'] else '-', line["date"] if line['date'] else '-', line["category"] if line["category"] else '-', line["description"] if line["description"] else '-'])     

    @classmethod
    def alt(cls):
        # create the folder (if exist ok, create parents)
        # filtrar dados para exportar
        # Tirar a possibilidade de exportar da função LIST e adicionar a função de listar a função própria de exportação
        # dessa forma podemos ampliar as possibilidades da função de exportar -- exportar com filtros, exportar em CSV e PDF, exportar pro caminho desejado e criado quando não houver
        ...

    @classmethod 
    def real_filter(cls, database, args):
        datas = []
        amount = quantity = 0

        for expense in database:
            date = Validation.str_to_date(expense["date"])


            if args.year is not None:
                if args.year != date.year:
                    continue
            
            if args.month is not None:
                if args.month != date.month:
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

            return datas, quantity, amount


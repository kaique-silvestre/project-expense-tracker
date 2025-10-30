from datetime import datetime
from copy import deepcopy
import csv
import pathlib

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
        datas = []

        for expense in database:
            path = pathlib.Path("C:\\Users\\Imuvi\\Documents\\kaique\\scripts\\expense-tracker\\teste.csv")
            date = datetime.strptime(expense['date'], '%d/%m/%Y')


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

        if args.export is not None and args.export is True:

            

            with open(path, "a+", encoding='utf8') as file:
                csv_writer = csv.DictWriter(file, fieldnames=database[0].keys())
                if not path.exists():
                    csv_writer.writerow(["id", "valor", "categoria", "data", "descricao"])
                
                
                    csv_writer.writerows(database)



            datas.append(expense)
        



        Read.list(datas)

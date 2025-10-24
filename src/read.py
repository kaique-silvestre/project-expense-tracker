from datetime import datetime

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
    def summary(file_path, database, args):
        total_spends = 0
        if not database:
            print("# Nenhum gasto registrado ainda.")
        else:
            if args.month is not None:
                for item in database:
                    date = datetime.strptime(item['date'], '%d/%m/%Y')
                    if date.month == args.month:
                        total_spends += item['amount']
                print(f"\n# Total expenses of {args.month} month: ${total_spends}")      
            else:
                for item in database:
                    total_spends += item['amount'] if item['amount'] != None else 0
                print(f"\n# Total expenses: ${total_spends}\n")
                    
        

                


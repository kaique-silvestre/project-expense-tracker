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
    def summary(database, args):
        total_spends = 0
        if args.month is not None:
            for item in database:
                if item['date'] is not None:
                    date = datetime.strptime(item['date'], '%d/%m/%Y')
                    if date.month == args.month:
                        total_spends += item['amount']
                    else:
                        continue
        elif args.category is not None:
            for item in database:
                if item['category'] == args.category:
                    total_spends += item['amount']
        else:
            for item in database:
                total_spends += item['amount'] if item['amount'] != None else 0
        print(f"\n# Total expenses: ${total_spends}\n")

    @staticmethod
    def teste(args):
        if args.category is not None and args.month is not None:
            ...
        elif args.category is not None:
            ...
        

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
    def filter(database, args):
        datas = []

        for expense in database:
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
            datas.append(expense)
        Read.list(datas)

class Read:
    @staticmethod
    def list(database):
        if not database:
            print("# Nenhum gasto registrado ainda.")
        else:
            for line in database:
                print("-" * 80)
                print(f"{'ID':<5} {'AMOUNT':<15} {'DATE':<15} {'CATEGORY':<15} {'DESCRIPTION'}")
                print("-" * 80)
                for line in database:
                    print(f"{line['id']:<5} {line['amount']:<15.2f} {line['date'] if line['date'] else "-":<15} {line['category'] if line['category'] else "-":<15}  {line['description'] if line['description'] else "-"}")
                print("-" * 80)
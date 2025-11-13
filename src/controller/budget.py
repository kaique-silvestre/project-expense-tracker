from controller.json_operations import JsonOperations
from datetime import datetime


class Budget:
    # Arrumar o set -- menos validações agressivas -- Melhor lógica
    @classmethod
    def set_budget(cls, budget_database, args):
        budget_database[0][str(int(args.month))] = int(args.value)
        JsonOperations.send_json(JsonOperations.BUDGET_FILE, budget_database)
        print("\n# Successfully set.\n")

    
    @classmethod
    def delete_budget(cls, budget_database, args):
        for item in args.month:
            budget_database[0][str(item)] = None
        JsonOperations.send_json(JsonOperations.BUDGET_FILE, budget_database)
        print("\n# Successfully deleted.\n")
    
    @classmethod
    def list_budget(cls, database_budget, args):
        print("=== Budget List ===")
        if args.month is None:
            for month, value in database_budget[0].items():
                print(f"Month: {month} | Budget: {value if value is not None else '-'}") # inline validation of the value
        else:
            for month, value in database_budget[0].items():
                if int(month) in args.month:
                    print(f"Month: {month} | Budget: {value if value is not None else '-'}") # inline validation of the value

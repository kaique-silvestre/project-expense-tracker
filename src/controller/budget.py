from controller.json_operations import JsonOperations
from datetime import datetime

class Budget:

    @classmethod
    def budget_set(cls, budget_database, args):
        budget_database[0][str(args.month)] = int(args.value)
        JsonOperations.send_json(JsonOperations.BUDGET_FILE, budget_database)
    
    @classmethod
    def budget_remove(cls, budget_database, args):
        for item in args.month:
            budget_database[0][str(item)] = None
        JsonOperations.send_json(JsonOperations.BUDGET_FILE, budget_database)
    
    @classmethod
    def budget_list(cls, database_budget, args):
        if args.month is None:
            for line in database_budget[0].items():
                print(line[0], line[1]) # Fazer texto
        else:
            for mes, valor in database_budget[0].items():
                if int(mes) in args.month:
                    print(mes, valor) # Fazer texto

    @classmethod
    def return_budget(cls, budget_file, args):
        date = datetime.strptime(args.date, '%d/%m/%Y')
        print(date, type(date))


import pathlib
import csv
from controller.read import Read

class Export:
    @classmethod
    def csv_export_flow(cls, database, args):
        if args.folder is not None:
            folder_path = pathlib.Path(args.folder)
        else:
            folder_path = pathlib.Path.home() / "Desktop"

        csv_var = ".csv"

        file_str = args.file + csv_var
        file_name = pathlib.Path(file_str)
        complete_path = folder_path / file_name
        print(f"\n# CSV file was exproted to: {complete_path}\n")

        data, var1, var2 = Read.filter(database, args)
        cls.export(data, complete_path)

    @classmethod
    # Tirar o "-" dos daods que obrigatóriamente existem na base de dados
    # ID, AMOUNT, DATE
    def export(cls, database, path):
        with open(path, "w+", encoding="utf8", newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(["ID", "AMOUNT", "DATE", "CATEGORY", "DESCRIPTION"])
            for line in database:
                csv_writer.writerow([line["id"], line["amount"], line["date"], line["category"] if line["category"] else '-', line["description"] if line["description"] else '-'])     



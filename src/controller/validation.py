from datetime import datetime


class Validation:

    def date_validation():...

    @classmethod
    def date_to_str(cls, date, date_format="%d/%m/%Y"):
        date = datetime.strftime(date, date_format)
        return date

    @classmethod
    def str_to_date(cls, string, date_format="%d/%m/%Y"):
        date = datetime.strptime(string, date_format).date()
        return date

if __name__ == "__main__":
    date = Validation.str_to_date("31/10/2025")
    print(date)
    date = Validation.date_to_str(date)
    print(date)
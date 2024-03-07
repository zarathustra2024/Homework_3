from datetime import datetime


def get_days_from_today(date):
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.today()
        delta = today - date_obj
        return delta.days
    except ValueError:
        return "Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'."


date = input("Введіть дату у форматі 'РРРР-ММ-ДД': ")
print(get_days_from_today(date))

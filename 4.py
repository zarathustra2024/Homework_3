from datetime import datetime, timedelta


def get_next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return d + timedelta(days=days_ahead)


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        try:
            birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
            birthday_this_year = birthday.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(
                    year=today.year + 1)

            days_until_birthday = (birthday_this_year - today).days
            if days_until_birthday <= 7:
                if birthday_this_year.weekday() >= 5:
                    next_weekday = get_next_weekday(birthday_this_year, 0)
                    congratulation_date_str = next_weekday.strftime('%Y.%m.%d')
                else:
                    congratulation_date_str = birthday_this_year.strftime(
                        '%Y.%m.%d')

                upcoming_birthdays.append(
                    {"name": user["name"], "congratulation_date": congratulation_date_str})
        except ValueError:
            print(f'Некоректна дата народження для користувача {user["name"]}')

    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.03.09"},
    {"name": "Jane Smith1", "birthday": "1990.03.08"},
    {"name": "Jane Smith2", "birthday": "1990.03.16"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

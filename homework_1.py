from datetime import datetime # імпорт класу datetime із модулю datetime

def get_days_from_today(date):
    # перевірка правильності вводу даних
    try:
        new_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today()
        # обраховування кількості днів
        number_of_days = today.toordinal() - new_date.toordinal()
        return number_of_days
    # обробка виключення
    except ValueError:
        return "Incorrect date input"
    

print(get_days_from_today("23"))
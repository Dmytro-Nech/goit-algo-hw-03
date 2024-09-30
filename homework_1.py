from datetime import datetime # імпорт класу datetime із модулю datetime

def get_days_from_today(date):
    # перевірка правильності вводу даних
    try:
        new_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today()
        # обраховування кількості днів
        number_of_days =  new_date.toordinal() - today.toordinal()
        return number_of_days
    # обробка виключення
    except ValueError:
        return "Incorrect date input"
    
# перевіряємо
if __name__ == "__main__":
    print(get_days_from_today("2024-11-22"))
    print(get_days_from_today("2023-11-22"))
    print(get_days_from_today("2024/11-22"))
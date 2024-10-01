# імпортуємо модуль re
import re 
# створюємо функцію
def normalize_phone(phone_number):
    # паттерн який видаляє усе окрім цифр
    pattern =r"[^0-9]"
    replacement = ""  
    # чистимо номер від зайвого
    new_number = re.sub(pattern, replacement, phone_number)
    # перевіріємо чи номер починається із 38
    if new_number[:2] != "38":
        new_number = "38" + new_number
    return "+" + new_number
        
# перевіряємо функцію
if __name__ == "__main__":
    raw_numbers = [
        "067\\t123 4567",
        "(095) 234-5678\\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]
    for number in raw_numbers:
        print(normalize_phone(number))
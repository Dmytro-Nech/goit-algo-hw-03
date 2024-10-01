# імпортуємо модуль random
import random
# створюємо функцію
def get_numbers_ticket(min, max, quantity):
# створюємо порожній список
    tickets_list = []
# перевіряємо відповідність умовам
    if min >= max or quantity > (max - min) or min < 1 or max > 1000:
        return tickets_list
# генеруємо список відповідно до передананих аргументів
    tickets_list = [el for el in range(min, max+1)]
# вибараємо задану кількість випадкових чисел
    chosen_tickets = random.sample(tickets_list, quantity) 
# повертаємо відсортований список випадкових чисел
    return sorted(chosen_tickets)

# перевіряємо функцію
if __name__ == "__main__":
    print(get_numbers_ticket(1, 100, 4))
    print(get_numbers_ticket(0, 100, 3))
    print(get_numbers_ticket(1, 1001, 2))
    print(get_numbers_ticket(10, 4, 4))
    print(get_numbers_ticket(10, 14, 6))

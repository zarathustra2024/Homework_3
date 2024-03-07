import random


def get_numbers_ticket(min, max, quantity):
    if min >= 1 and max <= 1000:
        return random.sample(range(min, max), quantity)


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

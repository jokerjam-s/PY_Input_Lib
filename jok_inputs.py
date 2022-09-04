# Методы ввода значений с консоли
#
#


# получить целое число с консоли
#   message - сообщение для пользователя
def input_int(message: str) -> int:
    return int(input(message))


# получить вещественное число с консоли
#   message - сообщение для пользователя
def input_float(message: str) -> float:
    return float(input(message))


# получить строковое значениеи с консоли
#   message - сообщение для пользователя
def input_str(message: str) -> str:
    return input(message)


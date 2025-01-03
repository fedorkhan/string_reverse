def reverse_string(initial_string: str) -> str:
    """
    Функция, возвращающая строку в обратном порядке
    :param initial_string: str
    :return: str
    """

    reversed_string = initial_string[::-1]

    return reversed_string


if __name__ == "__main__":
    print(reverse_string("asdfgh"))

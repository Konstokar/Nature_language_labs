from collections import Counter


def read_text():
    """
    Считывает текст из консоли и одновременно подсчитывает буквы.

    Ввод осуществляется построчно.
    Для завершения ввода пользователь вводит команду /end.

    Весь текст целиком в памяти не хранится.
    Каждая строка сразу обрабатывается и после этого больше не нужна.
    """

    counter = Counter()

    print("\nВведите текст.")
    print("Для завершения ввода введите /end на отдельной строке.\n")

    while True:
        line = input()

        if line == "/end":
            break

        line = line.lower()

        for char in line:

            if char.isalpha():

                counter[char] += 1

    return counter


def print_statistics(counter):
    """
    Выводит частоту каждой найденной буквы.

    Параметр counter содержит результаты подсчёта.
    """

    if not counter:

        print("\nТекст не содержит букв.")

        return

    total = sum(counter.values())

    print("\nЧастота букв:")
    print("-" * 35)

    for letter, count in sorted(counter.items()):
        percentage = count / total * 100
        print(f"{letter}: {count:5d} ({percentage:6.2f}%)")

    print("-" * 35)
    print(f"Всего букв: {total}")


def print_histogram(counter):
    """
    Выводит вертикальную гистограмму частоты букв.
    """

    if not counter:
        return

    max_count = max(counter.values())
    max_height = 20

    heights = {}

    for letter, count in counter.items():
        heights[letter] = round(
            count / max_count * max_height
        )

    print("\nВертикальная гистограмма:\n")

    for level in range(max_height, 0, -1):
        for letter in sorted(counter):
            if heights[letter] >= level:
                print("  █  ", end="")
            else:
                print("     ", end="")
        print()
    print("  " + "─────" * len(counter))
    for letter in sorted(counter):
        print(f"  {letter}  ", end="")

    print()


def run():
    """
    Главная функция лабораторной работы №1.

    Именно эту функцию вызывает main.py.
    """

    print("\n" + "=" * 40)
    print("ЛАБОРАТОРНАЯ РАБОТА №1")
    print("Подсчёт частоты букв")
    print("=" * 40)
    counter = read_text()
    print_statistics(counter)
    print_histogram(counter)
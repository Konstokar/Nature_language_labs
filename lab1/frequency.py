from collections import Counter


def read_text(filename):
    """Читает текст из файла."""
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def count_letters(text):
    """Подсчитывает частоту каждой буквы."""
    letters = []

    for char in text.lower():
        if char.isalpha():
            letters.append(char)

    return Counter(letters)


def print_statistics(counter):
    """Выводит статистику частоты букв."""

    total = sum(counter.values())

    print("\nЧастота букв:")
    print("-" * 35)

    for letter, count in sorted(counter.items()):
        percentage = count / total * 100
        print(f"{letter}: {count:5d} ({percentage:6.2f}%)")

    print("-" * 35)
    print(f"Всего букв: {total}")


def print_histogram(counter):
    """Выводит вертикальную гистограмму."""

    if not counter:
        print("Текст не содержит букв.")
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

    print("\n" + "=" * 40)
    print("ЛАБОРАТОРНАЯ РАБОТА №1")
    print("Подсчёт частоты букв")
    print("=" * 40)

    filename = "data/text.txt"

    text = read_text(filename)

    counter = count_letters(text)

    print_statistics(counter)
    print_histogram(counter)
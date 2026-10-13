import re
from collections import Counter, defaultdict
from nltk.stem import SnowballStemmer


RUSSIAN_STEMMER = SnowballStemmer("russian")
ENGLISH_STEMMER = SnowballStemmer("english")


WORD_PATTERN = re.compile(r"[a-zа-яё]+", re.IGNORECASE)


def read_and_count_words():
    """
    Считывает текст построчно и группирует слова по основам.

    Возвращает словарь следующего вида:
    {
        "основа": Counter({"исходное_слово": количество})
    }

    Исходный текст целиком в памяти не хранится.
    """
    word_groups = defaultdict(Counter)

    print("\nВведите текст на русском и/или английском языке.")
    print("Для завершения ввода введите /end на отдельной строке.\n")

    while True:
        try:
            line = input()

        except EOFError:
            break

        if line.strip() == "/end":
            break

        words = WORD_PATTERN.findall(line.lower())

        for word in words:


            if re.fullmatch(r"[а-яё]+", word):
                stem = RUSSIAN_STEMMER.stem(word)
            else:
                stem = ENGLISH_STEMMER.stem(word)

            word_groups[stem][word] += 1

    return dict(word_groups)


def print_statistics(word_groups):
    """Выводит частоты основ и исходных слов."""

    if not word_groups:
        print("\nТекст не содержит слов.")
        return

    total_words = sum(
        sum(words.values())
        for words in word_groups.values()
    )

    print("\nЧастоты слов, сгруппированных по основам:")
    print("=" * 65)

    sorted_groups = sorted(
        word_groups.items(),
        key=lambda item: (-sum(item[1].values()), item[0])
    )

    for stem, words in sorted_groups:
        frequency = sum(words.values())

        percentage = frequency / total_words * 100

        variants = ", ".join(
            f"{word} ({count})"
            for word, count in sorted(
                words.items(),
                key=lambda item: (-item[1], item[0])
            )
        )

        print(
            f"Основа: {stem:<15} "
            f"Частота: {frequency:5d} "
            f"({percentage:6.2f}%)"
        )
        print(f"  Слова: {variants}")

    print("=" * 65)
    print(f"Всего слов: {total_words}")
    print(f"Уникальных основ: {len(word_groups)}")


def print_histogram(word_groups):
    """Строит горизонтальную гистограмму частот основ."""

    if not word_groups:
        return

    frequencies = {
        stem: sum(words.values())
        for stem, words in word_groups.items()
    }

    top_groups = sorted(
        frequencies.items(),
        key=lambda item: (-item[1], item[0])
    )[:20]

    max_frequency = top_groups[0][1]

    max_bar_width = 40

    print("\nГоризонтальная гистограмма частот основ:")
    print("(показаны до 20 наиболее частых основ)\n")

    for stem, frequency in top_groups:

        bar_width = round(
            frequency / max_frequency * max_bar_width
        )

        bar = "█" * bar_width

        print(f"{stem:<15} | {bar} {frequency}")


def run():
    """Точка запуска лабораторной работы №2."""

    print("\n" + "=" * 40)
    print("ЛАБОРАТОРНАЯ РАБОТА №2")
    print("Частота слов по основам")
    print("=" * 40)

    word_groups = read_and_count_words()

    print_statistics(word_groups)

    print_histogram(word_groups)

import re
from collections import Counter
from nltk.stem import PorterStemmer


STEMMER = PorterStemmer(
    mode=PorterStemmer.ORIGINAL_ALGORITHM
)


WORD_PATTERN = re.compile(r"[a-zA-Z]+")


def read_text():
    """
    Считывает текст из консоли построчно.

    Ввод завершается, если пользователь вводит /end
    на отдельной строке.

    Возвращает список строк. Хранение текста целиком позволяет
    затем показать результаты обработки всех слов.
    """

    print("\nВведите английский текст.")
    print("Для завершения ввода напишите /end на отдельной строке.\n")

    lines = []

    while True:
        try:
            line = input()

        except EOFError:
            break

        if line.strip().lower() == "/end":
            break

        lines.append(line)

    return "\n".join(lines)


def extract_words(text):
    """
    Выделяет английские слова из текста.

    Пунктуация, цифры и символы других алфавитов не считаются
    английскими словами и не передаются стемматизатору.

    Возвращает список найденных слов в нижнем регистре.
    """

    words = WORD_PATTERN.findall(text.lower())

    return words


def stem_words(words):
    """
    Применяет алгоритм Портера к каждому слову.

    Возвращает список пар:
        (исходное слово, полученная основа).

    Например:
        ("studies", "studi")
        ("studying", "studi")

    Основа, полученная стемматизацией, не обязательно является
    самостоятельным словом английского языка.
    """

    results = []

    for word in words:

        stem = STEMMER.stem(word)

        results.append((word, stem))

    return results


def print_results(results):
    """
    Выводит пары "исходное слово — основа" и общую статистику.
    """

    if not results:
        print("\nВ тексте не найдено английских слов.")
        return

    print("\nРезультаты стемматизации:")
    print("=" * 55)

    print(f"{'Исходное слово':<25} | {'Основа':<20}")
    print("-" * 55)

    for word, stem in results:
        print(f"{word:<25} | {stem:<20}")

    print("=" * 55)

    stem_frequencies = Counter(
        stem for word, stem in results
    )

    total_words = len(results)

    unique_words = len(set(word for word, stem in results))

    unique_stems = len(stem_frequencies)

    print(f"\nВсего обработано слов: {total_words}")
    print(f"Уникальных исходных слов: {unique_words}")
    print(f"Уникальных основ: {unique_stems}")

    print("\nЧастоты полученных основ:")

    for stem, count in sorted(
        stem_frequencies.items(),
        key=lambda item: (-item[1], item[0])
    ):
        print(f"{stem:<20} — {count}")


def run():
    print("\n" + "=" * 50)
    print("ЛАБОРАТОРНАЯ РАБОТА № 4")
    print("Алгоритм выделения основы слова Портера")
    print("=" * 50)

    text = read_text()

    words = extract_words(text)

    results = stem_words(words)

    print_results(results)

import math


WORD_PROBABILITIES = {
    "мама": 0.08,
    "мам": 0.01,
    "а": 0.03,
    "мы": 0.05,
    "мыла": 0.04,
    "мыл": 0.01,
    "ыла": 0.005,
    "раму": 0.02,
    "рама": 0.03,
    "ра": 0.005,
    "му": 0.01,
    "ру": 0.005,
    "ам": 0.01,
    "ла": 0.01,
}


def validate_dictionary(word_probabilities):


    for word, probability in word_probabilities.items():

        if not isinstance(word, str) or not word:
            raise ValueError(
                "Словарь содержит пустое или некорректное слово."
            )

        if isinstance(probability, bool) or not isinstance(
            probability, (int, float)
        ):
            raise ValueError(
                f"Вероятность слова '{word}' должна быть числом."
            )

        if not math.isfinite(probability) or not (
            0 < probability <= 1
        ):
            raise ValueError(
                f"Некорректная вероятность слова '{word}': "
                f"{probability}. Допустим диапазон (0, 1]."
            )


def viterbi_segment(text, word_probabilities):
    """
    Разделяет строку на наиболее вероятную последовательность слов.

    Аргументы:
        text:
            Входная строка без пробелов.

        word_probabilities:
            Словарь, где ключ — слово, а значение — его вероятность.

    Возвращает:
        Кортеж из двух элементов:
        1. список найденных слов;
        2. вероятность полученного разбиения.

        Если разбиение не найдено, возвращает (None, 0.0).
    """

    text = text.lower()

    text = "".join(text.split())

    if not text:
        return None, 0.0

    validate_dictionary(word_probabilities)

    text_length = len(text)

    best_probability = [0.0] * (text_length + 1)
    best_probability[0] = 1.0

    previous_position = [None] * (text_length + 1)

    for end in range(1, text_length + 1):

        for start in range(end):

            if best_probability[start] == 0.0:
                continue

            candidate_word = text[start:end]

            word_probability = word_probabilities.get(
                candidate_word, 0.0
            )

            if word_probability == 0.0:
                continue

            candidate_probability = (
                best_probability[start] * word_probability
            )

            if candidate_probability > best_probability[end]:

                best_probability[end] = candidate_probability

                previous_position[end] = start

    if best_probability[text_length] == 0.0:
        return None, 0.0

    words = []

    position = text_length

    while position > 0:

        start = previous_position[position]

        if start is None:
            return None, 0.0

        words.append(text[start:position])

        position = start

    words.reverse()

    return words, best_probability[text_length]


def run():
    """
    Точка входа лабораторной работы.

    Вызывается из общего main.py, поэтому отдельный main()
    в этом модуле не нужен.
    """

    print("\n" + "=" * 50)
    print("ЛАБОРАТОРНАЯ РАБОТА № 3")
    print("Разделение потока на слова: алгоритм Витерби")
    print("=" * 50)

    print("\nВведите строку без пробелов.")
    print("Для выхода в меню введите /exit.\n")

    text = input("Входная строка: ").strip()

    if text.lower() == "/exit":
        print("Возврат в главное меню.")
        return

    try:
        words, probability = viterbi_segment(
            text,
            WORD_PROBABILITIES
        )

        if words is None:
            print("\nНе удалось полностью разделить строку.")
            print(
                "Возможно, в словаре отсутствуют необходимые слова."
            )
            return

        print("\nРезультат разделения:")
        print(" ".join(words))

        print(f"\nКоличество слов: {len(words)}")

        print(
            "Вероятность разбиения: "
            f"{probability:.12g}"
        )

    except ValueError as error:
        print(f"\nОшибка в словаре: {error}")

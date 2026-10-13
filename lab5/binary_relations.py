def parse_elements(input_text):
    """
    Преобразует строку с элементами в множество.

    Например:
        Ввод: a, b, c
        Результат: {"a", "b", "c"}

    Элементы разделяются запятыми.
    """

    elements = {
        item.strip()
        for item in input_text.split(",")
        if item.strip()
    }

    if not elements:
        raise ValueError("Множество должно содержать хотя бы один элемент.")

    return elements


def parse_relation(input_text, elements):
    """
    Преобразует строку с парами в бинарное отношение.

    Формат ввода:
        a,b; b,c; a,c

    Точка с запятой разделяет пары,
    запятая разделяет элементы внутри пары.

    Каждая пара должна состоять ровно из двух элементов,
    принадлежащих заданному множеству.
    """

    if not input_text.strip():
        return set()

    relation = set()

    for pair_text in input_text.split(";"):

        pair_text = pair_text.strip()

        if not pair_text:
            continue

        parts = [part.strip() for part in pair_text.split(",")]

        if len(parts) != 2 or not all(parts):
            raise ValueError(
                f"Некорректная пара: '{pair_text}'. "
                "Используйте формат a,b."
            )

        first, second = parts

        if first not in elements or second not in elements:
            raise ValueError(
                f"Пара ({first}, {second}) содержит элемент, "
                "которого нет в заданном множестве."
            )

        relation.add((first, second))

    return relation


def symmetric_closure(relation):
    """
    Вычисляет симметричное замыкание бинарного отношения.

    Для каждой пары (a, b) добавляет обратную пару (b, a).

    Исходное отношение не изменяется:
    создаётся его копия.
    """

    result = set(relation)

    for first, second in relation:
        result.add((second, first))

    return result


def reflexive_closure(relation, elements):
    """
    Вычисляет рефлексивное замыкание отношения
    относительно заданного множества элементов.

    Для каждого элемента a добавляет пару (a, a).
    """

    result = set(relation)

    for element in elements:
        result.add((element, element))

    return result


def transitive_closure(relation):
    """
    Вычисляет транзитивное замыкание бинарного отношения.

    Если существуют пары (a, b) и (b, c),
    в отношении должна присутствовать пара (a, c).

    Алгоритм повторяет добавление новых пар, пока отношение
    перестаёт изменяться. Это необходимо, поскольку добавленная
    пара может позволить получить новые транзитивные следствия.
    """

    result = set(relation)

    while True:

        new_pairs = set()

        for first, middle in result:
            for middle_next, last in result:

                if middle == middle_next:

                    candidate = (first, last)

                    if candidate not in result:
                        new_pairs.add(candidate)

        if not new_pairs:
            break

        result.update(new_pairs)

    return result


def is_symmetric(relation):
    """
    Проверяет симметричность отношения.

    Отношение симметрично, если для каждой пары (a, b)
    существует обратная пара (b, a).
    """

    return all(
        (second, first) in relation
        for first, second in relation
    )


def is_reflexive(relation, elements):
    """
    Проверяет рефлексивность отношения на заданном множестве.

    Для каждого элемента должна существовать пара (a, a).
    """

    return all(
        (element, element) in relation
        for element in elements
    )


def is_transitive(relation):
    """
    Проверяет транзитивность отношения.

    Для любых пар (a, b) и (b, c) должна существовать (a, c).
    """

    for first, middle in relation:
        for middle_next, last in relation:

            if middle == middle_next:
                if (first, last) not in relation:
                    return False

    return True


def format_relation(relation):
    """
    Подготавливает отношение к удобному выводу.

    Сортируем пары, чтобы результат не зависел
    от внутреннего порядка элементов в множестве set.
    """

    sorted_pairs = sorted(relation)

    if not sorted_pairs:
        return "∅"

    formatted_pairs = [
        f"({first}, {second})"
        for first, second in sorted_pairs
    ]

    return "{ " + ", ".join(formatted_pairs) + " }"


def print_relation_properties(relation, elements):
    """
    Выводит информацию о том, какими свойствами обладает отношение.
    """

    print("\nСвойства отношения:")

    print(
        "Симметричность: "
        + ("да" if is_symmetric(relation) else "нет")
    )

    print(
        "Рефлексивность: "
        + ("да" if is_reflexive(relation, elements) else "нет")
    )

    print(
        "Транзитивность: "
        + ("да" if is_transitive(relation) else "нет")
    )


def run():
    print("\n" + "=" * 55)
    print("ЛАБОРАТОРНАЯ РАБОТА № 5")
    print("Бинарные отношения и их замыкания")
    print("=" * 55)

    print("\nВведите элементы конечного множества через запятую.")
    print("Пример: a, b, c")

    try:
        elements = parse_elements(input("\nМножество A: "))

        print("\nВведите пары отношения через точку с запятой.")
        print("Формат: a,b; b,c")
        print("Чтобы задать пустое отношение, оставьте строку пустой.")

        relation = parse_relation(
            input("\nОтношение R: "),
            elements
        )

    except ValueError as error:
        print(f"\nОшибка ввода: {error}")
        return

    print("\nИсходные данные:")
    print(f"A = {format_relation({(x, x) for x in elements})}")
    print(f"R = {format_relation(relation)}")

    print_relation_properties(relation, elements)

    symmetric = symmetric_closure(relation)
    reflexive = reflexive_closure(relation, elements)
    transitive = transitive_closure(relation)

    print("\n" + "=" * 55)
    print("РЕЗУЛЬТАТЫ ВЫЧИСЛЕНИЯ ЗАМЫКАНИЙ")
    print("=" * 55)

    print("\n1. Симметричное замыкание:")
    print(format_relation(symmetric))

    print("\n2. Рефлексивное замыкание:")
    print(format_relation(reflexive))

    print("\n3. Транзитивное замыкание:")
    print(format_relation(transitive))

    print("\nПроверка свойств полученных отношений:")

    print("\nСимметричное замыкание:")
    print_relation_properties(symmetric, elements)

    print("\nРефлексивное замыкание:")
    print_relation_properties(reflexive, elements)

    print("\nТранзитивное замыкание:")
    print_relation_properties(transitive, elements)

    print("\nЛабораторная работа завершена.")

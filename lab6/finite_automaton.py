class FiniteAutomaton:

    def __init__(
        self,
        states,
        alphabet,
        transitions,
        start_state,
        accepting_states
    ):

        self.states = set(states)
        self.alphabet = set(alphabet)
        self.accepting_states = set(accepting_states)

        self.transitions = dict(transitions)

        self.start_state = start_state

        self._validate_definition()

    def _validate_definition(self):
        """
        Проверяет корректность определения автомата.

        Для полного ДКА:
        1. Множество состояний не должно быть пустым.
        2. Начальное состояние должно существовать.
        3. Принимающие состояния должны входить в множество состояний.
        4. Все переходы должны использовать допустимые состояния
           и символы алфавита.
        5. Для каждой пары (состояние, символ) должен быть задан
           ровно один переход.
        """

        if not self.states:
            raise ValueError(
                "Множество состояний автомата не может быть пустым."
            )

        if self.start_state not in self.states:
            raise ValueError(
                "Начальное состояние отсутствует "
                "в множестве состояний."
            )

        if not self.accepting_states.issubset(self.states):
            raise ValueError(
                "Принимающие состояния должны входить "
                "в множество состояний автомата."
            )

        for transition, next_state in self.transitions.items():

            if not isinstance(transition, tuple) or len(transition) != 2:
                raise ValueError(
                    "Переход должен задаваться парой "
                    "(состояние, входной символ)."
                )

            current_state, symbol = transition

            if current_state not in self.states:
                raise ValueError(
                    f"Неизвестное исходное состояние: {current_state}"
                )

            if symbol not in self.alphabet:
                raise ValueError(
                    f"Символ '{symbol}' отсутствует во входном алфавите."
                )

            if next_state not in self.states:
                raise ValueError(
                    f"Неизвестное следующее состояние: {next_state}"
                )

        for state in self.states:
            for symbol in self.alphabet:
                if (state, symbol) not in self.transitions:
                    raise ValueError(
                        f"Не задан переход из состояния '{state}' "
                        f"по символу '{symbol}'."
                    )

    def process(self, input_string):
        """
        Обрабатывает входную строку посимвольно.

        Возвращает:
            accepted:
                True, если конечное состояние принимающее,
                иначе False.

            path:
                Список состояний, через которые прошёл автомат.

        Если во входной строке встречается символ, не входящий
        в алфавит, строка отвергается.
        """

        current_state = self.start_state

        path = [current_state]

        for symbol in input_string:

            if symbol not in self.alphabet:
                return False, path

            current_state = self.transitions[
                (current_state, symbol)
            ]

            path.append(current_state)

        accepted = current_state in self.accepting_states

        return accepted, path

    def describe(self):
        """
        Выводит формальное описание автомата.
        """

        print("\nФормальное описание конечного автомата:")
        print(f"K  = {sorted(self.states)}")
        print(f"T  = {sorted(self.alphabet)}")
        print(f"k1 = {self.start_state}")
        print(f"F  = {sorted(self.accepting_states)}")

        print("\nФункция переходов:")

        sorted_transitions = sorted(
            self.transitions.items(),
            key=lambda item: (item[0][0], item[0][1])
        )

        for (state, symbol), next_state in sorted_transitions:
            print(
                f"t({state}, {symbol}) = {next_state}"
            )


def create_demo_automaton():
    """
    Создаёт демонстрационный автомат.

    Он принимает непустые строки из символов a и b,
    которые начинаются с a.

    Примеры принимаемых строк:
        a
        aa
        ab
        abb
        abab

    Примеры отвергаемых строк:
        b
        ba
        bb
        пустая строка

    Состояния:
        q0    — начальное состояние, символ a ещё не прочитан;
        q1    — строка начинается с a, строка принимается;
        q_dead — ловушка для строк, начинающихся с b.
    """

    states = {"q0", "q1", "q_dead"}

    alphabet = {"a", "b"}

    transitions = {
        ("q0", "a"): "q1",
        ("q0", "b"): "q_dead",

        ("q1", "a"): "q1",
        ("q1", "b"): "q1",

        ("q_dead", "a"): "q_dead",
        ("q_dead", "b"): "q_dead",
    }

    start_state = "q0"

    accepting_states = {"q1"}

    return FiniteAutomaton(
        states,
        alphabet,
        transitions,
        start_state,
        accepting_states
    )


def run():
    print("\n" + "=" * 55)
    print("ЛАБОРАТОРНАЯ РАБОТА № 6")
    print("Моделирование детерминированного конечного автомата")
    print("=" * 55)

    automaton = create_demo_automaton()

    automaton.describe()

    print("\nНазначение автомата:")
    print(
        "Принимает непустые строки из символов a и b, "
        "начинающиеся с a."
    )

    print("\nВведите строки для проверки.")
    print("Для завершения введите /exit.")

    while True:
        input_string = input("\nВходная строка: ")

        if input_string == "/exit":
            print("Возврат в главное меню.")
            break

        accepted, path = automaton.process(input_string)

        print("Путь по состояниям: " + " -> ".join(path))

        if accepted:
            print("Результат: строка ПРИНЯТА автоматом.")
        else:
            print("Результат: строка ОТВЕРГНУТА автоматом.")

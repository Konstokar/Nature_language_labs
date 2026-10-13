def print_menu():
    print("\n" + "=" * 40)
    print("ЛАБОРАТОРНЫЕ РАБОТЫ")
    print("=" * 40)
    print("1. Частота букв")
    print("2. Частота слов")
    print("3. Алгоритм Витерби")
    print("4. Алгоритм Портера")
    print("5. Бинарные отношения и замыкания")
    print("6. Конечный автомат")
    print("0. Выход")
    print("=" * 40)


def main():
    while True:
        print_menu()

        choice = input("Выберите лабораторную работу: ")

        if choice == "1":
            from lab1.frequency import run
            run()

        elif choice == "2":
            from lab2.word_frequency import run
            run()

        elif choice == "3":
            from lab3.viterbi import run
            run()

        elif choice == "4":
            from lab4.porter_stemmer import run
            run()

        elif choice == "5":
            from lab5.binary_relations import run
            run()

        elif choice == "6":
            from lab6.finite_automaton import run
            run()

        elif choice == "0":
            print("Программа завершена.")
            break

        else:
            print("Некорректный выбор.")


if __name__ == "__main__":
    main()
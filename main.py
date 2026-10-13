def print_menu():
    print("\n" + "=" * 40)
    print("ЛАБОРАТОРНЫЕ РАБОТЫ")
    print("=" * 40)
    print("1. Частота букв")
    print("2. Частота слов")
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

        elif choice == "0":
            print("Программа завершена.")
            break

        else:
            print("Некорректный выбор.")


if __name__ == "__main__":
    main()
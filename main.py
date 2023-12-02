from colorama import Fore, Style
import random
import time

# Функция для создания файла с результатами теста
def create_answer_file(answer, save_results):
    if save_results:
        file_path = 'test_results.txt'
        with open(file_path, 'a') as file:
            file.write(answer + '\n')
        return file_path

# Функция для проверки правильности ответа
def check_answer(correct_answer, user_answer):
    # Сравнение ответа пользователя с правильным ответом
    if user_answer == correct_answer:
        # Вывод сообщения о правильном ответе
        print(Fore.GREEN + "Правильный ответ!" + Style.RESET_ALL)
        return True
    else:
        # Вывод сообщения об ошибке
        print(Fore.RED + "Неправильный ответ!" + Style.RESET_ALL)
        return False

# Основная функция теста
def logic_test():
    # Создание файла с заранее заданным ответом перед началом теста
    pre_defined_answer_file_path = 'predefined_answer.txt'
    with open(pre_defined_answer_file_path, 'w') as file:
        file.write("1239")

    save_results = input("Хотите сохранить результаты в файл? (да/нет): ").lower() == 'да'

    # Вопросы теста
    questions = [
        ("Что у тебя написанно в txt файле?", "1239"),
        ("Сколько вышло частей Half Life (не считая эпизодов)?", "2"),
        ("Когда вышел пайтон? (просто напиши год)", "1991"),
        ("Когда вышел первый код программирования? (Shortcode)", "1949"),
        ("Как называется, самая популярная торговая площадка?", "Steam"),
        ("В каком году человек впервые высадился на Луну?", "1969"),
        ("Какой химический элемент имеет атомный номер 8?", "Кислород")
    ]

    # Перемешивание вопросов
    random.shuffle(questions)

    correct_answers = 0
    total_questions = len(questions)

    for question_text, correct_answer in questions:
        start_time = time.time()
        user_answer = input(question_text + " ")
        end_time = time.time()
        elapsed_time = end_time - start_time

        if elapsed_time > 10:
            print(Fore.YELLOW + "Время вышло!" + Style.RESET_ALL)
            continue

        # Искусственная задержка для имитации проверки ответа
        print(Fore.WHITE + "Погодика, дай-ка проверю...")
        time.sleep(0.5)

        # Особая логика для вопроса с чтением файла
        if question_text == "Что у тебя написанно в txt файле?":
            with open(pre_defined_answer_file_path, 'r') as file:
                if check_answer(file.read().strip(), user_answer):
                    correct_answers += 1
        elif check_answer(correct_answer, user_answer):
            correct_answers += 1

    # Вывод результатов теста
    result = f"Тест окончен! Правильных ответов: {correct_answers} из {total_questions}."
    print(result)

    if save_results:
        create_answer_file(result, save_results)

# Запуск теста
logic_test()

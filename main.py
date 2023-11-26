from colorama import Fore, Style
import os
import random
import time


def create_answer_file(answer):
    file_path = 'answer.txt'
    with open(file_path, 'w') as file:
        file.write(answer)
    return file_path


def check_answer(correct_answer, user_answer):
    time.sleep(1)
    if user_answer == correct_answer:
        print(Fore.GREEN + "Правильный ответ!" + Style.RESET_ALL)
        return True
    else:
        print(Fore.RED + "Неправильный ответ!" + Style.RESET_ALL)
        return False


def logic_test():
    print("Привет! Это мини тест на твою логику, пройдешь ли ты его?)")

    questions = [
        ("==============Что у тебя написанно в txt файле?==============", "1239"),
        ("==============Сколько вышло частей Half Life (не считая эпизодов)?==============", "2"),
        ("==============Когда вышел пайтон? (просто напиши год)==============", "1991"),
        ("==============Когда вышел первый код программирования? (Shortcode)==============", "1949"),
        ("==============Как называется, самая популярная торговая площадка?==============", "Steam")
    ]

    random.shuffle(questions)

    file_path = create_answer_file("1239")
    correct_answers = 0

    for question_text, correct_answer in questions:
        user_answer = input(question_text + " ")
        print("Погодика, дай-ка проверю...")
        if question_text == "==============Что у тебя написанно в txt файле?==============":
            with open(file_path, 'r') as file:
                if check_answer(file.read().strip(), user_answer):
                    correct_answers += 1
                else:
                    break
        elif check_answer(correct_answer, user_answer):
            correct_answers += 1
        else:
            break

    print(f"Тест окончен! Правильных ответов: {correct_answers} из {len(questions)}.")

logic_test()

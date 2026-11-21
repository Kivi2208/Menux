import time
import requests
import random
import os
import colorama
import datetime

# MenuxKey = "MenuxKey-2026-09-original-key-Menux-XD7DX7DX-Login"
MenuxVersion = "Menux Version 1.0.1"
# MenuxKeyBypass = "Bypass7X"

# user_key = input("Введите ключ для входа в систему: ")

# if user_key == MenuxKey or user_key == MenuxKeyBypass:
if "KeyMenux.exe" in os.popen("tasklist").read():
    print("Открыть Систему Menux?")
    print("")
else:
    print("Не Лицензионая версия!")
    exit()

colorama.init(autoreset=True) 

print("(y/n)")

osv = input("")

if osv == "y":

    print("Вход в Систему Menux Выполнен Успешно")

else:
    print("Выход из программы")
    exit()

#FeedBackAntiSpamCount = 0

while True:
    print("Хотите ли вы перейти в режим...")

    print("")

    print("Удаленый контент (0)")
    print("Калькулятор (1)")
    print("Спам Текстом (2)")
    print("Легкая Dos Атака (3)")
    print("Выйти Из Menux (4)")
    print("Рандомные Числа (5)")
    print("Инструкция (6)")
    #print("Обратная Связь (7)")
    print("Правда или Ложь (7)")
    print("Четное или Нечетное (8)")
    print("Генератор Никнеймов (9)")
    print("Заметки (10)")
    print("Создание Псевдо Личности (11)")
    print("Посчитай до N (12)")
    print("Больше Меньше? (13)")
    print("Посчитать сколько дней прошло с даты (14)")

    print("")

    vm = input("")

    if vm == "0":
        print("")

        CutContent = ["Обратная Связь (7)", ]

        print("Вот весь удаленный контент:")
        print(CutContent)

    elif vm == "1":

        print("")

        print("Режим Калькулятора Активирован, напишите два числа в две строчки")

        print("")

        try:
            n1 = int(input("Введи первое число: "))
            n2 = int(input("Введи второе число: "))
        except ValueError:
            print("Ошибка! Введи корректные числа!")
            continue

        print("")

        print("Что сделать?")

        print("")

        print("Умножить (1)")
        print("Добавить (2)")
        print("Отнять (3)")
        print("Разделить (4)")

        print("")

        vkm = input("")

        print("Готово Результат сравнения:")

        if vkm == "1":

            rn = n1 * n2

            print("Получилось:", rn)

        elif vkm == "2":
            rn = n1 + n2

            print("Получилось:", rn)

        elif vkm == "3":
            rn = n1 - n2

            print("Получилось:", rn)

        elif vkm == "4":
            if n2 == 0:
                print("Ошибка! На ноль делить нельзя!")
            else:
                rn = n1 / n2
                print("Получилось:", rn)

    elif vm == "2":

        print("Пожалуйста напишите что спамить")

        print("")

        spamtext = input("")

        print("")

        print("Сколько Раз Спамить?")  

        print("")  

        try:
            spamcount = int(input(""))
        except ValueError:
            print("Ошибка! Введи корректное число!")
            continue

        print("")

        for i in range(spamcount):
            print(spamtext)


    elif vm == "3":

        print("")

        EasyDosAttackURL = input("Пожалуйста Напишите ссылку на сайт: ")

        print("")

        print("Начинаю Easy Dos")

        while True:
            r = requests.get(EasyDosAttackURL)
            print("Статус/Пинг Сайта:", r.status_code)

    elif vm == "4":
        
        print("Выход из программы")
        time.sleep(0.3)
        exit()

    elif vm == "5":

        print("")

        try:
            rnicount = int(input("Сколько вам нужно рандомных чисел?: "))
        except ValueError:
            print("Ошибка! Введи корректное число!")
            continue

        for i in range(rnicount):
            rni1 = random.randint(1, 1000)
            rni2 = random.randint(1, 1000)
            rn3 = random.randint(1, 1000)

            mrni = random.randint(1, 3)
            
            if mrni == 1:
                print(rni1)
            elif mrni == 2:
                print(rni2)
            elif mrni == 3:
                print(rn3)
    
    elif vm == "6":

        print("")
        print("Инструкция по использованию программы:")
        print("1. Калькулятор - позволяет выполнять базовые арифметические операции с двумя числами.")
        print("2. Спам Текстом - позволяет отправлять заданный текст указанное количество раз.")
        print("3. Легкая Dos Атака - позволяет отправлять запросы на указанный URL для тестирования нагрузки (используйте с осторожностью).")
        print("4. Выйти Из Menux - завершает выполнение программы.")
        print("5. Рандомные Числа - генерирует указанное количество случайных чисел в диапазоне от 1 до 1000.")
        print("6. Инструкция - выводит инструкцию по использованию программы.")
        #print("7. Обратная Связь - позволяет отправлять сообщения обратной связи через Telegram (лимит 5 сообщений).")
        print("7. Правда или Ложь - позволяет Узнать правду или ложь (Рандом).")
        print("8. Четное или Нечетное - позволяет Узнать Четное или Нечетное.")
        print("9. Генератор Никнеймов - позволяет генерировать никнеймы на основе введенной начальной части.")
        print("10. Заметки - позволяет создавать и сохранять заметки в файл NotesSaves.json.")
        print("11. Создание Псевдо Личности - позволяет генерировать случайные данные для псевдо личности, включая имя, фамилию, возраст, профессию и пол.")
        print("12. Посчитай до N - позволяет посчитать от 1 до указанного числа N с возможностью выбора цвета текста (красный, зеленый, синий).")
        print("13. Больше Меньше - позволяет установить диапозон рандома и с помощью игры больше меньше узнать рандомное число.")
        print("14. Посчитать сколько дней прошло с даты - позволяет ввести год, месяц и день, и узнать, сколько дней прошло с этой даты до сегодняшнего дня.")

        print("Другая информация:")

        print("")

        print("Версия программы:", MenuxVersion)
        print("Автор программы: Pechen1ko")
        # print("Ключ для входа в систему:", MenuxKey)
        # print("Ключ для обхода:", MenuxKeyBypass)


    elif vm == "7":

        print("")

        print("Задайте Вопрос")

        print("")

        input("")

        print("")

        random_answer = random.choice(["Правда", "Ложь"])

        print("Ответ:", random_answer)

    elif vm == "8":
        print("")

        try:
            number = int(input("Введите число: "))
        except ValueError:
            print("Ошибка! Введи корректное число!")
            continue

        if number % 2 == 0:
            print("Чётное")
        else:
            print("Нечётное")

    elif vm == "9":
        print("")

        StartNick = input("Введите начальную часть никнейма: ")

        MenuxBaseNick = ["_XD", "_Pro", "_Gamer", "_Master", "_Legend", "_King", "_Queen", "_Ninja", "_Shadow", "_Dragon", "_Wolf", "_Tiger", "_Eagle", "_Phoenix", "_Knight", "_Wizard", "_Assassin", "_Samurai", "_Viking", "_Pirate", "_Rogue", "_Hunter", "_Sniper", "_Soldier", "_Captain", "_Commander", "_General", "_Admiral", "_Marshal", "_Chief", "_Leader", "_Boss", "_Hero", "_Champion", "_Warrior", "_Gladiator", "_Spartan", "_Vigilante", "_ЛохТупой"]

        print("")

        randomtwopart = random.choice(MenuxBaseNick)

        print("Ваш Никнейм:", StartNick + randomtwopart)

    elif vm == "10":
        print("")

        print("Чтобы выйти из режима заметок введите 'Стоп'.")
        print("Чтобы очистить заметки напишите 'Очистить'.")

        print("")

        notes = []

        while True:
            note = input("Введите слово для заметки: ")

            if note.lower() == "стоп":
                try:
                    with open("NotesSaves.json") as f:
                        for line in f:
                            notes.append(line.strip())
                            print("Сохраненные заметки:", line.strip())
                except Exception as e:
                    print(f"Ошибка при чтении заметок: {e}")
                break

            elif note.lower() == "очистить":
                notes.clear()
                try:
                    with open("NotesSaves.json", "w"):
                        pass
                    print("Заметки очищены.")
                except Exception as e:
                    print(f"Ошибка при очистке заметок: {e}")
                continue

            print("Слово добавлено в заметки.")
            try:
                with open("NotesSaves.json", "a") as f:
                    f.write(note + "\n")
            except Exception as e:
                print(f"Ошибка при сохранении заметки: {e}")

    elif vm == "11":
        print("")

        print("Создание Псевдо Личности")

        print("")

        psname = ["Петя", "Вася", "Коля", "Саша", "Маша", "Даша", "Катя", "Лена", "Ира", "Оля", "Света", "Таня", "Женя", "Аня", "Наташа", "Юля", "Вика", "Люба", "Галя", "Рита"]
        psfam = ["Иванов", "Петров", "Сидоров", "Кузнецов", "Попов", "Смирнов", "Васильев", "Морозов", "Новиков", "Федоров", "Михайлов", "Алексеев", "Григорьев", "Егоров", "Козлов", "Соколов", "Орлов", "Тарасов", "Крылов", "Лебедев", "Иванова", "Петрова", "Сидорова", "Кузнецова", "Попова", "Смирнова", "Васильева", "Морозова", "Новикова", "Федорова", "Михайлова", "Алексеева", "Григорьева", "Егорова", "Козлова", "Соколова", "Орлова", "Тарасова", "Крылова", "Лебедева"]
        psagegod = random.randint(10, 60)
        psjob = ["Программист", "Инженер", "Учитель", "Врач", "Юрист", "Дизайнер", "Менеджер", "Маркетолог", "Повар", "Архитектор", "Фотограф", "Журналист", "Писатель", "Музыкант", "Актер", "Режиссер", "Спортсмен", "Полицейский", "Пожарный", "Военный"]
        pspol = ["Мужской", "Женский"]

        Info = [
            "Имя: " + random.choice(psname),
            "Фамилия: " + random.choice(psfam),
            "Возраст: " + str(psagegod),
            "Профессия: " + random.choice(psjob),
            "Пол: " + random.choice(pspol)

        ]

        print("Информация о Псевдо Личности:")
        print("\n".join(Info))

    elif vm == "12":
        print("")

        text_color = input("Выберите цвет текста ('red', 'green', 'blue'): ")

        try:
            n = int(input("Введите число N: "))
            print(f"Считаем до {n}:")
            for i in range(1, n + 1):
                if text_color.lower() == "red":
                    print(colorama.Fore.RED + str(i))
                elif text_color.lower() == "green":
                    print(colorama.Fore.GREEN + str(i))
                elif text_color.lower() == "blue":
                    print(colorama.Fore.BLUE + str(i))
                else:
                    print(str(i))
        except ValueError:
            print("Ошибка! Введи корректное число!")
            continue

    elif vm == "13":
        print("")

        print("Привет! Я загадаю число от N до N, и буду говорить больше/меньше, а ты попробуй угадать!")

        print("")

        try:
            minranditbm = int(input("Число будет от: "))
            maxranditbm = int(input("Число будет до: "))
        except ValueError:
            print("Ошибка! Введи корректные числа!")
            continue

        print("А теперь попробуй угадать!")

        randitnumberbm = random.randint(minranditbm, maxranditbm)

        attemps = 0

        while True:
            try:
                attempnumber = int(input("Как думаешь, какое число было загадано? "))
            except ValueError:
                print("Ошибка! Введи корректное число!")
                continue

            attemps += 1

            if attempnumber == randitnumberbm:
                print("Поздравляю, ты смог!")
                print("Ты потратил всего лишь", attemps, "попыток")
                break
            elif attempnumber > randitnumberbm:
                print("Меньше")
            else:
                print("Больше")

    elif vm == "14":
        try:
            print("")
            print("От какого дня нужно посчитать?")
            print("")

            year = int(input("Год: "))
            month = int(input("Месяц: "))
            day = int(input("День: "))

            mydate = datetime.date(year, month, day)
            todaydata = datetime.date.today()

            ResultateDataToDay = todaydata - mydate

            print("С этой даты прошло", ResultateDataToDay, "Дней!")

        except ValueError:
            print("Извините, напишите дату числами")

    else:
        print("Ошибка! Введи число от 0 до 14!")
        print("")
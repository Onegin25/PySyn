import random

def guess_the_number():
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуйте угадать его.")
    
    while True:
        # Генерация случайного числа
        secret_number = random.randint(1, 100)
        attempts = 0
        
        while True:
            try:
                # Запрос ввода числа от пользователя
                guess = int(input("Введите ваше предположение: "))
                
                # Проверка введенного числа
                if guess < 1 or guess > 100:
                    print("Пожалуйста, введите число в диапазоне от 1 до 100.")
                    continue
                
                attempts += 1
                
                if guess < secret_number:
                    print("Слишком маленькое.")
                elif guess > secret_number:
                    print("Слишком большое.")
                else:
                    print(f"Поздравляю, вы угадали! Загаданное число было {secret_number}.")
                    print(f"Вы угадали число за {attempts} попыток.")
                    break
            
            except ValueError:
                print("Ошибка: введите целое число.")
        
        # Возможность повторной игры или завершения игры
        play_again = input("Хотите сыграть еще раз? (да/нет): ").strip().lower()
        if play_again != 'да':
            print("Спасибо за игру! До свидания!")
            break
        # Запуск игры
guess_the_number()
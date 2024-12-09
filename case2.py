import math

def calculate_factorial():
    try:
        # Запрашиваем ввод положительного целого числа
        num = int(input("Введите положительное целое число: "))
        
        # Проверяем, что число положительное
        if num < 0:
            raise ValueError("Число должно быть положительным.")
        
        # Вычисляем факториал с использованием библиотеки math
        result = math.factorial(num)
        
        # Выводим результат
        print(f"Факториал числа {num} равен {result}")
    
    except ValueError as e:
        # Обрабатываем ошибки ввода
        print(f"Ошибка: {e}. Пожалуйста, введите положительное целое число.")
    except Exception as e:
        # Обрабатываем любые другие ошибки
        print(f"Произошла ошибка: {e}")

# Запускаем функцию
calculate_factorial()

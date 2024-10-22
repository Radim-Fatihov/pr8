total_sum = 0

while True:
    user_input = input("Введите число (или 'stop' для завершения): ")
    
    if user_input.lower() == "stop":
        break 

    try:
        number = float(user_input)
        total_sum += number
    except ValueError:
        print("Ошибка: введено не число. Пожалуйста, введите корректное число или 'stop' для завершения.")

print(f"Сумма введенных чисел: {total_sum}")

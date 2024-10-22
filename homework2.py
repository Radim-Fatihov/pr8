while True:
    try:
        num1 = int(input("Введите первое целое число: "))
        num2 = int(input("Введите второе целое число: "))
        result = num1 + num2
        print(f"Сумма: {result}")
    except ValueError:
        print("Пожалуйста, вводите только целые числа.")

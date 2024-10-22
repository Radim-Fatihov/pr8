def get_integer_input(prompt):
    while True:
        user_input = input(prompt).strip()
        
        if user_input.isdigit() and (user_input != "0"):
            return int(user_input)
        elif user_input == "0":
            return 0
        elif user_input.startswith('-') and user_input[1:].isdigit():
            return int(user_input)
        else:
            print("Ошибка: введите целое число. Числа не могут начинаться с ведущего нуля (например, '01' недопустимо).")

a = get_integer_input("Введите первое число (a): ")
b = get_integer_input("Введите второе число (b): ")

start = min(a, b)
end = max(a, b)

print(f"Целые числа между {a} и {b}:")

for number in range(start + 1, end):
    print(number)





# 1. Користувач вводить три цифри з клавіатури.
# Залежно від вибору користувача програма виводить
# на екран максимум із трьох,
# мінімум із трьох або середньоарифметичне трьох чисел.

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
third = int(input("Enter third number: "))

choose_the_number = input("Enter MAX, MIN or AVER: ")
if choose_the_number != "MAX" and choose_the_number != "MIN" and choose_the_number != "AVER":
    print("Incorrect inquiry")
else:
    if choose_the_number == "MAX":
        if first > second > third:
         print (first)
        elif second > first > third:
            print(second)
        else:
            print (third)
    elif choose_the_number == "MIN":
        if first < second < third:
            print(first)
        elif second < first < third:
            print (second)
        else:
            print (third)
    elif choose_the_number == "AVER":
        print(int((first+second+third)/3))


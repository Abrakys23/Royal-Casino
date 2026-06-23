import random

balance = 100
print("Добро пожаловать в Royal Casino")
for i in range(99999):
    print("Выберите действие")
    print("------------------------------")
    print("1 - Game")
    print("2 - Balance")
    print("3 - Close Game")
    print("------------------------------")
    move = int(input("Действие: "))

    if move == 1:
        if balance <= 0:
            print("Ваш баланс очень мал. Вы проиграли(")
            break

        stavka = int(input("Сделайте ставку "))
        if stavka > balance:
            print("Ставка больше вашего баланса")
            break

        win1 = random.randint(5, 7)
        win2 = random.randint(5, 7)
        win3 = random.randint(5, 7)

        if stavka <= balance:
            print("Вы поставили ", stavka, " Лари")
            print(win1, win2, win3)
        balance -= stavka

        if win1 == win2 == win3:
            stavka *= 5
            balance += stavka
            print("Поздравляем, вы победили и выигрыли ", stavka, "Лари")
        else:
            print("К сожалению вы проиграли. Повезет в следующий раз...")
            stavka = 0

    if move == 2:
        print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        print("Баланс Лари - ", balance)
        print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

    if move == 3:
        print("До скорой встречи в Royal Casino")
        break

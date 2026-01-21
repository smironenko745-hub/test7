import random

health_player = 100
atack_player = 15

health_enemy = random.randint(100, 200)
atack_enemy = random.randint(10, 20)

turn = 1 # turn 1 = jucatorul alege, turn 2 = inamicul alege

def atack():
    global health_enemy, turn
    if turn == 1:
        health_enemy -= atack_player + random.randint(1,5)
        turn = 2
        if health_enemy <= 0:
            print("Ai castigat")
            exit()

        choice()


def heal():
    global health_player, turn
    if turn == 1:
        health_player += random.randint(10, 20)
        turn = 2
        if health_player > 100:
            health_player = 100

        choice()

def atack_enemyy():
    global health_player, turn
    health_player -= atack_enemy
    if health_player <= 0:
        print("Ai pierdut")
        exit()
    turn = 1

def heal_enemy():
    global health_enemy, turn
    health_enemy += random.randint(1,10)
    turn = 1

def choice():
    c = random.randint(1,2)
    if c == 1:
        atack_enemyy()
    elif c == 2:
        heal_enemy()

def optiuni():
    print("Viata jucator: ", health_player, "Viata inamic: ", health_enemy)
    print("1 - Atack")
    print("2 - Heal")
    print("3 - Leave game")

while True:
    optiuni()
    n = int(input("Ce optiune alegeti: "))
    if n == 1:
        atack()
    elif n == 2:
        heal()
    elif n == 3:
        print("La revedere")
        break
    else:
        print("Ati scris gresit")
import random
import colorama
from colorama import Fore, Style
import time

colorama.init()

print("""
Bienvenue dans votre DiceGame !
Ici vous controlez le hasard. Lol\n
Pour gagner, vous devez atteindre 100 points.
Vous perdez votre tour si vous jeter un dé d'une valeur de 1.\n
On est parti !
""")

response = input("Voulez-vous commencer une nouvelle partie (oui/non) ? ")

player1 = input("Nom du joueur N°1 : ").upper()
player2 = input("Nom du joueur N°2 : ").upper()


def RandomDice():
    return random.randint(1, 6)


launched = True
points1 = points2 = 0
points_tmp = 0

# Lequel des deux joueurs démarre le jeu
random_player = RandomDice()
if random_player >= 4:
    tour1, tour2 = True, False
else:
    tour2, tour1 = True, False


while launched:

    # Tour du joueur 1
    while tour1:
        random_dice = RandomDice()
        print(f"\n{player1} a jeté {Fore.CYAN}{random_dice}{Style.RESET_ALL}")
        if random_dice > 1:
            points_tmp += random_dice
            print(f"Points temp = {Fore.YELLOW}{points_tmp}{Style.RESET_ALL}")
            choice = input("Encore ou Stop (e/s) ? ")
            if choice == 'e':
                break
            elif choice == 's':
                points1 += points_tmp

        else:
            print("Tour perdu")

        tour2, tour1 = True, False
        points_tmp = 0
        print(f"{player1} totalise {Fore.BLUE}{points1}{Style.RESET_ALL} points")
            
        if points1 >= 50:
            tour2, launched = False, False
            print(f"{Fore.GREEN} Bravo {player1} {Style.RESET_ALL}")

    # Tour du joueur 2
    while tour2:
        random_dice = RandomDice()
        print(f"\n{player2} a jeté {Fore.MAGENTA}{random_dice}{Style.RESET_ALL}")
        if random_dice > 1:
            points_tmp += random_dice
            print(f"Points temp = {Fore.YELLOW}{points_tmp}{Style.RESET_ALL}")
            choice = input("Encore ou Stop (e/s) ? ")
            if choice == 'e':
                break
            elif choice == 's':
                points2 += points_tmp

        else:
            print("Tour perdu")

        tour1, tour2 = True, False
        points_tmp = 0
        print(f"{player2} totalise {Fore.RED}{points2}{Style.RESET_ALL} points")
            
        if points1 >= 50:
            launched = False, False
            print(f"{Fore.GREEN} Bravo {player2} {Style.RESET_ALL}")

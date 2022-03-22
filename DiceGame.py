import random
import colorama
from colorama import Fore, Style
import time

colorama.init()

WIN = 100
play = True

print(f"""
Bienvenue dans votre DiceGame, le jeu de dés le plus cool !
A chaque tour, vous avez le choix entre continuer votre tour et jeter un autre dé
ou passer votre tour en engrangeant le total de points marqués par les dés jetés.
Vous perdez votre tour si vous jeter un dé d'une valeur de 1.
Pour gagner, vous devez atteindre {WIN} points.
On est parti !
""")


def RandomDice():
    return random.randint(1, 6)


while play:
    response = input("\nVoulez-vous commencer une nouvelle partie (oui/non) ? ")
    if response == "oui":
        player1 = input("Joueur N°1 : ").upper()
        player2 = input("Joueur N°2 : ").upper()
        launched = True
        points1 = 0
        points2 = 0
        points_tmp = 0
        # Lequel des deux joueurs démarre le jeu
        random_player = RandomDice()
        if random_player >= 4:
            tour1, tour2 = True, False
        else:
            tour2, tour1 = True, False
    else:
        exit("Yafoy ! Reste cool Bro...")

    while launched:

        # Tour du joueur 1
        while tour1:
            random_dice = RandomDice()
            time.sleep(0.8)
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
            time.sleep(0.8)
            print(f"{Fore.BLUE}{player1} {points1} - {Fore.RED}{points2} {player2} {Style.RESET_ALL}")

            if points1 >= WIN:
                time.sleep(2)
                print(f"{Fore.GREEN}\nBravo {player1}{Style.RESET_ALL}")
                tour2, launched = False, False

        # Tour du joueur 2
        while tour2:
            random_dice = RandomDice()
            time.sleep(0.8)
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
            time.sleep(0.8)
            print(f"{Fore.BLUE}{player1} {points1} - {Fore.RED}{points2} {player2} {Style.RESET_ALL}")

            if points2 >= WIN:
                launched = False
                time.sleep(2)
                print(f"{Fore.GREEN}\nBravo {player2}{Style.RESET_ALL}")

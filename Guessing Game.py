
# guessing-game v1.0 - 2024-05-17 - Erste spielbare version mit highscore
# guessing-game v2.0 - 2024-06-04 - Exceptions mit try ... except abfangen
# guessing-game v3.0 - 2024-06-07 - Funktion play und play again Möglichkeit.

import random

def load_highscore(filename):
    try:
        with open(filename, 'r') as file:
            highscore = int(file.read())
    except (FileNotFoundError, ValueError):
        highscore = None
    return highscore

def save_highscore(filename, highscore):
    with open(filename, 'w') as file:
        file.write(str(highscore))

def play():
    highscore_file = 'highscore.txt'
    highscore = load_highscore(highscore_file)

    print("Willkommen zum Zahlenratespiel!")
    if highscore is not None:
        print(f"Der aktuelle Highscore liegt bei {highscore} Versuchen.")
    else:
        print("Es gibt noch keinen Highscore.")

    number = random.randint(1, 100)
    print(number)
    user_wins = False
    score = 0

    while not user_wins:  # alternative: user_wins == False
        score += 1 # kurzform für: score = score +1

        try:
            guess = int(input("Geben Sie eine Zahl zwischen 1 und 100 ein:"))
            if guess < 1 or guess > 100:
                raise ValueError
        except ValueError:
            print("Falsche eingabe!")
            continue

        if number == guess:
            print(f"Yes, {number} is the winner. Score: {score}")
            user_wins = True
        elif guess > number:
            print("Die gesuchte Zahl ist kleiner.")
        else:
            print("Die gesuchte Zahl ist größer.")
    # bis hier ist die function play
    if highscore is None or score < highscore:
        print(f"Neuer Highscore! Du hast den bisherigen Highscore von {highscore} Versuchen geschlagen.")
        save_highscore(highscore_file, score)
    else:
        print(f"Du hast {score} Versuche gebraucht. Der Highscore liegt weiterhin bei {highscore} Versuchen.")

#def save_score(score):
    # speichert den HIGHSCORE in einer DATEI ab.
    #TODO: implementieren Sie diese Funktion.
#    highscore = open("Highscore", "r+")
#    pass

while True:  # Dauerschleife
    play()

    correctUserInput = False
    while not correctUserInput:
        prompt = input("Wollen Sie noch eine Runde spielen? [y/n]")

        if prompt == 'n':
            exit()
        elif prompt == 'y':
            correctUserInput = True
        else:
            print("Falsche eingabe nur y oder n erlaubt.")

import random
import time

print("\nWELCOME TO THE HANGMAN\n")
Name=input ("Enter your name:")
print("HELLO" + Name + "BEST OF LUCK")
time.sleep(2)
print("THE GAME IS ABOUT TO BEGIN")
time.sleep(3)


def main():
     global count
     global display
     global word
     global alreadygussed
     global length
     global playgame
word_to_guess =["February","image","movie","kids","Rocket","Operation","Science","Computer",
              "Rhyme","Cellphone","Mathematics"]
word = random.choice(word_to_guess)
length = len(word)
count = 0
display = '_'*length
already_guessed = []
play_game = ""


def play_loop():
    global  play_game
    play_game= input("Do you want to play again? y=yes , n=no \n")
    while play_game not in ["y","n","Y","N"]:
        play_game = input("Do you want to play game again y=yes , n= no \n")
    if play_game =="y":
        if __name__ == '__main__':
          main()
        elif play_game =="n":
          print("Thanks for playing the Game \n")
          exit()

def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit=5
    guess=input("This is the Hangman word:" + display + "Enter your guess \n")
    guess=guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()

    elif guess in word:
         already_guessed.extend([guess])
         index = word.find(guess)
         word = word[:index] + "" + word[index + 1:]
         display = display[:index] + guess + display[index + 1:]
         print(display + "\n")

    elif guess in already_guessed:
         print("Try another letter.\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:", already_guessed, word)
            play_loop()

    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()

    elif count != limit:
        hangman()


main()

hangman()


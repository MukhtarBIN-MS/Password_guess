import random
import time

# Welcome to password guessing game 

print("Welcome to my password Guessing App")

# Get name of the user

print("Hy there, Please input your name")
name = input("Your name: ")

print("Welcome " + name + " To password guessing game\n")

time.sleep(3)

def main():
    global password
    global count
    global length
    global already_guessed
    global play_game_again
    global display
    
    password = "Mukhtar"
    length = len(password)
    display = "_" * length
    
    count = 0
    already_guessed = []
    
def play_again():
    global play_game_again
    
    play_game_again = input("Do you want to play password guessing game again ??")
    while play_game_again not in ["Y", 'y', 'N', 'n']:
        print("Invalid answer, try with Y OR N")
        play_again()
        
    if play_game_again == "Y":
        main()
    elif play_game_again == "N":
        print("Thanks for playing, Bye")
        exit()
        
def password_guess():
    global count
    global already_guessed
    global length
    
    limit = 5
    words_count = 0
    
    
    guess = input("The password has " + display + "(" + str(length) +")" +" words, Enter a word to start guessing ")
    guess = guess.strip()
    
    if len(guess.strip()) == 0 or len(guess.strip()) >=2  or guess <="9":
        print("Invalid selection")
        password_guess()
        
    elif guess in password:
        print("Good continue")
        words_count += 1
        print(f"{str(length - words_count)} words remaining")
        already_guessed.extend([guess])
        
    elif guess in already_guessed:
        print("Already guessed, try with another word")
        
    else:
        count +=1
        
        if count == 1:
            time.sleep(1)
            print("Wrong guess " + str(limit-count) + " attempts remaining")
        elif count == 2:
            time.sleep(1)
            print("Wrong guess " + str(limit-count)  + " attempts remaining")
        elif count == 3:
            time.sleep(1)
            print("Wrong guess " + str(limit-count)  + " attempts remaining")
        elif count == 4:
            time.sleep(1)
            print("Wrong guess " + str(limit-count) + " attempts remaining")
        elif count == 5:
            print("Game over")
            play_again()
            
    if password == "_" * length:
        print("Congratulations You win!!")
        play_again()
        
    elif count != limit:
        password_guess()
            
main()

password_guess()
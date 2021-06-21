import sys
import random
from art import logo1, logo2, game_over_logo, you_win, unlock
import winsound



print(logo2)
print("")
print("***UNLOCK 3 MEMORIES TO WIN THE GAME***")
print("")
print("Argh... my head is killing me...😵‍💫😖")
print("What the hell happened last night??😲")
print("Let's see... I'm in my flat -- that's good! --")

memories = []

def quit():
    wanna_quit = input("> ").lower()
    if wanna_quit == "y":
        print("👎👎👎Booo! You quit the game!")
    elif wanna_quit == "n":
        main(sound)
    else:
        print("Sorry I didn't catch that")
        quit()


def game_over():
    print(game_over_logo)
    print("You failed!")
    print()
    print("Your progress has been saved")
    print()
    print("Do you want to try again?")
    try_again = input("y / n > ")
    if try_again == "y":
         main(sound)
    elif try_again == "n":
        sys.exit()
    else:
        game_over()

def phone(_has_run=[]):
    if _has_run: 
        print("I've already checked my phone.")
        main(sound)
    else:
        print("*** 📱 Check ***")
        print("---📞 calls")
        print("---📩 texts")
        print("---📧 emails")
    
        answer = input("> ").lower()
        if answer not in ["calls", "texts", "emails"]:
            print("Sorry I didn't catch that...🤔")
            phone()
        elif answer == "calls":
            print("Last calls:")
            print("")
            contacts = ["Michelle", "Jack", "Ruby"]
            code_nation = ["Dave", "Tim", "Jay"]
            for i in contacts:
                print("-", i)
            print()
            print("or... call someone from Code Nation...")
            print()
            for name in code_nation:
                print("-", name)
            print("Who should I call?")
            contact = input("> ").lower()
            if contact.lower() in [x.lower() for x in contacts]:
                print(f"{contact} is not answering the phone...")
                print("Maybe I need to check something else in my phone...")
                phone()
            elif contact.lower() in [x.lower() for x in code_nation]:
                print(f"{contact} has blocked you....")
                phone()
            elif contact.lower() not in [x.lower() for x in contacts]:
                print(f"There is no {contact} in your contacts.")
                phone()
            

        elif answer == "texts" or answer == "text":
            print("Last text is from my bestie (at 7am this morning)...")
            print("""
            BESTIE -- Yesterday night you opened a bunch of tampons and said they looked like little ghosts...
                   -- ... and you tried to "haunt" me...
            """)
            reply1 = "1----- What?? Where did I get the tampons from??"
            reply2 = "2----- I don't use tampons!" 
            reply3 = "3----- ...they do kinda look like little ghosts..."
            print()
            print()
            print("Which of these options do you want to text back? (type 1, 2 or 3)")
            print(reply1)
            print(reply2)
            print(reply3)
            reply = input("> ")
            if reply.lower() == "1":
                print("typing...")
                print("What?? Where did I get the tampons from??")
                phone()
            elif reply.lower() == "2":
                print("typing...")
                print("2----- I don't use tampons!")
                phone()
            elif reply.lower() == "3":
                print("typing...")
                print("...they do kinda look like little ghosts...")
                phone()
            else:
                print("Sorry I didn't catch that")
                phone()
        else: 
            answer == "emails"
            print("My last email is an Uber receipt. I've ordered an Uber from Northern Quarter.... Hold on...")
                
            secret_word = "Terrace"
            guess_count = 0
            guess_limit = 3
            while guess_count < guess_limit:
                print("""In which of these Manchester bars did I party yesterday night? 
                Cane & Grane
                Terrace
                Wetherspoons
                Dive
                Bar 21
                """)
                guess = input("> ").lower()
                guess_count += 1
                if guess.lower() != secret_word.lower():
                    print("No... I'm sure I wasn't there... Let's try again")
                elif guess.lower() == secret_word.lower():
                    print("Yes! Now I remember! I was in Terrace!")
                    memories.append("Phone Memory")
                    print()
                    print()
                    print()
                    print(unlock)
                    print(f" *** 🌟YOU HAVE UNLOCKED {len(memories)} MEMORIES!🌟 ***")
                    _has_run.append(1)    
                    main(sound)
                    break
            else:
                game_over()

            
def roll_dices(_has_run=[]):
    if _has_run: 
        print("I've already checked that.")
        main(sound)
    else:
        min = 1
        max = 6
        roll_again = "y"
        roll_again = input("Roll the dices in pocket? (y / n) ").lower()
        if roll_again == "y":
            print("Rolling the dices...")
            print("The values are....")
            print (random.randint(min, max))
            print (random.randint(min, max))
            roll_dices()
        elif roll_again == "n":
            print("Dices......Of course! I was in the casino last night!")
            memories.append("Coat Memory")
            print()
            print()
            print()
            print(unlock)
            print(f" *** 🌟YOU HAVE UNLOCKED {len(memories)} MEMORIES!🌟 ***")
            _has_run.append(1)    
            main(sound)
        else:
            print ("Sorry didn't catch that")
            roll_dices()
 

def coat(_has_run=[]):
    if _has_run: 
        print("I've already checked my coat.")
        main(sound)
    else:
        print("Check right or left pocket?")
        answer = input("> ").lower()
        if answer not in ["right", "left"]:
            print("Sorry I didn't catch that...🤔")
            coat()
        elif answer == "right":
            print("What?? A condom?? What the heck did I do last night?!")
            coat()
        elif answer == "left": 
            roll_dices()
           
    _has_run.append(1) 


def ana(_has_run=[]):
    if _has_run: 
        print("I've already checked the trash.")
        main(sound)
    else:
        kajbalkjc = "blackjack"
        alqetiu = "tequila"
        dickiefrench = "fried chicken"

        guess_count = 0
        guess_limit = 3
        while guess_count < guess_limit:
                print("...kajbalkjc...")
                print("'kajbalkjc'? What does this mean? Is it even a word??")
                print("What word can it be...")
                kajbalkjc_pro = input("").lower()
                guess_count += 1
                if kajbalkjc_pro != kajbalkjc:
                    print ("No that can't be right, Maybe it's something else?")
                elif kajbalkjc_pro == kajbalkjc:
                    print ("Of course! It's 'BLACKJACK'!")
                    guess_count = 0
                    guess_limit = 3
                    while guess_count < guess_limit:
                        print("Let me see what else is in there...")
                        print("...alqetiu...")
                        print("What's that now??")
                        print("What word can it be...")
                        alqetiu_pro = input("").lower()
                        guess_count += 1
                        if alqetiu_pro != alqetiu:
                            print ("No that can't be right, Maybe it's something else?")
                        elif alqetiu_pro == alqetiu:
                            print ("Of course! It's 'TEQUILA'!")
                            guess_count = 0
                            guess_limit = 3
                            while guess_count < guess_limit:
                                print("Let me see what else is in there...")
                                print("...dickiefrench...")
                                print ("OMG... this is getting worse...")
                                print("What word can it be...")
                                dickiefrench_pro = input("").lower()
                                guess_count += 1
                                if dickiefrench_pro != dickiefrench:
                                    print ("No that can't be right, Maybe it's something else?") 
                                elif dickiefrench_pro == dickiefrench:
                                    print ("Of course! It's 'FRIED CHICKEN'!")
                                    memories.append("Kitchen Memory")
                                    print()
                                    print()
                                    print()
                                    print(unlock)
                                    print(f" *** 🌟YOU HAVE UNLOCKED {len(memories)} MEMORIES!🌟 ***")
                                    _has_run.append(1)
                                    main(sound)                                               
        else:
            game_over()                               

def kitchen(_has_run=[]):
    if _has_run: 
        print("I've already been in the kitchen.")
        main(sound)
    else:
        print("Shall I look in the microwave or the trash bin?")
        answer = input("> ").lower()
        if answer not in ["trash", "microwave"]:
            print("Sorry I didn't catch that...🤔")
            kitchen()
        elif answer == "microwave":
            print("What is my tablet doing in the microwave??")
            kitchen()
        elif answer == "trash" or answer == "trash bin" or answer == "bin":
            ana()
    _has_run.append(1)

        
def win_game():
    if len(memories) == 3:
        print("""NOW I REMEMBER IT ALL.....!!

         We had predrinks at mine, then we hit the town.
         We went to the casino, we gambled... and I lost £700!
         Then I slipped and fell on the blackjack table and they kicked us out..
         I had the BRILLIANT idea to take a tequila shot in every bar on the way from Portland St to Northern Quarter...
         That's a LOT of bars!
         Somehow we ended up in Terrace, in Northern Quarter, and I think I met someone there...
         We decided to hook up, and my friend gave me a condom... but it's still unused...
         That's probably why I decided to have a take away fried chicken and call an Uber home.
         ... and I put my tablet in the microwave thinking it was pizza!

         Sounds like a good night! 
        
        """)
        print(you_win)
        print("👏👏👏")
        print("Congratulations! You win the game!🏆")
        print()
        print()
        print()
        sys.exit()
        
sound = winsound.PlaySound("Chill.wav", winsound.SND_ASYNC + winsound.SND_LOOP)  

def main(sound):
    win_game()
    print("")
    print("What shall I do?")
    print("")
    print("📱 Check my phone")
    print("🧥 Check my coat")
    print("➡️ Go to the kitchen")
    print("❌ QUIT GAME")
    print("")
    answer = input("> ").lower()
    if answer == "phone" or answer == "check phone" or answer == "check my phone":
        phone()
    elif answer == "coat" or answer == "check coat" or answer == "check my coat":
        coat()
    elif answer == "kitchen" or answer == "go to kitchen" or answer == "go to the kitchen":
        kitchen()
    elif answer == "help":
        print("")
        print("What shall I do?")
        print("")
        print("📱 Check my phone")
        print("🧥 Check my coat")
        print("➡️ Go to the kitchen")
        print("❌ QUIT GAME")
        print("")
        answer = input("> ").lower()
    elif answer == "quit":
        quit_choice = input("Are you sure you wanna quit? y / n").lower()
        if quit_choice == "y":
            quit()    
        elif quit_choice == "n":
            main(sound)
        else: 
            print("sorry I didn't catch that")
            main(sound)
    else:
        print("Sorry I didn't catch that...🤔")
        main(sound)
            
            
main(sound)



###stage1###

print("welcome player, the rules are simple.\nYou have a word to guess, 5 hints and 5 tries")
ready = input("are you ready ? \n types \"y\" or \"n\":")
if ready == "n":
    print("well, too late to call for your mama")
elif ready == "y":
    print("i like your enthusiasm")
else:
    print("if you cant answer that, i see no hope for the word; here it is")
answer = "mclaren"
answer_check = "Mclaren"
hints = {1: "i am a word of 7 letters",
         2: "Mcdonals's biggest inspiration",
         3: "if you haven't guessed yet that i am a car you're really bad at this game",
         4: "i'm from where the football was invented",
         5: "Maybe that's why i am a sporty",
         6: "i mainly do super cars",
         7: "my name rhymes with karen but i'm definitely not one"}


def boucle(number_of_tries,x):
    print(hints[1])
    guess_1 = input("what's the word ?:").lower()
    while number_of_tries != 0 and guess_1 != answer :
        print("nope genuis," + str(number_of_tries) + " chances left")
        x += 1
        number_of_tries -= 1
        print(hints[x])
        guess_1 = input("what's the word ?:").lower()
    return guess_1

if boucle(4,1) == answer:
    print("correct, smarter than i thought")
else:
    print("well no surprise genius, you lost")
    retry = input("more hints or should i give you the answer ?\n type 1 or 2:")
    while retry != "1" and retry != "2":
            print("invalid answer, 1 or 2 genuis")
            retry = input("more hints or should i give you the answer ?\n type 1 or 2:")
    if retry == "1":
        print("alright two more chances to guess!")
        print(hints[6])
        guess_1 = input("what's the word ?:").lower()
        if boucle(1, 6) == answer:
            print("correct, finally, i guess it's better late than never")
        else:
            print("no hope for you. The answer is " + answer_check)
    elif retry == "2":
        print("well loser, the answer was " + answer_check)
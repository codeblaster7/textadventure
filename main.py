# Text Based Adventure Game

level = 1
health = 100
money = 10
items = []
won = False

name = input("What is your name? ")
by = input("What is your birth year? ")
age = 2020 - int(by)

if age <= 8:
    print(f"Oh! {name}. You are not old enough to play this game")
else:
    print(f"Hello, {name}. I see you are {age} years old. So you are\n"
          f"old enough to play this game. You are in level 1 and your health is 100\n"
          f"Make sure to take wise decisions here or else you will lose your health\n"
          f"And you have 10 dollars... Don't worry you will earn more :)")

    print("You are in a cave... with deep silence... you wanna go outside of the cave,\n"
          "you wanna go left or right?")

    answer = input("")
    if answer == "left":
        print("You went left, and a boar attacked you and you lost 10 health")
        health -= 10
        print(f"Level: {level}\n"
              f"Health: {health}\n"
              f"Money: ${money}")
    elif answer == "right":
        print("You went right, and you saw a man you is fainted infront of you, will you give your 5 dollars to cure him or ignore him")
        level += 1
        print(f"Level: {level}\n"
              f"Health: {health}\n"
              f"Money: ${money}")
        answer2 = input("(yes or no) ")
        if answer2 == "yes":
            print("Yay! You cured him and that man was very happy because of your kind act and gave you 100 dollars")
            money += 100
            level += 1
            print(f"Level: {level}\n"
                  f"Health: {health}\n"
                  f"Money: ${money}")
            print("A man passing gives you a phone. Will you accept it? ")
            answer3 = input("(yes/no) ")
            if answer3 == "yes":
                print("Yay! You got a smartphone.")
                items.append("smartphone")
                level += 1
                print(f"Level: {level}\n"
                      f"Health: {health}\n"
                      f"Money: ${money}\n"
                      f"Items: {items[0].title()}")
                print("You got a heart attack, you have to go hospital so you called them and you recovered. But 50 dollars are reduced")
                level += 1
                money -= 50
                print(f"Level: {level}\n"
                      f"Health: {health}\n"
                      f"Money: ${money}\n"
                      f"Items: {items[0].title()}")
                print("Now where you wanna go?")
                answer4 = input("(left/right) ")
                if answer4 == "left":
                    print("You fell of the edge and died")
                    print("You died with: ")
                    print(f"Level: {level}\n"
                          f"Health: {health}\n"
                          f"Money: ${money}\n"
                          f"Items: {items[0].title()}")
                elif answer4 == "right":
                    print("You went to the right, started a business in city and you are a millionaire now")
                    print("You won with: ")
                    level += 1
                    money += 100000000
                    money -= 60
                    won = True
                    print(f"Level: {level}\n"
                          f"Health: {health}\n"
                          f"Money: ${money}\n"
                          f"Items: Can't Count, as you have many")
            elif answer3 == "no":
                print("Oh! you didn't get the smartphone")
                level += 1
                print(f"Level: {level}\n"
                      f"Health: {health}\n"
                      f"Money: ${money}\n")
                print("You got a heart attack, you have to go hospital but you can't call them as you don't have any phone. So you died")
                health = 0
                print("You died with: ")
                print(f"Level: {level}\n"
                      f"Health: {health}\n"
                      f"Money: ${money}\n")
                exit()
        elif answer2 == "no":
            print("You ignored him but after that a wild dog attacked you and you lost all your health")
            health = 0
            print("You died with: ")
            print(f"Level: {level}\n"
                  f"Health: {health}\n"
                  f"Money: ${money}")
if won == True:
    actual_win = "won this game"
elif not won:
    actual_win = "lost this game"

with open("choices.txt", "a") as f:
    f.write(f"{name}'s answers were: \n"
            f"1. {answer}\n"
            f"2. {answer2}\n"
            f"3. {answer3}\n"
            f"4. {answer4}\n"
            f"And {actual_win}\n")

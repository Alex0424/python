import random

def start_game():
    for number in number_list:
        user_answer = int(input(f"{number} * {multiply_number} = "))
        correct_answer = number * multiply_number
        if user_answer == correct_answer:
            print("correct")
        else:
            print("incorret")


while True:
    play = input("Enter 'yes' to play Or Enter to quit: ").upper()
    if play == "Y" or play == "YES":
        multiply_number = int(input("Enter multiplication number: "))
        first_number = int(input("Enter the first number: "))
        second_number = int(input("Enter the second number: "))
        if abs(first_number - second_number) > 100:
            print("more than 100 numbers is too much")
            exit()
        number_list = list(range(first_number, second_number + 1))

        random_order = input("Random order? (yes/no)\n: ").lower()
        if random_order == "n" or random_order == "no":
            start_game()
        elif random_order == "y" or random_order == "yes":
            random.shuffle(number_list)
            start_game()
        else:
            print("Invalid input")
            break
    else:
        exit()

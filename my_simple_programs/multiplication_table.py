import random
numbers = [2,3,4,5,6,7,8,9]

while True:
    #random.shuffle(numbers)
    user_number = int(input("what number do you want to train? 2,3,4,5,6,7,8,9: "))
    for number in numbers:
        user_answer = int(input(f"{user_number} * {number} = "))
        correct_answer = user_number * number
        if user_answer == correct_answer:
            print("Correct")
        else:
            print("Wrong") 

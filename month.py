import calendar
import time
import random

print("Welcome to Guess The Month Position Game")
months_old = list(calendar.month_name[1:13])
months = [month.lower() for month in months_old]


#Order Month Game
def order_month():

    global months
    order = 1
    correct_answers = 0
    
    for month in months:
        user_input = input(f"What month is in order {order} out of 12?: ").lower()
        if user_input == month:
            print("Correct")
            correct_answers += 1
        else:
            print("Incorrect")
        order += 1 
    print(f"Your Score: {correct_answers}/12")

#Unorder Month Game
def unorder_month():

    global months
    random_months = months.copy()
    random.shuffle(random_months)
    correct_answers = 0

    for month in random_months:
        user_input = input(f"What month is in order {months.index(month)+1} out of 12?: ").lower()
        if user_input == month:
            print("Correct")
        else:
            print("Incorrect")

def begin_timer():
    global start_time  
    start_time = time.time() 
    print("Timer started!")

def end_timer():
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")


# MENU OPTIONS
while True:
    user_input = input("Select 1 for order months game \nSelect 2 for unorder months game \nSelect 0 to exit \nAnswer: ")
    if user_input == "1":
        begin_timer()
        order_month()
        end_timer()
    elif user_input == "2":
        begin_timer()
        unorder_month()
        end_timer()
    elif user_input == "0":
        print("Goodbye!")
        exit()
    else:
        print("Unknown Answer")
        time.sleep(2)

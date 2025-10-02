# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247

# + 129

# ------

# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.

def problem_generator():
    import random
    number1 = random.randint(1,999)
    number2 = random.randint(1,999)
    print(f"  {number1}")
    print("+", number2)
    print("------")
    correct_answer = number1 + number2
    return correct_answer

def user_response():
    user_answer = int(input("Enter your answer as an integer: "))
    return user_answer

solution = problem_generator()
attempt = user_response()

if solution == attempt:
    print("Your answer is correct!")
else:
    print(f'The correct answer is {solution}.')

#Created by Logan Gibson on 10/1/25
#The program's name is "Addition Quizzer"
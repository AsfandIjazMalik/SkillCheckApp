# Quiz data structure containing questions, options, and correct answers
questions = {
    1: {
        "question": "Which keyword is used to define a function in Python?",  # The question being asked
        "options": ["A. function", "B. def", "C. define", "D. func"],  # List of options for answers
        "correct_answer": "B"  # Correct answer for this question
    },
    2: {
        "question": "Which data type is used to store a sequence of characters in Python?",
        "options": ["A. int", "B. float", "C. str", "D. list"],
        "correct_answer": "C"
    },
    3: {
        "question": "What is the output of 2 ** 3 in Python?",
        "options": ["A. 6", "B. 8", "C. 9", "D. 12"],
        "correct_answer": "B"
    },
    4: {
        "question": "Which of the following is used to insert an item at a specific index in a list?",
        "options": ["A. add()", "B. insert()", "C. append()", "D. push()"],
        "correct_answer": "B"
    },
    5: {
        "question": "What will be the output of print(type([ ]))?",
        "options": ["A. <class 'list'>", "B. <class 'tuple'>", "C. <class 'dict'>", "D. <class 'set'>"],
        "correct_answer": "A"
    }
}

# Welcome message and instructions for the quiz
print('****************************************\n\t  Welcome to QUIZ APP\n****************************************\n\nImportant NOTE\nQuiz Contains 5 MCQs, each worth 5 marks\nCorrect Answer adds 5 Marks. Passing Marks: 60%\n')

# Function to display the questions and handle the quiz logic
def showing_question():
    marks = 0  # Variable to track the total marks obtained by the user
    
    # Iterate through each question in the quiz dictionary
    for question_num, all_inner_elements in questions.items():
        while True:  # Repeatedly ask the user for input until a valid answer is given
            # Display the question and available options
            print(f'\nQuestion {question_num}: {all_inner_elements["question"]}')
            for option in all_inner_elements["options"]:
                print(option)
            
            # Get user input and convert to uppercase to match the options
            answer = input('Choose A, B, C, or D: ').upper()

            # Check if the answer is valid (A, B, C, or D)
            if answer in ['A', 'B', 'C', 'D']:
                # If the answer is correct, increment the marks
                if answer == all_inner_elements["correct_answer"]:
                    print('HURRAHHHH!!! Your Answer is Correct')
                    marks += 5  # Adding 5 marks for the correct answer
                else:
                    # If the answer is wrong, display the correct answer
                    print(f'OPPS! Your Answer is Wrong\nCorrect Answer is: {all_inner_elements["correct_answer"]}')
                break  # Exit the loop to go to the next question
            else:
                # If the input is invalid, prompt the user to try again
                print('Answer Must Be In A, B, C, or D. Please try again.')
                
    # Calculate the percentage of marks obtained
    marks_percentage = (marks / 25) * 100
    print(f'\nYour Total Marks are {marks} out of 25')
    
    # Provide feedback based on the calculated percentage
    if marks_percentage >= 90:
        print(f'Super Star Excellent! Your Percentage is {marks_percentage}%\nAnd Grade Is A+')
    elif marks_percentage >= 80:
        print(f'Excellent! Your Percentage is {marks_percentage}%\nAnd Grade Is A')
    elif marks_percentage >= 75:
        print(f'Very Good! Your Percentage is {marks_percentage}%\nAnd Grade Is B+')
    elif marks_percentage >= 70:
        print(f'Good! Your Percentage is {marks_percentage}%\nAnd Grade Is B')
    elif marks_percentage >= 60:
        print(f'Good! Your Percentage is {marks_percentage}%\nAnd Grade Is C+')
    elif marks_percentage >= 50:
        print(f'Good! Your Percentage is {marks_percentage}%\nAnd Grade Is C')
    else:
        print(f'OPPS!!! You Failed To Pass The Test\n{marks_percentage}% is Not Enough to Pass')

# Call the function to start the quiz
showing_question()
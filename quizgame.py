quizes = {
    "Python Basics": [
        {
            "question": "Which data type is mutable in Python?",
            "options": {"A": "Tuple", "B": "String", "C": "List", "D": "Integer"},
            "answer": "C",
        },
        {
            "question": "Which keyword defines a function in Python?",
            "options": {"A": "func", "B": "def", "C": "define", "D": "function"},
            "answer": "B",
        },
        {
            "question": "What is the correct file extension for Python files?",
            "options": {"A": ".pt", "B": ".pyt", "C": ".py", "D": ".txt"},
            "answer": "C",
        },
        {
            "question": "Which of the following functions is used to get the length of a list in Python?",
            "options": {"A": "length()", "B": "size()", "C": "len()", "D": "count()"},
            "answer": "C",
        },
        {
            "question": "How do you insert comments in Python code?",
            "options": {"A": "// This is a comment", "B": "# This is a comment", "C": "/* This is a comment */", "D": "<!-- This is a comment -->"},
            "answer": "B",
        },
    ],
    "Data Structures": [
        {
            "question": "What is the worst-case time complexity of Selection Sort?",
            "options": {"A": "O(n)", "B": "O(n log n)", "C": "O(n^2)", "D": "O(1)"},
            "answer": "C",
        },
        {
            "question": "Which data structure operates on a LIFO (Last In, First Out) principle?",
            "options": {"A": "Queue", "B": "Stack", "C": "Array", "D": "Tree"},
            "answer": "B",
        },
        {
            "question": "Which data structure operates on a FIFO (First In, First Out) principle?",
            "options": {"A": "Stack", "B": "Queue", "C": "Tree", "D": "Graph"},
            "answer": "B",
        },
        {
            "question": "What is the best-case time complexity of Merge Sort?",
            "options": {"A": "O(n)", "B": "O(n log n)", "C": "O(n^2)", "D": "O(1)"},
            "answer": "B",
        },
        {
            "question": "In a singly linked list, what does each node point to?",
            "options": {"A": "Only the previous node", "B": "Both previous and next nodes", "C": "Only the next node", "D": "Nothing"},
            "answer": "C",
        },
    ],
    "Engineering Math": [
        {
            "question": "What is the derivative of x^2 with respect to x?",
            "options": {"A": "x", "B": "2x", "C": "x^2", "D": "2"},
            "answer": "B",
        },
        {
            "question": "What is the base-10 logarithm of 1000?",
            "options": {"A": "1", "B": "2", "C": "3", "D": "10"},
            "answer": "C",
        },
        {
            "question": "What is the integral of 1/x with respect to x?",
            "options": {"A": "ln|x|", "B": "x^2 / 2", "C": "e^x", "D": "-1/x^2"},
            "answer": "A",
        },
        {
            "question": "What is the value of the factorial of 4 (4!)?",
            "options": {"A": "12", "B": "16", "C": "24", "D": "32"},
            "answer": "C",
        },
        {
            "question": "What is the sum of angles in a triangle in degrees?",
            "options": {"A": "90", "B": "180", "C": "270", "D": "360"},
            "answer": "B",
        },
    ],
}

def run_quiz(questions, titles):
    score = 0
    wrong = []
    print(f" -----------STARTING YOUR QUIZ FOR {titles}-----------")
    for i in range(len(questions)):
        q = questions[i]
        ind = i + 1
        print(f"\nQuestion{ind}:{q['question']}")
        for k, o in q['options'].items():
            print(f"\n{k}.{o}")
        response = input("\nChoose the correct option among A,B,C,D: ").strip().upper()
        if response == q['answer']:
            if i==len(questions)-1:
                print("\nCorrect answer!")
            else:    
                print("\nCorrect answer!Let's move on to the next question")
            score = score + 1
        else:
            print(f"\nIncorrect answer...\nThe correct answer was {q['answer']} ")
            wrong.append(q)
            
    total = len(questions)
    correct_count = score
    wrong_count = len(wrong)
    accuracy = (score / total) * 100 if total > 0 else 0

    print(f"\nTest Finished!")
    print(f"Score: {score}/{total}")
    print(f"Correct Answers: {correct_count}")
    print(f"Wrong Answers: {wrong_count}")
    print(f"Accuracy: {accuracy:.2f}%")

def topic_select():
    topic = list(quizes.keys())
    print("\n========================================")
    print("          SELECT A QUIZ TOPIC           ")
    print("========================================")
    for i in range(len(topic)):
        print(f"{i+1}.{topic[i]}")
    choice = input(f"Select a topic between 1-{len(topic)}: ").strip()

    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(topic):
            selectedtopic = topic[choice - 1]
            problems = quizes[selectedtopic]
            run_quiz(problems, selectedtopic)
            return
    print("\n Invalid selection!")
topic_select()
questions = [
    {
        "question": "What is the formula of water in chemistry?",
        "answer": 'H2O'
    },
    {
        "question": "What is the name of Newton's law?",
        "answer": 'law of inertia'
    },
    {
        "question": "Who is the painter of the Mona Lisa painting?", 
        "answer": 'Leonardo da Vinci'
    },
    {
        "question": "What is the name of the biggest ocean on the world?",
        "answer": 'Pacific Ocean'
    },
    {
        "question": 'How many planets are there in the solar system?',
        'answer': '8 planets' 
    },
    {
        'question': 'What is the name of the biggest planet in the solar system?',
        'answer': 'Jupiter'
    },
    {
        'question': 'What is the name of the biggest continent on the world?',
        'answer': 'Asia'
    },
    {
        'question': 'What is the name of the biggest country on the world?',
        'answer': 'Russia'
    },
]








current_question_index = 0

while current_question_index < len(questions):
    current_question = questions[current_question_index]["question"]
    current_answer = questions[current_question_index]["answer"]

    while True:
        print(current_question + "?")
        answer = input()

        if answer.lower() == current_answer.lower():
            print("Correct!")
            break  # Doğru cevap alındığında içteki döngüden çık
        else:
            print("Incorrect! Try again.")

    current_question_index += 1

print("All questions have been answered.")

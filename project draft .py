questions = [
    {
        "question": "2+2",
        "answer": "4"
    },
    {
        "question": "2+3",
        "answer": "5"
    }
]

current_question_index = 0

while current_question_index < len(questions):
    current_question = questions[current_question_index]["question"]
    current_answer = questions[current_question_index]["answer"]

    while True:
        print("What is " + current_question + "?")
        answer = input()

        if answer.lower() == current_answer.lower():
            print("Correct!")
            break  # Doğru cevap alındığında içteki döngüden çık
        else:
            print("Incorrect! Try again.")

    current_question_index += 1

print("All questions have been answered.")
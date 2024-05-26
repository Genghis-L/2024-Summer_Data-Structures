# Copyright 2024 Genghis, 骆可瀚(Luo Kehan), kl4747@nyu.edu

# Basic functionalities, one can add more interesting features


class Question:
    def __init__(self, question, answer1, answer2, answer3, answer4, correct_answer):
        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.correct_answer = correct_answer

    def get_question(self):
        return self.question

    def get_answer1(self):
        return self.answer1

    def get_answer2(self):
        return self.answer2

    def get_answer3(self):
        return self.answer3

    def get_answer4(self):
        return self.answer4

    def get_correct_answer(self):
        return self.correct_answer

    def set_question(self, question):
        self.question = question

    def set_answer1(self, answer1):
        self.answer1 = answer1

    def set_answer2(self, answer2):
        self.answer2 = answer2

    def set_answer3(self, answer3):
        self.answer3 = answer3

    def set_answer4(self, answer4):
        self.answer4 = answer4

    def set_correct_answer(self, correct_answer):
        self.correct_answer = correct_answer


def create_questions():
    questions = [
        Question(
            "What is the main focus of procedural programming?",
            "1. Manipulating objects",
            "2. Manipulating functions",
            "3. Manipulating classes",
            "4. Manipulating data structures",
            2,
        ),
        Question(
            "In Python, what are functions inside a class called?",
            "1. Attributes",
            "2. Methods",
            "3. Procedures",
            "4. Instances",
            2,
        ),
        Question(
            "What is encapsulation in object-oriented programming?",
            "1. Combining data and methods into a single object",
            "2. Separating data and methods",
            "3. Using objects without classes",
            "4. Hiding implementation details",
            1,
        ),
        Question(
            "Which of the following is a built-in method in Python classes?",
            "1. __init__",
            "2. __main__",
            "3. __class__",
            "4. __self__",
            1,
        ),
        Question(
            "What is the first argument of every method in a Python class?",
            "1. self",
            "2. this",
            "3. cls",
            "4. obj",
            1,
        ),
        Question(
            "What happens when a subclass redefines a method from its superclass?",
            "1. Both the new and old methods get executed",
            "2. Only the new method gets executed",
            "3. Only the old method gets executed",
            "4. An error is raised",
            2,
        ),
        Question(
            "How do you define a subclass in Python?",
            "1. class SubclassName extends SuperclassName",
            "2. class SubclassName inherits SuperclassName",
            "3. class SubclassName(SuperclassName)",
            "4. class SubclassName.SuperclassName",
            3,
        ),
        Question(
            "Which Python special method is used to define how an object is represented as a string?",
            "1. __repr__",
            "2. __str__",
            "3. __print__",
            "4. __string__",
            2,
        ),
        Question(
            "What are non-method data stored by objects in a class called?",
            "1. Attributes",
            "2. Variables",
            "3. Instances",
            "4. Fields",
            1,
        ),
        Question(
            "According to the course overview, what constitutes the core of software engineering?",
            "1. Algorithms and data structures",
            "2. Programming languages",
            "3. User interfaces",
            "4. Computer hardware",
            1,
        ),
    ]

    # We can use mutators to update/change questions
    questions[0].set_question("Do you like Professor Olivier Marin?")
    questions[0].set_answer1("1. I hate him!")
    questions[0].set_answer2("2. I hate him!")
    questions[0].set_answer3("3. I hate him!")
    questions[0].set_answer4("4. I like him!")
    questions[0].set_correct_answer(4)

    return questions


def print_separator():
    print("\n" + "—" * 60 + "\n")


def ask_question(question: Question, player: str) -> bool:
    print(question.get_question())
    print(question.get_answer1())
    print(question.get_answer2())
    print(question.get_answer3())
    print(question.get_answer4())
    answer = int(input(f"{player}, please enter your choice of the answer: >"))
    return answer == question.get_correct_answer()


def result(player1_score, player2_score):
    print("Final Result: ")
    print(f"Player1 Score: {player1_score}")
    print(f"Player2 Score: {player2_score}")

    if player1_score > player2_score:
        print("Player1 wins!")
    elif player2_score > player1_score:
        print("Player2 wins!")
    else:
        print("It's a tie!")


def main():
    questions = create_questions()
    player1_score = 0
    player2_score = 0

    for i in range(5):
        print(f"Question {i+1} for Player 1:")
        if ask_question(questions[i], "Player 1"):
            print("Correct!")
            player1_score += 1
        else:
            print("Incorrect.")

        print_separator()

        print(f"Question {i+1} for Player 2:")
        if ask_question(questions[i + 5], "Player 2"):
            print("Correct!")
            player2_score += 1
        else:
            print("Incorrect.")

        print_separator()

    result(player1_score, player2_score)


if __name__ == "__main__":
    main()

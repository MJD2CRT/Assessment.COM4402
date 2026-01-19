# NAME: Modupe John Dairo

def initialise_question_bank():
    question_bank = {}

    # History Questions
    question_bank["History"] = [
        {
            "question_text": "What year did World War 2 end?",
            "options": {"A": "2000", "B": "1944", "C": "1945", "D": "1950"},
            "correct_letter": "C",
        },
        {
            "question_text": "Who was the first President of the United States?",
            "options": {
                "A": "John Dairo",
                "B": "George Washington",
                "C": "Charles Barbage",
                "D": "John Adams",
            },
            "correct_letter": "B",
        },
        {
            "question_text": "The ancient Egyptian writing system is called:",
            "options": {
                "A": "Habaacus",
                "B": "Hieroglyphics",
                "C": "Latin",
                "D": "yoruba",
            },
            "correct_letter": "B",
        },
        {
            "question_text": "The Roman Empire was centered around which modern day country?",
            "options": {
                "A": "France",
                "B": "Italy",
                "C": "Greece",
                "D": "Spain",
            },
            "correct_letter": "B",
        },
        {
            "question_text": "The Industrial Revolution began in which country?",
            "options": {
                "A": "Germany",
                "B": "Nigeria",
                "C": "United States",
                "D": "Great Britain",
            },
            "correct_letter": "D",
        },
        {
            "question_text": "The “Black Death” was primarily what type of disease?",
            "options": {
                "A": "Corona virus",
                "B": "Bubonic plague",
                "C": "Ebola",
                "D": "Influenza",
            },
            "correct_letter": "B",
        },
        {
            "question_text": "The Great Wall is most associated with which country?",
            "options": {
                "A": "China",
                "B": "India",
                "C": "Mongolia",
                "D": "Russia",
            },
            "correct_letter": "A",
        },
        {
            "question_text": "Who was famously known as the “Maid of Orléans”?",
            "options": {
                "A": "Marie Antoinette",
                "B": "Queen Elizabeth",
                "C": "Joan of Arc",
                "D": "Catherine the Great",
            },
            "correct_letter": "C",
        },
        {
            "question_text": "The Cold War was mainly between the USA and:",
            "options": {
                "A": "Germany",
                "B": "China",
                "C": "Japan",
                "D": "Soviet Union",
            },
            "correct_letter": "D",
        },
        {
            "question_text": "Which event is often associated with the start of World War I?",
            "options": {
                "A": "Titanic sinking",
                "B": "Assassination of Archduke Franz Ferdinand",
                "C": "The Boston Tea Party",
                "D": "The fall of the Berlin Wall",
            },
            "correct_letter": "B",
        },
    ]

    # General Knowledge Questions
    question_bank["General Knowledge"] = [
        {
            "question_text": "What is the capital of France?",
            "options": {"A": "Rome", "B": "Madrid", "C": "Paris", "D": "Berlin"},
            "correct_letter": "C",
        },
        {
            "question_text": "How many continents are there on Earth?",
            "options": {"A": "10", "B": "6", "C": "7", "D": "8"},
            "correct_letter": "C",
        },
        {
            "question_text": "Water freezes at what temperature in Celsius?",
            "options": {"A": "0°C", "B": "10°C", "C": "32°C", "D": "100°C"},
            "correct_letter": "A",
        },
        {
            "question_text": "Which planet is known as the Red Planet?",
            "options": {"A": "Venus", "B": "Mars", "C": "Jupiter", "D": "Saturn"},
            "correct_letter": "B",
        },
        {
            "question_text": "Which ocean is the largest?",
            "options": {"A": "Atlantic", "B": "Indian", "C": "Arctic", "D": "Pacific"},
            "correct_letter": "D",
        },
        {
            "question_text": "What is the chemical symbol for gold?",
            "options": {"A": "Ag", "B": "Au", "C": "Gd", "D": "Go"},
            "correct_letter": "B",
        },
        {
            "question_text": "How many days are in a leap year?",
            "options": {"A": "322", "B": "365", "C": "366", "D": "367"},
            "correct_letter": "C",
        },
        {
            "question_text": "Which animal is the largest mammal?",
            "options": {
                "A": "African elephant",
                "B": "Blue whale",
                "C": "Rhino",
                "D": "Great white shark",
            },
            "correct_letter": "B",
        },
        {
            "question_text": "What is the primary language spoken in Brazil?",
            "options": {"A": "Yoruba", "B": "Portuguese", "C": "French", "D": "English"},
            "correct_letter": "B",
        },
        {
            "question_text": "Which instrument has 88 keys (typically)?",
            "options": {"A": "Guitar", "B": "Violin", "C": "Piano", "D": "Flute"},
            "correct_letter": "C",
        },
    ]

    # Coding Questions
    question_bank["Coding"] = [
        {
            "question_text": "In most programming languages, what does a variable do?",
            "options": {
                "A": "Stores data values",
                "B": "Prints text automatically",
                "C": "Deletes files",
                "D": "Turns code into hardware",
            },
            "correct_letter": "A",
        },
        {
            "question_text": "Which of these is an example of a loop?",
            "options": {"A": "IF statement", "B": "FOR loop", "C": "Comment line", "D": "Constant"},
            "correct_letter": "B",
        },
        {
            "question_text": "Which symbol is commonly used for “not equal to” in many languages?",
            "options": {"A": "==", "B": "!=", "C": "=.", "D": ":="},
            "correct_letter": "B",
        },
        {
            "question_text": "What does “HTTP” stand for?",
            "options": {
                "A": "HyperText Transfer Protocol",
                "B": "HighText Transfer Program",
                "C": "HyperTool Text Process",
                "D": "Hyper Transfer Text Package",
            },
            "correct_letter": "A",
        },
        {
            "question_text": "Which data type is best for storing True/False values?",
            "options": {"A": "Integer", "B": "String", "C": "Boolean", "D": "Float"},
            "correct_letter": "C",
        },
        {
            "question_text": "What is the purpose of an “if” statement?",
            "options": {
                "A": "Repeat code forever",
                "B": "Make decisions based on a condition",
                "C": "Store a list of items",
                "D": "Draw a flowchart",
            },
            "correct_letter": "B",
        },
        {
            "question_text": "In Python, which keyword is used to define a function?",
            "options": {"A": "func", "B": "define", "C": "def", "D": "function"},
            "correct_letter": "C",
        },
        {
            "question_text": "What does “IDE” stand for?",
            "options": {
                "A": "Integrated Development Environment",
                "B": "Internal Data Engine",
                "C": "Integrated Design Editor",
                "D": "Internet Development Extension",
            },
            "correct_letter": "A",
        },
        {
            "question_text": "Which of these is a valid example of a comment?",
            "options": {"A": "-- comment", "B": "// comment", "C": "** comment **", "D": "\\\\ comment"},
            "correct_letter": "B",
        },
        {
            "question_text": "What is debugging?",
            "options": {
                "A": "Writing code faster",
                "B": "Removing errors from a program",
                "C": "Encrypting data",
                "D": "Compressing files",
            },
            "correct_letter": "B",
        },
    ]

    # Bible Questions
    question_bank["Bible"] = [
        {
            "question_text": "Who built the ark?",
            "options": {"A": "Moses", "B": "Noah", "C": "David", "D": "Abraham"},
            "correct_letter": "B",
        },
        {
            "question_text": "Jesus was born in which town?",
            "options": {"A": "Nazareth", "B": "Jerusalem", "C": "Bethlehem", "D": "Jericho"},
            "correct_letter": "C",
        },
        {
            "question_text": "How many days and nights did it rain during the flood?",
            "options": {"A": "7", "B": "20", "C": "40", "D": "100"},
            "correct_letter": "C",
        },
        {
            "question_text": "Who led the Israelites out of Egypt?",
            "options": {"A": "Joshua", "B": "Moses", "C": "Solomon", "D": "Isaiah"},
            "correct_letter": "B",
        },
        {
            "question_text": "What is the first book of the Bible?",
            "options": {"A": "Exodus", "B": "Psalms", "C": "Matthew", "D": "Genesis"},
            "correct_letter": "D",
        },
        {
            "question_text": "Who was swallowed by a great fish?",
            "options": {"A": "Jonah", "B": "Peter", "C": "Paul", "D": "Elijah"},
            "correct_letter": "A",
        },
        {
            "question_text": "Which disciple betrayed Jesus?",
            "options": {"A": "John", "B": "Judas Iscariot", "C": "Andrew", "D": "Thomas"},
            "correct_letter": "B",
        },
        {
            "question_text": "The Ten Commandments were given on which mountain?",
            "options": {"A": "Mount Carmel", "B": "Mount Sinai", "C": "Mount Olive", "D": "Mount Ararat"},
            "correct_letter": "B",
        },
        {
            "question_text": "Who defeated Goliath?",
            "options": {"A": "Saul", "B": "Samson", "C": "David", "D": "Solomon"},
            "correct_letter": "C",
        },
        {
            "question_text": "The Lord’s Prayer is found in which part of the Bible?",
            "options": {"A": "The Gospels", "B": "Proverbs", "C": "Revelation", "D": "Genesis"},
            "correct_letter": "A",
        },
    ]

    return question_bank


def build_topic_quiz(question_bank, selected_topic):
    quiz_questions = question_bank[selected_topic]
    return quiz_questions


def run_quiz(quiz_questions):
    user_answers = []
    question_number = 0

    while question_number < 10:
        print("\nQuestion", question_number + 1)
        print(quiz_questions[question_number]["question_text"])
        print("A)", quiz_questions[question_number]["options"]["A"])
        print("B)", quiz_questions[question_number]["options"]["B"])
        print("C)", quiz_questions[question_number]["options"]["C"])
        print("D)", quiz_questions[question_number]["options"]["D"])

        valid_answer = False
        while not valid_answer:
            answer = input("Enter your answer: ").upper()
            if answer in ["A", "B", "C", "D"]:
                valid_answer = True
            else:
                print("Invalid input, pls answer again")

        user_answers.append(answer)
        question_number += 1

    return user_answers



#####MARK AND DISPLAY RESULT RIGHT HERE




print("Welcome to my quiz!")
print("You will pick from 4 topics and answer the 10 questions.")
print("You will get the correct answers and what you scored at the end of the quiz.")
print("Enter A, B, C, or D for each question.")

question_bank = initialise_question_bank()

valid_topic = False
while not valid_topic:
    print("\nChoose a topic:")
    print("1. History")
    print("2. General Knowledge")
    print("3. Coding")
    print("4. Bible")

    topic_choice = input("Enter your choice: ")

    if topic_choice == "1":
        selected_topic = "History"
        valid_topic = True
    elif topic_choice == "2":
        selected_topic = "General Knowledge"
        valid_topic = True
    elif topic_choice == "3":
        selected_topic = "Coding"
        valid_topic = True
    elif topic_choice == "4":
        selected_topic = "Bible"
        valid_topic = True
    else:
        print("Invalid choice, enter your choice again")

quiz_questions = build_topic_quiz(question_bank, selected_topic)
user_answers = run_quiz(quiz_questions)
#mark_and_display_results(quiz_questions, user_answers)

play_again = input("Do you want to play again? (Y/N): ").upper()
while play_again != "Y" and play_again != "N":
    print("Invalid input. Enter Y or N.")
    play_again = input("Do you want to play again? (Y/N): ").upper()

if play_again == "Y":
    print("Restart the program to play again.")
else:
    print("Thank you for playing!")



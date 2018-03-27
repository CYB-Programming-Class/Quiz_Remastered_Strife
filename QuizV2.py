from Question import Question
print("ALL ANSWERS MUST BE LOWER-CASE!!!\n Theme: Imagine Dragons.\n\n")

Easy_Questions = [
    "I'm waking up, I feel it in my bones\nEnough to make my system blow\nWelcome to the new age, to the new age\n"
    "Welcome to the new age, to the new age\nWhoa, oh, oh, oh, oh, whoa, oh, oh, oh, I'm ________\n(a) Dead\n(b) Old\n"
    "(c) Pymaster\n(d) Radioactive\n\n",
    "I don't ever wanna let you down\nI don't ever wanna leave this town\n'Cause after all\nThis city never sleeps at n"
    "ight\n(a) It's Time\n(b) Higher\n(c) America\n(d) Thief\n\n",
    "Here we are.\nDon't turn away now (don't turn away)\nWe are the _______ that built this town.\n(a) Underdogs\n(b) "
    "Workers\n(c) Warriors\n(d) People\n\n ",
    "Kids were laughing in my classes\nWhile I was scheming for the masses\nWho do you think you are?\nDreaming 'bout b"
    "eing a big star\n(a) Rise Up\n(b) Thunder\n(c) Panda\n(d) Mock Me\n\n",
    "When the days are cold\nAnd the cards all fold\nAnd the saints we see\nAre all made of gold\n(a) Demons\n(b) Greed"
    "\n(c) Gold\n(d) Money\n\n",
]
Hard_Questions = [
    "____, I got my head on aright\nI got my people strapped tight\nI got my head on aright\noh oh oh oh\nI, I got my h"
    "ead on aright\nI got my people strapped tight\nI got my head on aright\noh oh oh oh\n(a) Hello\n(b) Walk on\n(c) I"
    "\n(d) Drive\n\n",
    "In the morning light let my roots take flight\nWatch me fall above like a vicious dove\nThey don't see me come, wh"
    "o can blame them?\nThey never seem to catch my eye but I've never wondered why\nEnter the song name: \n\n",
    "When the ____ is nigh\nAnd ________ is sinking in\nAnd the wolves all cry\nTo fill the night with hollering\nFill "
    "in the blanks(Separate the different answers with a comma.): \n\n",
    "All that I've known\nBuildings of stone\nFall to the ground\nWithout a sound\nThis is my word\nHeart breaker, gate"
    "keeper\nI'm feeling far away, I'm feeling right there\n(a) Fake\n(b) False\n(c) Illusion\n(d) None of the above\n"
    "\n",
    "Oh, how did it come to this?\nOh, love is a _______\nBetter in picture\nBut never can fill the void\nFill in the B"
    "lank: \n\n",
]
Impossible_Questions = [
    "Take a look inside\nI've got nothing to hide\nOh no\nI'll beat around the bush\nI've got nothing but time\nOh no o"
    "h no\nEnter the name of the song: \n\n",
    "Nobody can save me now\nThe king is crowned\nIt's do or die\nNobody can save me now\nEnter the name of the song: "
    "\n\n",
    "______ seems to be the worst of all my friends\nShe brings in all the darkness when the year, it just begins\nBut "
    "oh it seems so cold at the strangest of times\nLoneliness, it seems to be the worst of all her crimes\nAnd I'm alr"
    "ight\nIt's alright\nFill in the blank: \n\n",
    "If you ever want to join me baby I'll __ _______ __ ___ ____\nFill in the blanks(Separate different answers with "
    "a comma): \n\n",
    "Come out, I'm waiting on your front porch\nYou came in through the back door\nWe drift along the flooded sea of mu"
    "ddy waters\nClouds above us crying tears of ____\nFill in the blank: \n\n",
]
e_questions = [
    Question(Easy_Questions[0], "d"),
    Question(Easy_Questions[1], "a"),
    Question(Easy_Questions[2], "c"),
    Question(Easy_Questions[3], "b"),
    Question(Easy_Questions[4], "a"),
]
h_questions = [
    Question(Hard_Questions[0], "d"),
    Question(Hard_Questions[1], "tiptoe"),
    Question(Hard_Questions[2], "hour,hopelessness"),
    Question(Hard_Questions[3], "d"),
    Question(Hard_Questions[4], "polaroid"),
]
i_questions = [
    Question(Impossible_Questions[0], "leave me"),
    Question(Impossible_Questions[1], "battle cry"),
    Question(Impossible_Questions[2], "february"),
    Question(Impossible_Questions[3], "be,dancing,in,the,dark"),
    Question(Impossible_Questions[4], "sins"),
]


def run_test(questions):
    """ loops through a list of questions and asks each one"""
    score = 0
    for question in questions:
        valid_input = False
        # ask question until a valid input has come through
        while valid_input == False:
            answer = input(question.prompt)
            # check if answer is correct
            if answer == question.answer:
                score += 1
            # check if answer is valid
            if answer != "a" and answer != "b" and answer != "c" and answer != "d":
                print("Not a valid answer. Use a, b, c, or d to answer the question.")
            else:
                valid_input = True  # if valid answer was given, exit loop
    print("You Got " + str(score) + "/" + str(len(questions)) + " correct on the easy quiz!")
    if score == 0:
        print("This is a joke right? No one could possibly be THIS bad.")
    if score == 1:
        print("Pffft My grandmother could do better.")
    if score == 2:
        print("Your a failure. Complete failure.")
    if score == 3:
        print("Study and take this quiz again.")
    if score == 4:
        print("Nice Job!")
    if score == 5:
        print("PeRfEcT ScOrE!")


run_test(e_questions)


def run_test2(questions):
    """ loops through a list of questions and asks each one"""
    score = 0
    for question in questions:
        valid_input = False
        # ask question until a valid input has come through
        while valid_input == False:
            answer = input(question.prompt)
            # check if answer is correct
            if answer == question.answer:
                score += 1
            # check if answer is valid
            if questions.index(question) == 0 or questions.index(question) == 3:
                if answer != "a" and answer != "b" and answer != "c" and answer != "d":
                    print("Not a valid answer. Use a, b, c, or d to answer the question.\n")
                else:
                    valid_input = True
            else:
                valid_input = True  # if valid answer was given, exit loop
    print("You Got " + str(score) + "/" + str(len(questions)) + " correct on the hard quiz!")
    if score == 0:
        print("This is a joke right? No one could possibly be THIS bad.")
    if score == 1:
        print("Pffft My grandmother could do better.")
    if score == 2:
        print("Your a failure. Complete failure.")
    if score == 3:
        print("Study and take this quiz again.")
    if score == 4:
        print("Nice Job!")
    if score == 5:
        print("PeRfEcT ScOrE!")


if input("Would you like to take the Hard Quiz next?: ") == "yes":
    run_test2(h_questions)
else:
    exit()


def run_test3(questions):
    """ loops through a list of questions and asks each one"""
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You Got " + str(score) + "/" + str(len(questions)) + " correct on the hard quiz!")
    if score == 0:
        print("This is a joke right? No one could possibly be THIS bad.")
    if score == 1:
        print("Pffft My grandmother could do better.")
    if score == 2:
        print("Your a failure. Complete failure.")
    if score == 3:
        print("Study and take this quiz again.")
    if score == 4:
        print("Nice Job!")
    if score == 5:
        print("PeRfEcT ScOrE!")


if input("Would you like to take the Impossible Quiz next?: ") == "yes":
    run_test3(i_questions)
else:
    exit()


# The paragraphs with blanks and their corresponding answers:
paragraph_easy = "A ___1___ starts with a ___2___ character (#) that is not part of a string literal, and ___3___ at the end of the physical line. A ___4___ signifies the end of the logical line unless the implicit line joining rules are invoked. They are ___5___ by the syntax; the computer will not read them."
answers_easy = ["comment", "hash", "ends", "comment", "ignored"]

paragraph_medium = "___1___ are Python's abstraction for data. All data in a ___2___ program is represented by objects or by relations between objects. Every object has an identity, a type and a ___3___ . An object's identity ___4___ ___5___ once it has been created. You may think of it as the object's address in memory."
answers_medium = ["Objects", "Python", "value", "never", "changes"]

paragraph_hard = "The items of a ___1___ are arbitrary Python ___2___ . ___3___ are formed by placing a ___4___ -separated list of expressions in ___5___ brackets."
answers_hard = ["list", "objects", "Lists", "comma", "square"]

welcome_message = "\nWelcome to Guess-The-Word!"
print (welcome_message)

def level_selection():
    """Prompt the user for to select a difficulty level and loads the data.
        Inputs:
            none
        Outputs:
            paragraph with blanks in list type
            answer to the blanks
            level"""
    level = raw_input("\nPlease select your level (Easy / Medium / Hard): ")
    if level.lower() == "easy":
        return paragraph_easy.split(" "), answers_easy, "easy"
    if level.lower() == "medium":
        return paragraph_medium.split(" "), answers_medium, "medium"
    if level.lower() == "hard":
        return paragraph_hard.split(" "), answers_hard, "hard"
    else:
        print "You have selected an invalid difficulty level!"
        return level_selection()

def correct_paragraph(joined_paragraph):
    """Cleans up the paragraph from extra space that are created by join the list's elements in the paragraph.
       Inputs:
            joined_paragraph: initial result of using .join() function
        Outputs:
            joined_paragraph: updated paragraph that has been cleaned up from extra spaces"""
    joined_paragraph = joined_paragraph.replace(" .", ".")
    return joined_paragraph

def check_answer(blank_number, paragraph, list_answers, answer, i):
    """Prompts user to guess the word to replace the blank.
    If it is correct, the blank will be updated with the correct answer.
    Prompt for the next blank will be displayed.
    If it is incorrect, the user will be prompted to try to guess again until s/he run out of remaining attempt.
    Once the user has no more attempt, the game will be over and closed.

    Input:
        blank_number: the current blank number in play
        paragraph: lastest version of the paragraph relevant to game progress
        list_answers: the list containing answers for all the blanks
        answer: the answer to the current blank in play
        initial number of tries: number of attempts that is chosen by the user
    Output:
        the next blank number
        the next remaining attemp number"""

    current_blank_in_play = "___" + str(blank_number) + "___"
    guess = raw_input("\nThe best replacement word for ___" + str(blank_number) + "___ is: ")
    while i != 0:
        if guess != answer:
            print "It's an incorrect answer. Please try again."
            print "\nRemaining attempt(s): " + str(i) + "\n"
            i = i - 1
            return check_answer(blank_number, paragraph, list_answers, answer,i)
        else:
            paragraph[paragraph.index(current_blank_in_play)] = answer
            print correct_paragraph("\n" + " ".join(paragraph)) + "\n"
            blank_number += 1
            return blank_number
    else:
        print "Sorry, it's a game over! Please restart the game."
        return exit()

def open_gtw():
    """Open the game of Guess-The-Words!
    The users will be provided a fill-in-the-blanks paragraph according to the selected level,
    and will be prompted to provide replacement words for the blanks.
    At the start of the game, the user needs to select a level of difficulty and
    in how many tries s/he would be able to solve it.
    Once all the blanks are filled, a congratulations statement will be printed.
    If remaining attempt turns into 0 before they can solve all the blanks, the game will be over and closed.
    Inputs:
        none
    Outputs:
        none"""
    paragraph, list_answers, level = level_selection()
    number_of_tries = raw_input("How many tries do you think you need to solve it? ")
    i = int(number_of_tries) - 1
    print ("\nSelected level: " + level +
            "\nNumber of attempt(s): " + number_of_tries + "\n"
            "\nProvide a word to replace the following blanks."
            "\nPlease note that the answers are case_sensitive and must be gramatically correct.\n")
    print correct_paragraph(" ".join(paragraph)) + "\n"

    blank_number = 1
    for answer in list_answers:
        blank_number = check_answer(blank_number, paragraph, list_answers, answer,i)
    print ("Congratulation! You have solved this round. Come back anytime to try some more!")

open_gtw ()

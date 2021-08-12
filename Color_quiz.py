# Eva Dye
# August 11th, 2021
# Python 2.7
# Python program for a color guess game.

# Possible answers library
negative_answers = ["No", "no", "N", "n"]
positive_answers = ["Yes", "yes", "Y", "y"]
color_answers = ["Red", "red", "Orange", "orange", "Yellow", "yellow"]

# Message library
victory_message = "Woo-hoo! Thanks for playing!"
defeat_message = "Drat. I need to study the color wheel better..."


def opening():
    print "Let's play a color game! Think of a 'Warm' Color, and I'll try to guess it!"
    print "Remember, 'Warm' colors on the color wheel are Red, Orange, and Yellow."
    answer_one = raw_input("Have you thought of a color? ").lower()
    if answer_one in positive_answers:
        print "Awesome! Let's get started."
    elif answer_one in negative_answers:
        print "That's okay, maybe next time."
    else:
        print "I'm sorry, I didn't quite get that."


opening()


# Note for later: indent questions per color to form an answer path to get to a specific result
# Once 'cool' category is introduced, indent 'warm' and 'cool' colors together to stay organized
# Future goal: figure out how to loop back to question if wrong input is given


def game():
    question_one = raw_input("Is your color a primary color? ")
    if question_one in positive_answers:
        # 'Red' answer path
        question_two = raw_input("Can your color be used to make purple? ")
        if question_two in positive_answers:
            question_three = raw_input("Is your color red? ")
            if question_three in positive_answers:
                print victory_message
            elif question_three in negative_answers:
                end_question_red = raw_input("What was your color? ")
                if end_question_red in color_answers:
                    print defeat_message
        # 'Yellow' answer path
        elif question_two in negative_answers:
            question_four = raw_input("Can your color be used to make green? ")
            if question_four in positive_answers:
                question_five = raw_input("Is your color yellow? ")
                if question_five in positive_answers:
                    print victory_message
            elif question_four in negative_answers:
                end_question_yellow = raw_input("What was your color? ")
                if end_question_yellow in color_answers:
                    print defeat_message
    # Orange answer path
    elif question_one in negative_answers:
        question_six = raw_input("Is your color also a fruit? ")
        if question_six in positive_answers:
            question_seven = raw_input("Is your color orange? ")
            if question_seven in positive_answers:
                print victory_message
        elif question_six in negative_answers:
            end_question_orange = raw_input("What was your color? ")
            if end_question_orange in color_answers:
                print defeat_message


game()

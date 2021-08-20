# Eva Dye
# August 12th, 2021
# Python 2.7
# Python program for a color guess game.

# Possible answers library
negative_answers = ["No", "no", "N", "n"]
positive_answers = ["Yes", "yes", "Y", "y"]
color_answers = ["Red", "red", "Orange", "orange", "Yellow", "yellow", "Green", "green", "Blue", "blue", "Indigo",
                 "indigo", "Purple", "purple"]
question_answers = positive_answers + negative_answers

# Message library
victory_message = "Woo-hoo! Aren't colors wonderful?"
defeat_message = "Drat. I need to study the color wheel better..."


def opening():
    print "Let's play a color game! Think of a 'Warm' or 'Cool' Color, and I'll try to guess it!"
    print "Remember, 'Warm' colors on the color wheel are Red, Orange, and Yellow."
    print "And 'Cool' colors on the color wheel are Green, Blue, Indigo, and Purple."
    print "It's ROY G. BIP!"
    answer_one = raw_input("Have you thought of a color? ").lower()
    if answer_one in positive_answers:
        print "Awesome! Let's get started."
    elif answer_one in negative_answers:
        print "That's okay, maybe next time."
    else:
        print "I'm sorry, I didn't quite get that."


opening()


# Future goal: figure out how to loop back to question if wrong input is given


def game():
    starting_question = raw_input("Is your color a warm color? ")
    # Warm colors answer tree
    if starting_question in positive_answers:
        warm_question_one = raw_input("Is your color a primary color? ")
        if warm_question_one in positive_answers:
            # 'Red' answer path
            warm_question_two = raw_input("Can your color be used to make purple? ")
            if warm_question_two in positive_answers:
                warm_question_three = raw_input("Is your color red? ")
                if warm_question_three in positive_answers:
                    print victory_message
                elif warm_question_three in negative_answers:
                    end_question_red = raw_input("What was your color? ")
                    if end_question_red in color_answers:
                        print defeat_message
            # 'Yellow' answer path
            elif warm_question_two in negative_answers:
                warm_question_four = raw_input("Can your color be used to make green? ")
                if warm_question_four in positive_answers:
                    warm_question_five = raw_input("Is your color yellow? ")
                    if warm_question_five in positive_answers:
                        print victory_message
                elif warm_question_four in negative_answers:
                    end_question_yellow = raw_input("What was your color? ")
                    if end_question_yellow in color_answers:
                        print defeat_message
        # Orange answer path
        elif warm_question_one in negative_answers:
            warm_question_six = raw_input("Is your color also a fruit? ")
            if warm_question_six in positive_answers:
                warm_question_seven = raw_input("Is your color orange? ")
                if warm_question_seven in positive_answers:
                    print victory_message
            elif warm_question_six in negative_answers:
                end_question_orange = raw_input("What was your color? ")
                if end_question_orange in color_answers:
                    print defeat_message
    # Cool colors answer tree
    elif starting_question in negative_answers:
        cool_question_one = raw_input("Is your color a cool color? ")
        if cool_question_one in positive_answers:
            cool_question_two = raw_input("Is your color a primary color? ")
            if cool_question_two in positive_answers:
                # 'Blue' answer path
                cool_question_three = raw_input("Can your color be used to make purple? ")
                if cool_question_three in positive_answers:
                    cool_question_four = raw_input("Is your color blue? ")
                    if cool_question_four in positive_answers:
                        print victory_message
                    elif cool_question_four in negative_answers:
                        end_question_blue = raw_input("What was your color? ")
                        if end_question_blue in color_answers:
                            print defeat_message
            # Green answer path
            elif cool_question_two in negative_answers:
                cool_question_five = raw_input("Is your color the same color as grass? ")
                if cool_question_five in positive_answers:
                    cool_question_six = raw_input("Is your color green? ")
                    if cool_question_six in positive_answers:
                        print victory_message
                    elif cool_question_six in negative_answers:
                        end_question_green = raw_input("What was your color? ")
                        if end_question_green in color_answers:
                            print defeat_message
                # Indigo answer path
                elif cool_question_five in negative_answers:
                    cool_question_eight = raw_input("Is your color often mistaken for blue or purple? ")
                    if cool_question_eight in positive_answers:
                        cool_question_nine = raw_input("Is your color indigo? ")
                        if cool_question_nine in positive_answers:
                            print victory_message
                        elif cool_question_nine in negative_answers:
                            end_question_indigo = raw_input("What was your color? ")
                            if end_question_indigo in color_answers:
                                print defeat_message
                    # Purple answer path
                    elif cool_question_eight in negative_answers:
                        cool_question_ten = raw_input("Is your color the same color as an eggplant? ")
                        if cool_question_ten in positive_answers:
                            cool_question_eleven = raw_input("Is your color purple? ")
                            if cool_question_eleven in positive_answers:
                                print victory_message
                        elif cool_question_ten in negative_answers:
                            end_question_purple = raw_input("What was your color? ")
                            if end_question_purple in color_answers:
                                print defeat_message


game()


def play_again():
    while True:
        answer = raw_input("Would you like to play again? ")
        if answer in negative_answers:
            print "Thanks for playing!"
            exit()
        elif answer in positive_answers:
            print "Awesome!"
            return game()
        elif answer not in question_answers:
            print "Please enter valid input."
            return play_again()

play_again()

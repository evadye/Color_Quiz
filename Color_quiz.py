# Eva Dye
# August 11th, 2021
# Python 2.7
# Python program for a color guess game.

# Possible answers library
negative_answers = ["No", "no", "N", "n"]
positive_answers = ["Yes", "yes", "Y", "y"]
color_answers = ["Red", "red", "Orange", "orange", "Yellow", "yellow", "Green", "green", "Blue", "blue", "Indigo",
                 "indigo", "Purple", "purple"]
question_answers = positive_answers + negative_answers

# Message library
victory_message = "Woo-hoo! Thanks for playing!"
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
    while True:
        # Warm colors answer tree
        if starting_question in positive_answers:
            def warm_question_1():
                warm_question_one = raw_input("Is your color a primary color? ")
                while True:
                    if warm_question_one in positive_answers:
                        # 'Red' answer path
                        def warm_question_2():
                            warm_question_two = raw_input("Can your color be used to make purple? ")
                            while True:
                                if warm_question_two in positive_answers:
                                    def warm_question_3():
                                        warm_question_three = raw_input("Is your color red? ")
                                        while True:
                                            if warm_question_three in positive_answers:
                                                print victory_message
                                            elif warm_question_three in negative_answers:
                                                def end_question_r():
                                                    end_question_red = raw_input("What was your color? ")
                                                    while True:
                                                        if end_question_red in color_answers:
                                                            print defeat_message
                                                        elif end_question_red not in color_answers:
                                                            print "Please enter a ROY G BIV color."
                                                            return end_question_r()
                                            elif warm_question_three not in question_answers:
                                                print "Please enter valid input."
                                                return warm_question_3()
                                # 'Yellow' answer path
                                elif warm_question_two in negative_answers:
                                    def warm_question_4():
                                        warm_question_four = raw_input("Can your color be used to make green? ")
                                        while True:
                                            if warm_question_four in positive_answers:
                                                def warm_question_5():
                                                    warm_question_five = raw_input("Is your color yellow? ")
                                                    while True:
                                                        if warm_question_five in positive_answers:
                                                            print victory_message
                                                        elif warm_question_five in negative_answers:
                                                            def end_question_y():
                                                                end_question_yellow = raw_input("What was your color? ")
                                                                while True:
                                                                    if end_question_yellow in color_answers:
                                                                        print defeat_message
                                                                    elif end_question_yellow not in color_answers:
                                                                        print "Please enter a ROY G BIV color."
                                                                        return end_question_y()
                                                        else:
                                                            print "Invalid input."
                                                            return warm_question_5()
                                            elif warm_question_four in negative_answers:
                                                def end_question_y2():
                                                    end_question_yellow = raw_input("What was your color? ")
                                                    while True:
                                                        if end_question_yellow in color_answers:
                                                            print defeat_message
                                                        elif end_question_yellow not in color_answers:
                                                            print "Invalid input. Please enter a ROY G BIV color."
                                                            return end_question_y2()
                                            else:
                                                print "Invalid input."
                                                return warm_question_4()
                                else:
                                    print "Invalid input."
                                    return warm_question_2()
                # Orange answer path
                    elif warm_question_one in negative_answers:
                        def warm_question_6():
                            warm_question_six = raw_input("Is your color also a fruit? ")
                            while True:
                                if warm_question_six in positive_answers:
                                    def warm_question_7():
                                        warm_question_seven = raw_input("Is your color orange? ")
                                        while True:
                                            if warm_question_seven in positive_answers:
                                                print victory_message
                                            elif warm_question_seven in negative_answers:
                                                def end_question_o():
                                                    end_question_orange = raw_input("What was your color? ")
                                                    while True:
                                                        if end_question_orange in color_answers:
                                                            print defeat_message
                                                        elif end_question_orange not in color_answers:
                                                            print "Invalid input. Please enter a ROY G BIV color."
                                                            return end_question_o()
                                            else:
                                                print "Invalid input."
                                                return warm_question_7()
                                elif warm_question_six in negative_answers:
                                    def end_question_o2():
                                        end_question_orange = raw_input("What was your color? ")
                                        while True:
                                            if end_question_orange in color_answers:
                                                print defeat_message
                                            elif end_question_orange not in color_answers:
                                                print "Invalid input. Please enter a ROY G BIV color."
                                                return end_question_o2()
                                else:
                                    print "Invalid input."
                                    return warm_question_6()
                    else:
                        print "Invalid input."
                        return warm_question_1()


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

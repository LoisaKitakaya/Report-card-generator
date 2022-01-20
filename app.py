from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import numpy as np
import time
import os

# student class
class Student:

    # class initialization
    def __init__(self, first_name, last_name):
        
        self.first_name = first_name
        self.last_name = last_name
        self.object = 'The student'

    # print student name function
    def print_name(self):

        # clearing the screen
        if os.name == 'posix':

            _ = os.system('clear')

        else:

            _ = os.system('cls')

        record_added_time = datetime.now()

        print('Records for ' + self.object.lower() + ': ' + self.first_name + ' ' + self.last_name + ' have been added successfully')

        print('Action timestamp: ', record_added_time)

        print('\n')

# grades class
class Grades(Student):

    # class initialization
    def __init__(self, first_name, last_name, science, math, language, music, history, geography, art):

        super().__init__(first_name, last_name)

        self.science = science
        self.math = math
        self.language = language
        self.music = music
        self.history = history
        self.geography = geography
        self.art = art

    # grade subject and overall performance
    def get_grades(self):

        score_dict = {
            'Science' : self.science,
            'Math' : self.math,
            'Language' : self.language,
            'Music' : self.music,
            'History' : self.history,
            'Geography' : self.geography,
            'Art' : self.art
        }

        score_list = [
            self.science,
            self.math,
            self.language,
            self.music,
            self.history,
            self.geography,
            self.art
        ]

        # clearing the screen
        if os.name == 'posix':

            _ = os.system('clear')

        else:

            _ = os.system('cls')

        # grade performance in each subject
        for name, score in score_dict.items():

            if score <= 20:

                print(self.first_name + ' got an "E" in ' + name)

                print('\n')

            elif score <= 40:

                print(self.first_name + ' got a "D" in ' + name)

                print('\n')

            elif score <= 60:

                print(self.first_name + ' got a "C" in ' + name)

                print('\n')

            elif score <= 80:

                print(self.first_name + ' got a "B" in ' + name)

                print('\n')

            elif score <= 100:

                print(self.first_name + ' got an "A" in ' + name)

                print('\n')

            else:

                print('Invalid score! Subject: ' + name)

                print('\n')

        # grade overall performance
        mean_score = np.mean(score_list)

        if mean_score <= 20:

            print(self.first_name + ' has a mean score of: ', mean_score)
            print(self.first_name + ' has a mean grade of: "E".')
            
            print('\n')

        elif mean_score <= 40:

            print(self.first_name + ' has a mean score of: ', mean_score)
            print(self.first_name + ' has a mean grade of: "D".')

            print('\n')

        elif mean_score <= 60:

            print(self.first_name + ' has a mean score of: ', mean_score)
            print(self.first_name + ' has a mean grade of: "C".')

            print('\n')

        elif mean_score <= 80:

            print(self.first_name + ' has a mean score of: ', mean_score)
            print(self.first_name + ' has a mean grade of: "B".')

            print('\n')

        elif mean_score <= 100:

            print(self.first_name + ' has a mean score of: ', mean_score)
            print(self.first_name + ' has a mean grade of: "A".')

            print('\n')

        else:

            print(mean_score, 'is invalid, hence, cannot be graded!')

            print('\n')

    # visualize student performance statistics
    def visualize_data(self):

        # clearing the screen
        if os.name == 'posix':

            _ = os.system('clear')

        else:

            _ = os.system('cls')

        performance_dataset = {
            'Subject' : [
                'Science',
                'Math',
                'Language',
                'Music',
                'History',
                'Geography',
                'Art'
            ],
            'Score' : [
                self.science,
                self.math,
                self.language,
                self.music,
                self.history,
                self.geography,
                self.art
            ]
        }

        score_board = pd.DataFrame(performance_dataset)

        print('Here is the student score board: ')
        print(score_board)

        print('\n')

        print('This data can also be visualized as "graphs/charts".')

        print('\n')

        print('You can choose between "line (default)", "scattered/dot", "bar", & "pie" charts.')

        print('\n')

        x_axis_data = [
            'Science', 
            'Math', 
            'Language', 
            'Music', 
            'History', 
            'Geography', 
            'Art'
        ]

        y_axis_data = [
            self.science,
            self.math,
            self.language,
            self.music,
            self.history,
            self.geography,
            self.art
        ]

        while True:

            print('| Select "l" for "line graph" | select "s" for "scattered/dot graph" | select "b" for "bar graph" | select "p" for "pie chart" |')

            print('\n')

            visualization_prompt = input('[l]/[s]/[b]/[p]:? ')

            if visualization_prompt == 'l':

                score_board.plot()

                plt.show()

                break

            elif visualization_prompt == 's':

                plt.scatter(x_axis_data, y_axis_data)

                plt.title("Student performance data")

                plt.show()

                break

            elif visualization_prompt == 'b':

                plt.bar(x_axis_data, y_axis_data)

                plt.title("Student performance data")

                plt.show()

                break

            elif visualization_prompt == 'p':

                explode_values = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

                plt.pie(y_axis_data, explode = explode_values, shadow = True, )

                plt.legend(x_axis_data)

                plt.show()

                break

            else:

                print('Invalid option!')
            
                print('\n')

                print('| Select "l" for "line graph" | select "s" for "scattered/dot graph" | select "b" for "bar graph" | select "p" for "pie chart" |')

                print('\n')

    # generate report card
    def generate_report_card(self):

        my_canvas = canvas.Canvas("student_report.pdf")

        height = letter

        top_margin = 830

        left_margin = 72

        report_title = 'Report card for student: ' + self.first_name + ' ' + self.last_name

        score_dict = {
            'Science' : self.science,
            'Math' : self.math,
            'Language' : self.language,
            'Music' : self.music,
            'History' : self.history,
            'Geography' : self.geography,
            'Art' : self.art
        }

        x_axis_data = [
            'Science', 
            'Math', 
            'Language', 
            'Music', 
            'History', 
            'Geography', 
            'Art'
        ]

        y_axis_data = [
            self.science,
            self.math,
            self.language,
            self.music,
            self.history,
            self.geography,
            self.art
        ]

        my_canvas.drawString(left_margin, 800, report_title)

        for score, name in score_dict.items():

            sub_text_1 = str(name)

            sub_text_2 = '..........'

            sub_text_3 = str(score)

            text = sub_text_1 + sub_text_2 + sub_text_3

            my_canvas.drawString(left_margin, top_margin, text)

            top_margin += 20

        plt.bar(x_axis_data, y_axis_data)

        plt.title("Student performance data")

        plt.savefig('my_plot.png')

        image = 'my_plot.png'

        my_canvas.drawImage(image, left_margin, 900)

        my_canvas.showPage()

        my_canvas.save()
    
# main program
if __name__ == "__main__":

    # clearing the screen
    if os.name == 'posix':

        _ = os.system('clear')

    else:

        _ = os.system('cls')

    print('Welcome to Report Card Generator (RCG).')

    print('\n')

    # taking student data
    while True:

        print('Select "1" to analyze student performance and/or generate student report card. | Select "0" to exit program.')

        print('\n')

        first_prompt = input('[1]/[0]:? ')

        print('\n')

        if first_prompt == '0':

            # clearing the screen
            if os.name == 'posix':

                _ = os.system('clear')

            else:

                _ = os.system('cls')

            print('Exiting program...')

            time.sleep(2)

            if os.name == 'posix':

                _ = os.system('clear')

            else:

                _ = os.system('cls')

            print('Thanks for visiting!')

            break

        elif first_prompt == '1':

            # clearing the screen
            if os.name == 'posix':

                _ = os.system('clear')

            else:

                _ = os.system('cls')

            print('Follow the prompts below to generate a student report card.')

            print('\n')

            student_first_name = input('Enter the first name of the student: ')

            student_second_name = input('Enter the second name of the student: ')

            print('\n')

            while True:

                science_score = int(input('Enter science score (out of 100): '))

                if science_score > 100:

                    # clearing the screen
                    if os.name == 'posix':

                        _ = os.system('clear')

                    else:

                        _ = os.system('cls')

                    print('Please enter a score that is out of 100.')

                    print('\n')

                else:

                    break

                print('\n')

            while True:

                math_score = int(input('Enter math score (out of 100): '))

                if math_score > 100:

                    # clearing the screen
                    if os.name == 'posix':

                        _ = os.system('clear')

                    else:

                        _ = os.system('cls')

                    print('Please enter a score that is out of 100.')

                    print('\n')

                else:

                    break

                print('\n')

            while True:

                language_score = int(input('Enter language score (out of 100): '))

                if language_score > 100:

                    # clearing the screen
                    if os.name == 'posix':

                        _ = os.system('clear')

                    else:

                        _ = os.system('cls')

                    print('Please enter a score that is out of 100.')

                    print('\n')

                else:

                    break

                print('\n')

            while True:

                music_score = int(input('Enter music score (out of 100): '))

                if music_score > 100:

                    # clearing the screen
                    if os.name == 'posix':

                        _ = os.system('clear')

                    else:

                        _ = os.system('cls')

                    print('Please enter a score that is out of 100.')

                    print('\n')

                else:

                    break

                print('\n')

            while True:

                history_score = int(input('Enter history score (out of 100): '))

                if history_score > 100:

                    # clearing the screen
                    if os.name == 'posix':

                        _ = os.system('clear')

                    else:

                        _ = os.system('cls')

                    print('Please enter a score that is out of 100.')

                    print('\n')

                else:

                    break

                print('\n')

            while True:

                geography_score = int(input('Enter geography score (out of 100): '))

                if geography_score > 100:

                    # clearing the screen
                    if os.name == 'posix':

                        _ = os.system('clear')

                    else:

                        _ = os.system('cls')

                    print('Please enter a score that is out of 100.')

                    print('\n')

                else:

                    break

                print('\n')

            while True:

                art_score = int(input('Enter art score (out of 100): '))

                if art_score > 100:

                    # clearing the screen
                    if os.name == 'posix':

                        _ = os.system('clear')

                    else:

                        _ = os.system('cls')

                    print('Please enter a score that is out of 100.')

                    print('\n')

                else:

                    break

                print('\n')

            # passing data to functions to perform their operations
            grading_instance = Grades(student_first_name, student_second_name, science_score, math_score, language_score, music_score, history_score, geography_score, art_score)

            grading_instance.print_name()

            print('The following are actions you can perform on the data you have provided:')

            print('\n')

            print('[1]: Grade subject and overall performance')

            print('\n')

            print('[2]: Visualize student performance statistics')

            print('\n')

            print('[3]: Generate report card')

            print('\n')

            while True:

                print('Select "1" to grade subject and overall performance. | Select "2" to visualize student performance statistics. | Select "3" to generate report card.')

                print('\n')

                data_action_prompt = int(input('[1]/[2]/[3]/[select "0" to quit]:? '))

                if data_action_prompt == 0:

                    # clearing the screen
                    if os.name == 'posix':

                        _ = os.system('clear')

                    else:

                        _ = os.system('cls')

                    print('Exiting program...')

                    time.sleep(2)

                    if os.name == 'posix':

                        _ = os.system('clear')

                    else:

                        _ = os.system('cls')

                    print('Thanks for visiting!')

                    break

                if data_action_prompt == 1:

                    time.sleep(2)

                    grading_instance.get_grades()

                    print('\n')

                elif data_action_prompt == 2:

                    time.sleep(2)

                    grading_instance.visualize_data()

                    print('\n')

                elif data_action_prompt == 3:

                    time.sleep(2)

                    grading_instance.generate_report_card()
                    
                    print('\n')

                else:

                    # clearing the screen
                    if os.name == 'posix':

                        _ = os.system('clear')

                    else:

                        _ = os.system('cls')

                    print('Invalid input.')

                    print('\n')

            print('Thanks for using this app. See you again next time.')

            print('\n')

            break

        else:

            # clearing the screen
            if os.name == 'posix':

                _ = os.system('clear')

            else:

                _ = os.system('cls')

            print('Invalid option!')
            
            print('\n')
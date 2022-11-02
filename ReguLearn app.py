# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 20:58:40 2022

@author: akote
"""


# Python program to learn regular expressions
 
from tkinter import *
 
from tkinter import messagebox as mb

from PIL import Image, ImageTk
 
# json file will store questions and answers
import json
 
class Quiz:
  
    # function which is called when object of Quiz class is created
    def __init__(self):
         
        # set question, lesson and slide number to 0
        self.q_no = 0
        self.lesson_no = 0
        self.slide_no = 0
        
        self.radio_list = []
        
        # variable to store selected option
        self.opt_selected = IntVar()
        
        self.display_title()
        self.start_menu()
        
    # function which displays menu: credit and start buttons, menu background
    def start_menu(self):
        
        image1 = Image.open("menu_background.png")
        test = ImageTk.PhotoImage(image1)

        label1 = Label(image=test)
        label1.image = test
        label1.place(x = 0, y = 0)
        
        # start button displays first lesson when clicked
        start_button = Button(gui, text="Start",command=lambda:[self.start_game(), start_button.destroy(), credit_button.destroy(), label1.destroy()],
        width=10, bg="#2E4054", fg="white",font=("ariel",16,"bold"))
         
        # placing the button on the screen
        start_button.place(x=350,y=380)
    
        credit_button = Button(gui, text="Credit",command=lambda:[self.credit_view(), start_button.destroy(), credit_button.destroy()],
        width=10, bg="#2E4054" ,fg="white",font=("ariel",16,"bold"))
         
        # placing the button on the screen
        credit_button.place(x=350,y=330)
        
        

    def credit_view(self):
        credit = Label(gui, text="Created by Adam Kotecki", bg = "#2E4054", fg = "white" , font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
         
        credit.place(x=300, y=200)
        
        start_button = Button(gui, text="Start",command=lambda:[self.start_game(), start_button.destroy(), credit.destroy()],
        width=10, bg ="#2E4054", fg="white",font=("ariel",16,"bold"))
        
        start_button.place(x=350,y=380)
        
        
    def start_game(self):
        
        image2 = Image.open("background.png")
        test2 = ImageTk.PhotoImage(image2)

        label2 = Label(image=test2)
        label2.image = test2
        label2.place(x = 0, y = 0)
        
        self.next_slide()
        
        # displays the next and exit button
        self.buttons()
         
        # number of questions
        self.data_size=len(question)
         
        # counter of correct answers
        self.correct = 0
        
    def display_lesson(self):
        
        if self.lesson_no > 0:
            question_no.destroy()
            
            for widget in self.radio_list:
                widget.destroy()
        
        # list which stores text of the lessons
        lessons = ["Lesson 1. Introduction\n\n \
A regular expression is a sequence of characters that matches the pattern.\n \
The simplest regex consists of a single literal character, such as a. It matches the first occurrence of that character in the given text (string). \
If the string is Adam, it matches the second a, as regexes are case sensitive.\n\n \
Combination of backslash and literal character can create a regex with a special meaning:\n\n \
\d - matches a single digit\n \
\w - matches an alphanumeric character, including _ \n \
\s - matches a whitespace character\n\n \
\D - matches non-digit\n \
\W - non-alphanumeric\n \
\S - non-whitespace\n\n \
There are also special characters that has no literal meaning:\n \
. - dot is like a Joker in card games, it matches any charater" \
, "Lesson 2. Ranges\n\n \
[a-zA-Z] – matches one character from specific range.\n\n \
If you will add ^ as the first character inside bracket, regex will match any character apart from the ones in the range.\n\n \
Below metacharacters can be put after character/group:\n\n \
*- any numer of repetitions\n \
+- at least one repetition\n \
{n} - exactly n repetitions\n \
{m, n} - between m to n repetitions\n \
? – at most one repetition\n \
| - alternation\n\n \
Example. Regex colou?r will match both words: colour and color, as u? matches 0 or 1 occurence of u letter " \
,"Lesson 3. Greedy and non-greedy\n\n \
Let's learn about greedy and non-greedy quantifiers.\n\n \
*, +, and ? are all greedy, meaning they searching for the longest possible match.\n\n \
You can make them non-greedy by adding ? after them, for example: *?, +?, ??. They will give you shortest possible match." \
,"Lesson 4. Anchors\n\n \
Anchors are used to define particular location in the search string where a match must occur. \n\n \
\A - asserts position at start of the string\n \
^ - as above\n\n \
\Z - asserts position at end of the string\n \
$ - as above" \
,"Lesson 5. Boundaries\n\n \
\\b  - assert position at a word boundary\n\n \
Word boundary is one of the following positions:\n\n \
1. Before the first word character in the string.\n \
2. After the last word character in the string.\n \
3. Between word characters separated by not a word character(s)."]
        
        global lesson
        
        # display lesson text based on lesson counter value
        lesson = Label(gui, text=lessons[self.lesson_no], bg = "#2E4054", fg ="white", font=( 'ariel' ,10, 'bold' ), anchor= 'w', wraplength=720, justify = "left") #, wraplength=5  width=60,
        
        # placing the lesson on the screen
        lesson.place(x=70, y=100)
        
        self.lesson_no += 1
        
    # display final results: number of correct and wrong answers
    def display_result(self):
        
        # removing next button from the screen as this is the last slide
        next_button.destroy()
        
        quit_button.place(x = 410, y=350)
        
        # removing last question from the screen
        question_no.destroy()
        
        for widget in self.radio_list:
                widget.destroy()
        import gc
        gc.collect()
        
        # number of wrong and correct answers
        wrong = self.data_size - self.correct
        correct = self.correct
        
        # % of correct answers
        result = int(self.correct / self.data_size * 100)
        
        result_label = Label(gui, text=f"Score: {result}%", bg ="#2E4054", fg = "white", font=( 'ariel' ,16, 'bold' ), anchor= 'w')
        correct_label = Label(gui, text=f"Correct: {correct}", bg ="#2E4054", fg = "white", font=( 'ariel' ,16, 'bold' ), anchor= 'w')
        wrong_label = Label(gui, text=f"Wrong: {wrong}", bg ="#2E4054", fg = "white", font=( 'ariel' ,16, 'bold' ), anchor= 'w')
        
        # placing results on the screen
        result_label.place(x=340,y=150)
        correct_label.place(x=340,y=200)
        wrong_label.place(x=340,y=250)
        
        # display try again button next to quit button
        again_button = Button(gui, text="Try again", command=lambda: [self.TryAgain()], width=8,bg="black", fg="white",font=("ariel",16," bold"))
        again_button.place(x = 280, y=350)
    
    # function to restart the game
    def TryAgain(self):
        gui.destroy()
        game()
        

    # checks if selected answer is correct
    def check_ans(self, q_no):
         
        if self.opt_selected.get() == answer[q_no]:
            # if the answer is correct its return true
            return True
 
    # function to change slide and check if lesson or question should be displayed
    def next_slide(self):
        
        self.slide_no += 1
        
        # check if current slide is a first lesson
        if self.slide_no == 1:
            self.display_lesson()
        
        # check if current slide is lesson
        if self.slide_no in [3, 5, 7, 9]:
            
            # Check if the answer of last question is correct
            if self.check_ans(self.q_no):
            # if the answer is correct
                self.correct += 1
                
            self.q_no += 1
            self.display_lesson()
            
        # if current slide is a question:    
        if self.slide_no in [2, 4, 6, 8, 10]:
            
             lesson.destroy()
             self.display_question()
             self.opts=self.radio_buttons()
             self.display_options()
             
        # if this is the last slide:
        if self.slide_no == 11:
            if self.check_ans(self.q_no):
            # if the answer is correct
                self.correct += 1
            self.display_result()
         
        
            
   # function to place next and quit buttons on screen
    def buttons(self):
        
        global next_button
        global quit_button
         
        # Next button calls next_slide() function 
        next_button = Button(gui, text="Next",command=lambda:[self.next_slide()],
        width=10,bg="#98A2A9",fg="black",font=("ariel",16,"bold"))
         
        # placing the button on the screen
        next_button.place(x=350,y=450)
        
        # Quit button ends game
        quit_button = Button(gui, text="Quit", command=gui.destroy,
        width=5,bg="#CC274C", fg="white",font=("ariel",16," bold"))
         
        quit_button.place(x=700,y=450)
 
    # if current slide is a question, options are displayed
    def display_options(self):
        val=0
         
        # no answer should be initially selected 
        self.opt_selected.set(0)
        
        # text of the available options in current question
        for option in options[self.q_no]:
            self.opts[val]['text']=option
            val+=1
 
 
    # function to display current question
    def display_question(self):
    
        global question_no
        
        # text of label is based on number of current question
        question_no = Label(gui, text=question[self.q_no], bg ="#2E4054", fg = "white",
        font=( 'ariel' ,12, 'bold' ), anchor= 'w' )
         
        # placing the question on the screen
        question_no.place(x=70, y=100)
 
    
    def display_title(self):
         
        title = Label(gui, text="Regulearn",
        width=50, bg="blue",fg="white", font=("ariel", 20, "bold"))
         
        title.place(x=0, y=2)
 
    # if current slide is a question, radio buttons are displayed
    def radio_buttons(self):
        
        # empty list of options
        q_list = []
         
        # position of the first option
        y_pos = 150
         
        # adding the options to the list
        while len(q_list) < 4:
             
            # setting the radio button
            radio_btn = Radiobutton(gui,text=" ",variable=self.opt_selected, bg ="#2E4054", fg = "white", selectcolor='grey',
            value = len(q_list)+1,font = ("ariel",14))
             
            # adding the button to the list
            q_list.append(radio_btn)
             
            # placing the button
            radio_btn.place(x = 100, y = y_pos)
             
            # incrementing position (next radio button will be placed lower)
            y_pos += 40
         
        # return the radio buttons
        self.radio_list = q_list
        return q_list
 

    def clear_frame(self):
       for widgets in frame.winfo_children():
          widgets.destroy() 


# most important function that starts program
def game():
    global gui
    # create a GUI object
    gui = Tk()
     
    # set the size and title of the gui
    gui.geometry("800x500")
    gui.title("Regulearn")
    
    gui.configure(bg = "#2E4054")
    
    frame = Frame(gui)
    frame.pack(side="top", expand=True, fill="both")
    
    # get the data from the json file
    with open('data.json') as f:
        data = json.load(f)
     
    global question
    global options
    global answer
    
    # setting the variables which store questions, options, and answers from json
    question = (data['question'])
    options = (data['options'])
    answer = (data['answer'])
     
    # create an object of the Quiz Class.
    quiz = Quiz()
     
    # starts the GUI
    gui.mainloop()

# starting the program
game()
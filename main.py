from tkinter import *
import random
from PIL import Image, ImageTk

names = []

asked =  []
score=0

def random_questions():
  global qnum 
  qnum = random.randint(1,10)
  if qnum not in asked:
      asked.append(qnum)
  elif qnum in asked:
    random_questions()


class QuizStarter:

  def __init__(self, parent):
 
  
    #users input is taken by an Entry Widget
    self.entry_box=Entry(window)
    self.entry_box.place(x=325, y=210)

  #continue Button
    self.continue_button = Button (window, text="START QUIZ", bg="azure3", command=self.name_collection)
    self.continue_button.place(x=355, y=250)

  def name_collection(self):
    name = self.entry_box.get()
    names.append(names)
    print(names)
    self.entry_box.destroy()
    self.continue_button.destroy()
    image_label.destroy()
    Quiz(window)



class Quiz:
  def __init__(self, parent):
    background_color="darkorange"
    #dictianary has key of number( for each question number) and : the value for each is a list that has 7 items, so index 0 to 6
    self.quiz_collection = {
    1: ["How many players are on the court from each team?", #item 1 index 0 will be the question
        '7 players', #item 2, index 1 will be first choice
        '5 players', #item 3, index 2 will be second choice
        '10 players', #item 4, index 3 will be thrid choice
        '12 players', #item 5, index 4 will be fourth choice
        '5 players', #item 6, index 5 will be the write statement we need to display the right statement if the users enters wrong choice
        2], #item 7,index 6 will be the position of the right answer (index whre right answer sits), this will be out check if answer is correct or not

    2: ["How tall is the average nba player?", #item 1 index 0 will be the question
        '6 foot 8 inches', #item 2, index 1 will be first choice
        '6 foot 9 inches', #item 3, index 2 will be second choice
        '6 foot 7 inches', #item 4, index 3 will be thrid choice
        '6 foot 5 inches',  #item 5, index 4 will be fourth choice
        '6 foot 7 inches',  #item 6, index 5 will be the write statement we need to display the right statement if the users enters wrong choice
        3], #item 7,index 6 will be the position of the right answer (index whre right answer sits), this will be out check if answer is correct or not

    3: ["how long is one quarter in basketball?", #item 1 index 0 will be the question
        '8 minutes', #item 2, index 1 will be first choice
        '10 minutes', #item 3, index 2 will be second choice
        '12 minutes', #item 4, index 3 will be thrid choice
        '15 minutes', #item 5, index 4 will be fourth choice
        '12 minutes', #item 6, index 5 will be the write statement we need to display the right statement if the users enters wrong choice
        3], #item 7,index 6 will be the position of the right answer (index whre right answer sits), this will be out check if answer is correct or not

    4: ["What is it called if you illegally dribble the basketball with both hands at once?", #item 1 index 0 will be the question
        'Double Dribble', #item 2, index 1 will be first choice
        'Illegal Touching', #item 3, index 2 will be second choice
        'Double Fault', #item 4, index 3 will be thrid choice
        'Two Hand Touch', #item 5, index 4 will be fourth choice
        'Double Dribble',  #item 6, index 5 will be the write statement we need to display the right statement if the users enters wrong choice
        1], #item 7,index 6 will be the position of the right answer (index whre right answer sits), this will be out check if answer is correct or not

    5: ["How many points is a half court shot?", #item 1 index 0 will be the question
        '4 points', #item 2, index 1 will be first choice
        '5 points', #item 3, index 2 will be second choice
        '2 points', #item 4, index 3 will be thrid choice
        '3 points', #item 5, index 4 will be fourth choice
        '3 points', #item 6, index 5 will be the write statement we need to display the right statement if the users enters wrong choice
        4], #item 7,index 6 will be the position of the right answer (index whre right answer sits), this will be out check if answer is correct or not

    6: ["What is the glass called that the rim is attached to?", #item 1 index 0 will be the question
        'Backboard', #item 2, index 1 will be first choice
        'Frame', #item 3, index 2 will be second choice
        'Mirror', #item 4, index 3 will be thrid choice
        'Box',  #item 5, index 4 will be fourth choice
        'Backboard',  #item 6, index 5 will be the write statement we need to display the right statement if the users enters wrong choice
        1], #item 7,index 6 will be the position of the right answer (index whre right answer sits), this will be out check if answer is correct or not

    7: ["How long are defending players allowed to stand in the paint for?", #item 1 index 0 will be the question
        '10 seconds', #item 2, index 1 will be first choice
        '24 seconds', #item 3, index 2 will be second choice
        '5 seconds', #item 4, index 3 will be thrid choice
        '3 seconds', #item 5, index 4 will be fourth choice
        '3 seconds', #item 6, index 5 will be the write statement we need to display the right statement if the users enters wrong choice
        4], #item 7,index 6 will be the position of the right answer (index whre right answer sits), this will be out check if answer is correct or not

    8: ["When play is stopped and a player takes shots at the foul line, what are those shots called?", #item 1 index 0 will be the question
        'jumpers', #item 2, index 1 will be first choice
        'Free Throws', #item 3, index 2 will be second choice
        'Dunk from a distance',  #item 4, index 3 will be thrid choice
        'Free Shots', #item 5, index 4 will be fourth choice
        'Free Throws', #item 6, index 5 will be the write statement we need to display the right statement if the users enters wrong choice
        2], #item 7,index 6 will be the position of the right answer (index whre right answer sits), this will be out check if answer is correct or not

    9: ["When your team gets possession, you have a limited number of time based on what?", #item 1 index 0 will be the question
        'Shooting Timer', #item 2, index 1 will be first choice
        'Possession Clock', #item 3, index 2 will be second choice
        'Shot Clock',  #item 4, index 3 will be thrid choice
        'Possession Timer', #item 5, index 4 will be fourth choice
        'Shot Clock', #item 6, index 5 will be the write statement we need to display the right statement if the users enters wrong choice
        3], #item 7,index 6 will be the position of the right answer (index whre right answer sits), this will be out check if answer is correct or not

  
    10: ["How many fouls does an NBA player get before they foul out?", #item 1 index 0 will be the question
         '6', #item 2, index 1 will be first choice
         '5', #item 3, index 2 will be second choice
         '3',  #item 4, index 3 will be thrid choice
         'limitless', #item 5, index 4 will be fourth choice
         '6', #item 6, index 5 will be the write statement we need to display the right statement if the users enters wrong choice
        1], #item 7,index 6 will be the position of the right answer (index whre right answer sits), this will be out check if answer is correct or not
  
  }
    self.con1 = IntVar()
    self.quiz_frame=Frame(parent, bg = background_color, padx=40, pady=40)
    self.quiz_frame.grid()
    random_questions()
    self.question_label=Label(window, text= self.quiz_collection[qnum][0], font=("Helvetica","16"),bg=background_color)
    self.question_label.grid(row=1, padx=10, pady=10)

    
    #Radio button 1
    self.rb1= Radiobutton(window, text=self.quiz_collection[qnum][1], font=("Helvetica","11"), bg=background_color,value=1,padx=10,pady=10,
                variable=self.con1, background = background_color)
    self.rb1.grid(row=2, sticky=W)
     
    #Radio button 2
    self.rb2= Radiobutton(window, text=self.quiz_collection[qnum][2], font=("Noto Serif","11"), bg=background_color,value=2,padx=10,pady=10,
                variable=self.con1, background = background_color)
    self.rb2.grid(row=3, sticky=W)

    #Radio button 3
    self.rb3= Radiobutton(window, text=self.quiz_collection[qnum][3], font=("Noto Serif","11"), bg=background_color,value=3,padx=10,pady=10,
                variable=self.con1, background = background_color)
    self.rb3.grid(row=4, sticky=W)
     
    #Radio button 4
    self.rb4= Radiobutton(window, text=self.quiz_collection[qnum][4], font=("Noto Serif","11"), bg=background_color,value=4,padx=10,pady=10,
                variable=self.con1, background = background_color)
    self.rb4.grid(row=5, sticky=W)


    #confirm Button
    self.confirm_button= Button(window, text="Confirm", font=("Noto Serif", "12", "bold"), bg="SpringGreen3",command=self.test_progress)
    self.confirm_button.grid(row=7, padx=5, pady=5)

    #score Label
    self.score_label=Label(window, text="SCORE", font=("Tw Cen MT", "16"), bg=background_color)
    self.score_label.grid(row=8, padx=10, pady=1)

  #check what is wrong in this method that is editing the radio buttons
  def questions_setup(self):
        random_questions()
        self.con1.set(0)
        self.question_label.config(text=self.quiz_collection[qnum][0])
        self.rb1.config(text=self.quiz_collection[qnum][1])
        self.rb2.config(text=self.quiz_collection[qnum][2])
        self.rb3.config(text=self.quiz_collection[qnum][3])
        self.rb4.config(text=self.quiz_collection[qnum][4])
       
  def test_progress(self):
      global score
      scr_label=self.score_label
      choice=self.con1.get()
      if len(asked)>9:
        if choice == self.quiz_collection[qnum][6]:
          score +=1
          scr_label.configure(text=score)
          self.confirm_button.config(text="Confirm")
         
        else:
          score+=0
          scr_label.configure(text="The correct answer was: "+ self.quiz_collection[qnum][5] )
          self.confirm_button.config(text="confirm")    
     
      else:
            if choice==0:
              self.confirm_button.config(text="Please select an option" )
              choice=self.con1.get()
            else:
              if choice == self.quiz_collection[qnum][6]:
                score+=1
                scr_label.configure(text=score)
                self.confirm_button.config(text="confirm")
                self.questions_setup()
 
              else:
                  score+=0
                  scr_label.configure(text="The correct answer was: " + self.quiz_collection[qnum][5])
                  self.confirm_button.config(text="Confirm")
                  self.questions_setup()
    


#************** Starting Point of Program *************#
if __name__ == '__main__':
  window = Tk()
  window.title('Basketball General Knowledge Quiz')
  window.geometry('500x300')
  bg_image = Image.open('real basketball.png')
  bg_image = bg_image.resize((500, 300),Image.ANTIALIAS)
  bg_image = ImageTk.PhotoImage(bg_image)
  image_label= Label(window, image=bg_image)
  image_label.place(x=0, y=0, relwidth=1, relheight=1)
  quiz_starter_window = QuizStarter(window)
  window.mainloop()


   


































  

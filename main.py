from tkinter import *
import random
from PIL import Image, ImageTk

names_list = []


#dictianary has key of number( for each question number) and : the value for each is a list that has 7 items, so index 0 to 6
questions_answers = {
    1: ["How many players are on the court from each team?", #item 1 index 0 will be the question
        '7 players', #item 2, index 1 will be first choice
        '5 players', #item 3, index 2 will be second choice
        '10 players', #item 4, index 3 will be thrid choice
        '12 players', #item 5, index 4 will be fourth choice
        '5 players' #item 6, index 5 will be the write statement we need to display the right statement if the users enters wrong choice
        ,2], #item 7,index 6 will be the position of the right answer (index whre right answer sits), this will be out check if answer is correct or not

    2: ["How tall is the average nba player?", #item 1 index 0 will be the question
        '6 foot 8 inches', #item 2, index 1 will be first choice
        '6 foot 9 inches', #item 3, index 2 will be second choice
        '6 foot 7 inches', #item 4, index 3 will be thrid choice
        '6 foot 5 inches',  #item 5, index 4 will be fourth choice
        '6 foot 7 inches'  #item 6, index 5 will be the write statement we need to display the right statement if the users enters wrong choice
        ,3], #item 7,index 6 will be the position of the right answer (index whre right answer sits), this will be out check if answer is correct or not

    3: ["how long is one quarter in basketball?", #item 1 index 0 will be the question
        '8 minutes', #item 2, index 1 will be first choice
        '10 minutes', #item 3, index 2 will be second choice
        '12 minutes', #item 4, index 3 will be thrid choice
        '15 minutes', #item 5, index 4 will be fourth choice
        '12 minutes' #item 6, index 5 will be the write statement we need to display the right statement if the users enters wrong choice
      ,3], #item 7,index 6 will be the position of the right answer (index whre right answer sits), this will be out check if answer is correct or not

    4: ["What is it called if you illegally dribble the basketball with both hands at once?" #item 1 index 0 will be the question
        'Double Dribble', #item 2, index 1 will be first choice
        'Illegal Touching', #item 3, index 2 will be second choice
        'Double Fault', #item 4, index 3 will be thrid choice
        'Two Hand Touch', #item 5, index 4 will be fourth choice
        'Double Dribble'  #item 6, index 5 will be the write statement we need to display the right statement if the users enters wrong choice
      ,1], #item 7,index 6 will be the position of the right answer (index whre right answer sits), this will be out check if answer is correct or not

    5: ["How many points is a half court shot?", #item 1 index 0 will be the question
        '4 points', #item 2, index 1 will be first choice
        '5 points', #item 3, index 2 will be second choice
        '2 points', #item 4, index 3 will be thrid choice
        '3 points', #item 5, index 4 will be fourth choice
        '3 points' #item 6, index 5 will be the write statement we need to display the right statement if the users enters wrong choice
      ,4], #item 7,index 6 will be the position of the right answer (index whre right answer sits), this will be out check if answer is correct or not

    6: ["",
        
      
    ]
  
  

  
}

































class QuizStarter:

  def __init__(self, parent):
 
  
    #users input is taken by an Entry Widget
    self.entry_box=Entry(parent)
    self.entry_box.place(x=325, y=210)

  #continue Button
    self.continue_button = Button (parent, text="START QUIZ", bg="azure3", command=self.name_collection)
    self.continue_button.place(x=355, y=250)

  def name_collection(self):
    name = self.entry_box.get()
    names_list.append(name)
    print(names_list)
    #Quiz(root)




#************** Starting Point of Program *************#
if __name__ == '__main__':
  root = Tk()
  root.title('Basketball General Knowledge Quiz')
  root.geometry('500x300')
  bg_image = Image.open('real basketball.png')
  bg_image = bg_image.resize((500, 300),Image.ANTIALIAS)
  bg_image = ImageTk.PhotoImage(bg_image)
  image_label= Label(root, image=bg_image)
  image_label.place(x=0, y=0, relwidth=1, relheight=1)
  quiz_starter_window = QuizStarter(root)
  root.mainloop()


   


































  

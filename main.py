from tkinter import *
import random
from PIL import Image, ImageTk

names_list = []


































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


   


































  

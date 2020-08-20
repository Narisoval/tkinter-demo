import pandas as pd
from PIL import ImageTk
from PIL import Image as mg
from tkinter import *
df = pd.read_csv('Strings.csv')
b = df.loc[30]
a = b['location']
root = Tk()
img = ImageTk.PhotoImage(mg.open(a))
myL = Label(image = img)
myL.pack()
def play(df):
    right_counter = 0
    wrong_counter = 0
    names = []
    wrong_notes = []
    right_notes = []
    myLabel.grid_forget()
    add_buttons()
    while 42:
        row = get_random_row(df)
        get_photo(row['location'])
        note = row['note']
        name = row['name']
        user_inp = (e.get()).upper().strip()
        if user_inp == note:
            right_counter += 1
        elif user_inp == 'STOP':
            if wrong_counter == 0:
                print('You got all {} notes right!!! congratulations'.format(right_counter))
            else:
                print(f'You get {right_counter} notes right and {wrong_counter} notes wrong')
                for (notew, namew, noter) in zip(wrong_notes, names, right_notes):
                    print(f'{namew} right note was: {noter}, your answer was {notew}')
            break
        else:
            right_notes.append(note)
            wrong_notes.append(user_inp)
            names.append(name)
            wrong_counter += 1


root.mainloop()
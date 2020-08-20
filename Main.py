try:
    import PIL as p
    import PIL.ImageTk as ptk
    import pandas as pd
    import time
    import re
    from random import randint
    from tkinter import *
    from tkinter import messagebox
    from tkinter import ttk
    import winsound
    from ttkthemes import ThemedTk
except Exception as e:
    print('Some modules were not imported {}'.format(e))
df = pd.read_csv('Strings.csv')


def get_random_row(data_frame):
    return data_frame.loc[randint(0, 59)]


root = ThemedTk(theme = 'Breeze')
my_style = ttk.Style()
my_style.configure('my.TButton', font=('Helvetica', 12), padx = 30)
root.title('Krich Daun!')
root.iconbitmap('A.ico')
my_img = p.Image.open('start.png').resize(size = (600,400))
photo = ptk.PhotoImage(my_img)
myLabel = ttk.Label(root, image = photo)
myLabel.grid(row = 0, column = 0, sticky = N, columnspan = 4)
time_list = []



def button_click(txt):
    e.delete(0, END)
    e.insert(0, str(txt))


def add_buttons():
    winsound.PlaySound('./sounds/YouSuffer', winsound.SND_ASYNC)
    root.wm_deiconify()
    start_button.grid_forget()
    myLabel.grid_forget()
    global right_counter
    global wrong_counter
    global names
    global wrong_notes
    global right_notes
    global row
    global note
    global name
    right_counter = 0
    wrong_counter = 0
    names = []
    wrong_notes = []
    right_notes = []
    row = get_random_row(df)
    get_photo(row['location'], root, 4)
    note = row['note']
    name = row['name']
    frame.grid(row = 2, columnspan = 4)
    e.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
    a_button.grid(row = 2, column = 0)
    as_button.grid(row = 2, column = 1)
    b_button.grid(row = 2, column = 2)
    c_button.grid(row = 2, column = 3)
    cs_button.grid(row = 3, column = 0)
    d_button.grid(row = 3, column = 1)
    ds_button.grid(row = 3, column = 2)
    e_button.grid(row = 3, column = 3)
    f_button.grid(row = 4, column = 0)
    fs_button.grid(row = 4, column = 1)
    g_button.grid(row = 4, column = 2)
    gs_button.grid(row = 4, column = 3)
    submit_button.grid(row = 5, column = 1)
    stop_button.grid(row = 5, column = 2)
    global _time
    _time = time.time()

def meausre_time():
    global _time
    time_list.append(time.time() - _time)
    _time = time.time()


def submit():
    global user_inp
    global right_counter
    global wrong_counter
    global row
    global note
    global name
    user_inp = (e.get()).upper().strip()
    e.delete(0,END)
    if user_inp == '':
        messagebox.showwarning('Empty field', 'Enter the note please fucking slave')
    elif user_inp == note:
        right_counter += 1
        # placing all the stuff
        row = get_random_row(df)
        get_photo(row['location'],root, 4)
        note = row['note']
        name = row['name']
        meausre_time()
    elif len(user_inp) > 3:
        messagebox.showwarning('To long input', 'Hey, your input is too long')
    else:
        right_notes.append(note)
        wrong_notes.append(user_inp)
        names.append(name)
        wrong_counter += 1
        #placing all the stuff
        row = get_random_row(df)
        get_photo(row['location'],root,4)
        note = row['note']
        name = row['name']
        meausre_time()

def stop():
    really = messagebox.askyesno('WTFF', 'You REALLY want to exit the game???')
    if really == 1:
        root.withdraw()
        top = Toplevel()
        top.iconbitmap('GS.ico')
        top.title('WHY?')
        get_photo('paka.png', top, 3)
        play_again_button = ttk.Button(top, text = 'Play again', style = 'my.TButton', command=lambda:[add_buttons(),top.quit()])
        exit_button = ttk.Button(top, text = 'Exit app', style = 'my.TButton', command=lambda:[top.quit(),root.quit()])
        play_again_button.grid(row = 1, column = 2)
        exit_button.grid(row = 1, column = 0)
        avg_time=round(sum(time_list)/len(time_list),ndigits=2)
        if wrong_counter == 0:
            winsound.PlaySound('./sounds/celebrate',winsound.SND_ASYNC)
            ttk.Label(top, text = 'You got all {} notes right!!! congratulations'.format(right_counter)).grid(row=2,columnspan = 3)
        else:
            winsound.PlaySound('./sounds/Spank', winsound.SND_ASYNC)
            ttk.Label(top, text=f'You got {right_counter} notes right and {wrong_counter} notes wrong').grid(row = 2,columnspan = 3)
            for (notew, namew, noter) in zip(wrong_notes, names, right_notes):
                string_ = "".join(re.split("[^a-zA-Z]*", namew))
                fret = ''.join(re.findall('[0-9]+', namew))
                ttk.Label(top, text=f'On the {string_} string, fret {fret} right note was {noter} but your answer was {notew}').grid(columnspan=3)
        ttk.Label(top, text = 'Your average time was {} seconds'.format(avg_time)).grid(columnspan = 3)
        top.mainloop()
    else:
        pass

frame = LabelFrame(root, padx = 40, pady = 40)
a_button = ttk.Button(frame, text = 'A', style = 'my.TButton', command =lambda: button_click('A'))
as_button = ttk.Button(frame, text='A#', style = 'my.TButton', command=lambda: button_click('A#'))
b_button = ttk.Button(frame ,text='B', style = 'my.TButton', command=lambda: button_click('B'))
c_button = ttk.Button(frame, text='C', style = 'my.TButton', command=lambda: button_click('C'))
cs_button =ttk.Button(frame, text='C#', style = 'my.TButton', command=lambda: button_click('C#'))
d_button = ttk.Button(frame ,text='D', style = 'my.TButton', command=lambda: button_click('D'))
ds_button = ttk.Button(frame, text='D#', style = 'my.TButton', command=lambda: button_click('D#'))
e_button = ttk.Button(frame, text='E', style = 'my.TButton', command=lambda: button_click('E'))
f_button = ttk.Button(frame, text='F', style = 'my.TButton', command=lambda: button_click('F'))
fs_button = ttk.Button(frame, text='F#', style = 'my.TButton', command=lambda: button_click('F#'))
g_button = ttk.Button(frame, text='G', style = 'my.TButton', command=lambda: button_click('G'))
gs_button = ttk.Button(frame, text='G#', style = 'my.TButton', command=lambda: button_click('G#'))


stop_button =  ttk.Button(root, text = 'End the game', style = 'my.TButton', command = stop)
e = Entry(root, width = 35, borderwidth = 5)
submit_button = ttk.Button(root, text='Submit', style = 'my.TButton', command = submit)




def get_photo(loc,where,colspan):
    global myLabel
    global my_img
    global photo
    try:
        ttk.myLabel.grid_forget()
    except:
        pass
    my_img = p.Image.open(loc).resize(size = (600,400))
    photo = ptk.PhotoImage(my_img)
    ttk.myLabel = Label(where, image = photo)
    ttk.myLabel.grid(row = 0, column = 0, columnspan = colspan)


start_button = ttk.Button(root, text='Start', style = 'my.TButton', command= add_buttons)
start_button.grid(row=1,column=1,sticky=W+E)
clicked = StringVar()
root.mainloop()

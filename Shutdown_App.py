# Shutdown app using Python with GUI

# $ Pip install tk

from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def logout():
    os.system("shutdown -l")
def shutdown():
    os.system("shutdown /s /t 1")

st = Tk()
st.title("ShutDown App")
st.geometry("800x500")
st.config(bg="light Blue")

r_button = Button(st, text="Re-Start", font=("Time New Roman", 20, "bold"),
    relief=RAISED, cursor="plus", command=restart)
r_button.place(x=300, y=60, height=50, width=200)

r_button = Button(st, text="Restart-Time", font=("Time New Roman", 20, "bold"),
    relief=RAISED, cursor="plus", command=restart_time)
r_button.place(x=300, y=170, height=50, width=200)

r_button = Button(st, text="Log-Out", font=("Time New Roman", 20, "bold"),
    relief=RAISED, cursor="plus", command=restart)
r_button.place(x=300, y=270, height=50, width=200)

r_button = Button(st, text="Shut-Down", font=("Time New Roman", 20, "bold"),
    relief=RAISED, cursor="plus", command=restart)
r_button.place(x=300, y=370, height=50, width=200)

st.mainloop()
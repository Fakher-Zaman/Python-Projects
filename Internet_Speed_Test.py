# $ pip install tk
# $ pip install speedtest-cli

from tkinter import *
import speedtest

def speedCheck():
    speed = speedtest.Speedtest()
    speed.get_servers()
    down = str(round(speed.download()/(10**6), 3)) + " Mbps"
    up = str(round(speed.upload()/(10**6), 3)) + " Mbps"
    label_Download.config(text=down)
    label_Upload.config(text=up)

# GUI
interface = Tk()
interface.title("Internet Speed Test")
interface.geometry("600x500")
interface.config(bg="cyan")

label = Label(interface, text="Internet Speed Test", font=("Time New Roman", 20, "bold"), bg="cyan") 
label.place(x=100, y=40, height=50, width=400)

label = Label(interface, text="Download Speed", font=("Roboto", 18, "underline"), bg="light blue") 
label.place(x=100, y=130, height=50, width=400)

label_Download = Label(interface, text="00", font=("Time New Roman", 15, "italic")) 
label_Download.place(x=100, y=180, height=50, width=400)

label = Label(interface, text="Upload Speed", font=("Roboto", 18, "underline"), bg="light blue") 
label.place(x=100, y=260, height=50, width=400)

label_Upload = Label(interface, text="00", font=("Time New Roman", 15, "italic")) 
label_Upload.place(x=100, y=310, height=50, width=400)

button = Button(interface, text="Check Speed", font=("Time New Roman", 15, "italic"), bg="red", relief=RAISED, command=speedCheck)
button.place(x=100, y=400, height=50, width=400)

interface.mainloop()
import tkinter as tk
from time import strftime

root = tk.Tk()
root.title('Digital Clock')
t = input("Enter your text")
root.attributes("-fullscreen",True)
#root.attributes("-topmost",True)
root.configure(background="skyblue")
message_label = tk.Label(root, text=t,font=("calibri",70,"bold"), background="skyblue",foreground="green")
message_label.pack(side="top",pady=20)

def time():

    string = strftime("%H:%M:%S %p \n %D \n %A" )
    clock_label.config(text=string)
    clock_label.after(1000,time)

clock_label = tk.Label(root, font=("calibri",100, "bold"), background="skyblue", foreground=["black"])
clock_label.pack(anchor="center")



clock_label.pack(expand=True,fill="both")

time()
root.bind("<Escape>",lambda e:root.destroy())
root.mainloop()

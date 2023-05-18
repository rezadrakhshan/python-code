import tkinter

from time import strftime

tk = tkinter.Tk()

title = tk.title("clock")

tk.resizable(0,0)


def time():
    string = strftime("%H:%M:%S %p")
    clocktime.config(text=string)
    clocktime.after(1000, time)

clocktime = tkinter.Label(
    tk, font=("calibri",40,"bold"),background="red",foreground="yellow"
)

clocktime.pack(anchor="center")

time()

tk.mainloop()


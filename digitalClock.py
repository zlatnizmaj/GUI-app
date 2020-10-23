# https://towardsdatascience.com/building-a-digital-clock-using-python-349b691c5cd7

from tkinter import Label, Tk
import time

# Designing the Application Window
# Define the Window
app_window = Tk()
app_window.title("Moj Digital Clock")
app_window.geometry("500x150")
app_window.resizable(0, 0) # The window is not resizable

# The Label Design
text_font = ("Boulder", 68, 'bold')
background = "#f2e750"
foreground= "#363529"
border_width = 25
label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)

# Digital Clock Function
def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, digital_clock)

# Run the Application
digital_clock()
app_window.mainloop()


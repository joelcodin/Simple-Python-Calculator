import tkinter as tk
from tkinter import Button, Entry #tkinter library is used to create the GUI for the calculator.
#Button and Entry are specific widgets from tkinter that we will use to create buttons and the display for the calculator.

root = tk.Tk() #Necessary command to create the GUI. It creates a window for the GUI to be displayed on.
root.title("Joel's Calculator")
root.geometry("340x400")
#This commands are to define how big the GUI would look like and the title of the GUI.

user_input = tk.StringVar()
# Stores whatever the user types or clicks so the Entry widget can display it.

entry = Entry(root, textvariable=user_input, font=("Arial", 50), width=10, justify="center")
# Creates the calculator display box.
# textvariable=user_input keeps the Entry synced with the StringVar above.
# font and width control the display size, and justify="center" centers the text.

entry.grid(row=0, column=0, columnspan=5, padx=8, pady=8)
# Places the display at the top of the window.
# columnspan=5 makes it stretch across 5 columns.
# padx and pady add space around the widget.

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
# Gives each grid column extra room when the window resizes.

def press_digit(digit):# Adds the button value to the current text shown in the calculator display.

 current = user_input.get() # Gets the current text from the display.
 user_input.set(current+digit) # Adds the new digit or operator to the end of the current text.

def enter_input(): # Evaluates the full expression currently shown in the display.
 # Reads the expression entered by the user.
 Input = user_input.get()
 try:
  result = eval(Input) # Calculates the result of the expression, for example 2+3*4.
  user_input.set(str(result))
  # Converts the result to string and shows it in the display.
 except Exception:
  user_input.set("Error...Error...Error...")
  # If the expression is invalid, show an error message instead.

button1 = Button(root, text="1", command=lambda: press_digit("1"), font=("Arial", 25), width=10 )
button2 = Button(root, text="2", command=lambda: press_digit("2"), font=("Arial", 25), width=10 )
button3 = Button(root, text="3", command=lambda: press_digit("3"), font=("Arial", 25), width=10 )
button4 = Button(root, text="4", command=lambda: press_digit("4"), font=("Arial", 25), width=10 )
button5 = Button(root, text="5", command=lambda: press_digit("5"), font=("Arial", 25), width=10 )
button6 = Button(root, text="6", command=lambda: press_digit("6"), font=("Arial", 25), width=10 )
button7 = Button(root, text="7", command=lambda: press_digit("7"), font=("Arial", 25), width=10 )
button8 = Button(root, text="8", command=lambda: press_digit("8"), font=("Arial", 25), width=10 )
button9 = Button(root, text="9", command=lambda: press_digit("9"), font=("Arial", 25), width=10 )
button0 = Button(root, text="0", command=lambda: press_digit("0"), font=("Arial", 25), width=10 )
addition_button = Button(root, text="+", command=lambda: press_digit("+"), font=("Arial", 10), width=8, justify="center")
subtraction_button = Button(root, text="-", command=lambda: press_digit("-"), font=("Arial", 10), width=8, justify="center")
Multiplication_button = Button(root, text="x", command=lambda: press_digit("*"), font=("Arial", 10), width=8, justify="center")
Clear_button = Button(root, text="AC", command=lambda: user_input.set(""), font=("Arial", 10), width=8, justify="center")
Modulus_button = Button(root, text="%", command=lambda: press_digit("%"), font=("Arial", 10), width=8, justify="center")
button_equals = Button(root, text="=", command=enter_input, font=("Arial", 10), width=8, justify="center")
button1.grid(row=3, column=0, padx=5, pady=5)
button2.grid(row=3, column=1, padx=5, pady=5)
button3.grid(row=3, column=2, padx=5, pady=5)
button4.grid(row=2, column=0, padx=5, pady=5)
button5.grid(row=2, column=1, padx=5, pady=5)
button6.grid(row=2, column=2, padx=5, pady=5)
button7.grid(row=1, column=0, padx=5, pady=5)
button8.grid(row=1, column=1, padx=5, pady=5)
button9.grid(row=1, column=2, padx=5, pady=5)
button0.grid(row=4, column=1, padx=5, pady=5)
addition_button.grid(row=1, column=4, padx=5, pady=5, ipady=18)
subtraction_button.grid(row=2, column=4, padx=5, pady=5, ipady=18)
Multiplication_button.grid(row=3, column=4, padx=5, pady=5, ipady=18)
Modulus_button.grid(row=4, column=2, padx=5, pady=5, ipady=18)
Clear_button.grid(row=4, column=0, padx=5, pady=5, ipady=18)
button_equals.grid(row=4, column=4, padx=5, pady=5, ipady=18)

root.mainloop()


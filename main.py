# Glossary
from tkinter import *

# keydownfunc
def click():
    entered_text=textentry.get()
    # ^ this will collect the text from the text entry box
    output.delete(0.0, END)


    result = entered_text.replace("s","sh")
    result = result.replace("S","Sh")
    output.insert(END, result)


# Main
window = Tk()
window.title("Conversh Like Connery")
window.configure(background="black")

### My Photo
photo1 = PhotoImage(file="glosstitle.png")
Label(window, image=photo1, bg="black") .grid(row=0, column=0, sticky=N)

# Create label
Label(window, text="Enter the text you would like converting:", bg="black", fg="white", font="none 35 bold") .grid(row=5, column=0, sticky=W)

# Create padding
Label(window, text="_________________________________________________", bg="black", fg="black", font="none 35 bold") .grid(row=1, column=0, sticky=W)

# Create text entry box
textentry = Entry(window, width=208, bg="grey")
textentry.grid(row=8, column=0, sticky=W)

# Submit button
Button(window, text="SUBMIT", width=6, command=click) .grid(row=8, column=0, sticky=E)

# Create another label
Label (window, text="\nConverted text:", bg="black", fg="white", font="none 12 bold") .grid(row=9, column=0, sticky=W)

# Create output text box
output = Text(window, width=75, height=4, wrap=WORD, background="grey")
output.grid(row=11, column=0, columnspan=2, sticky=W)



# exit function
def close_window():
    window.destroy()
    exit()

# exit button
Button(window, text="Click to Exit", width=14, command=close_window) .grid(row=15, column=0, sticky=W)

window.resizable(0,0)

# Run main loop
window.mainloop()
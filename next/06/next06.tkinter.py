import tkinter as tk
from pathlib import Path

# Create a window
window = tk.Tk()
window.title("My First GUI Program")

# Create a label
label = tk.Label(text="What's my favorite video?")
label.pack()

# Create a button
button = tk.Button(text="click to find out!")
button.pack()

# on button click


def on_button_click():
    # create a image object
    img = tk.PhotoImage(file=str(Path.cwd()) +
                        "/next/06/secret/895ce751ba0379700381d17a67086931.gif")
    # create a label with image
    img_label = tk.Label(image=img)
    img_label.image = img
    img_label.pack()


button["command"] = on_button_click

# Run the main loop
window.mainloop()

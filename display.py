from tkinter import *
# Setup meta
root = Tk()
root.title("Game of Life")

# Define grid
canv = Canvas(root, width=600, height=600)

# Visualize
canv.pack()

# Loop
root.mainloop()
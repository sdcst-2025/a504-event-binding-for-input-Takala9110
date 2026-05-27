"""
##### Task 1
Create entry widets to allow user to enter their:
* name
* student number
* grade

Create a button so that when they click on the button, it states all of the information in a 4th entry widget
"""

from tkinter import *

window = Tk()
window.title("task_1")

Label(window, text="Name").grid(row=0, column=0)
Label(window, text="Student Number").grid(row=1, column=0)
Label(window, text="Grade").grid(row=2, column=0)
Label(window, text="Output").grid(row=4, column=0)

name_entry = Entry(window, width=30)
student_entry = Entry(window, width=30)
grade_entry = Entry(window, width=30)
output_entry = Entry(window, width=50)

name_entry.grid(row=0, column=1)
student_entry.grid(row=1, column=1)
grade_entry.grid(row=2, column=1)
output_entry.grid(row=4, column=1)

def info():
    name = name_entry.get()
    student = student_entry.get()
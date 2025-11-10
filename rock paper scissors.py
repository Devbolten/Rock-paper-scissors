# importing modules
import tkinter as tk
import random

# setting up the window
window = tk.Tk()
window.title("Rock paper scissors")
window.geometry("500x250")
window.configure(bg="grey")

#initialising variables
choices = ["rock", "paper", "scissors"]
randnum = random.randint(0, 2)
computer_choice = choices[randnum]
result = ""
user = ""

# Making the labels
label_result = tk.Label(window, text="Result: ", bg="grey", fg="black", font=("Calibri", 17))
label_result.pack(pady=7)
label = tk.Label(window, text="Click to start! ⬇", bg="lightblue", fg="black", font=("Calibri", 16))
label.pack(pady=7)

## Making the button functions
def button_click_rock():
    global user
    label.config(text=f"you clicked the rock button")
    user = "rock"
    determine_winner()
    create_reset_button()


def button_click_paper():
    global user
    label.config(text=f"you clicked the paper button")
    user = "paper"
    determine_winner()
    create_reset_button()



def button_click_scissors():
    global user
    label.config(text=f"you clicked the scissors button")
    user = "scissors"
    determine_winner()
    create_reset_button()

# Making the buttons
rock_button = tk.Button(window, text="rock", bg="lightgrey", fg="black", command=button_click_rock, font=("Calibri", 15))
rock_button.place(relx=0.15, y=125, width=100, height=50)
paper_button = tk.Button(window, text="paper", bg="lightgrey", fg="white", command=button_click_paper, font=("Calibri", 15))
paper_button.place(relx=0.4, y=125, width=100, height=50)
scissors_button = tk.Button(window, text="scissors", bg="lightgrey", fg="grey", command=button_click_scissors, font=("Calibri", 15))
scissors_button.place(relx=0.65, y=125, width=100, height=50)




def reset_game():
    #global variables
    global choices
    global computer_choice
    global choices
    global randnum
    global rock_button
    global paper_button
    global scissors_button
    global label
    global label_result

    rock_button.destroy()
    paper_button.destroy()
    scissors_button.destroy()
    randnum = random.randint(0, 2)
    computer_choice = choices[randnum]

    # remaking buttons
    rock_button = tk.Button(window, text="rock", bg="lightgrey", fg="black", command=button_click_rock, font=("Calibri", 15))
    rock_button.place(relx=0.15, y=125, width=100, height=50)
    paper_button = tk.Button(window, text="paper", bg="lightgrey", fg="white", command=button_click_paper, font=("Calibri", 15))
    paper_button.place(relx=0.4, y=125, width=100, height=50)
    scissors_button = tk.Button(window, text="scissors", bg="lightgrey", fg="grey", command=button_click_scissors, font=("Calibri", 15))
    scissors_button.place(relx=0.65, y=125, width=100, height=50)

    label_result.config(text="Result: ", bg="grey", fg="black", font=("Calibri", 17))
    label.config(text="Click to start! ⬇", bg="lightblue", fg="black", font=("Calibri", 16))

    global reset_button
    reset_button.destroy()


def create_reset_button():
    global reset_button
    reset_button = tk.Button(window, text="Reset Game", bg="lightgrey", fg="black", command=reset_game, width=10, height=3, font=("Calibri", 10))
    reset_button.place(relx=0.8, y=10)
    

def determine_winner():
    global result
    global computer_choice
    global choices
    global randnum
    global rock_button
    global paper_button
    global scissors_button
    if user == 'rock' and computer_choice == 'rock':
        result = "It's a tie!"
        paper_button.destroy()
        scissors_button.destroy()
    elif user == 'paper' and computer_choice == 'paper':
        result = "It's a tie!"
        rock_button.destroy()
        scissors_button.destroy()
    elif user == 'scissors' and computer_choice == 'scissors':
        result = "It's a tie!"
        rock_button.destroy()
        paper_button.destroy()
    elif user == 'rock' and computer_choice == 'paper':
        result = "Computer wins!"
        paper_button.destroy()
        scissors_button.destroy()
    elif user == 'paper' and computer_choice == 'scissors':
        result = "Computer wins!"
        scissors_button.destroy()
        rock_button.destroy()
    elif user == 'scissors' and computer_choice == 'rock':
        result = "Computer wins!"
        rock_button.destroy()
        paper_button.destroy()
    elif user == 'rock' and computer_choice == 'scissors':
        result = "You win!"
        scissors_button.destroy()
        paper_button.destroy()
    elif user == 'paper' and computer_choice == 'rock':
        result = "You win!"
        rock_button.destroy()
        scissors_button.destroy()
    elif user == 'scissors' and computer_choice == 'paper':
        result = "You win!"
        rock_button.destroy()
        paper_button.destroy()
    else:
        result = "Make a choice to play!"
    label_result.config(text=f"Result: {result}")









window.mainloop()
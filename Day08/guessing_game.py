import random
import tkinter as tk


def get_guess():
    value = guess_entry.get()
    if value.isdigit():
        int_value = int(value)
        if int_value in range(1,21):
            return int_value
        elif int_value not in range(1,21):
            error_window = tk.Toplevel(root)
            error_window.geometry("200x150")
            error = tk.Label(error_window, text=f"Enter a valid value")
            error.pack(pady=50)
            feedback_var.set(f"Enter Number between 1 to 20")
            return None
    else:
        error_window = tk.Toplevel(root)
        error_window.geometry("200x150")
        error = tk.Label(error_window, text=f"Enter a valid value")
        error.pack(pady=50)
        feedback_var.set("Enter a valid value")
        return None

def play_game():
    global tries
    user_guess = get_guess()
    tries += 1
    if result_var.get()==0:
        window = tk.Toplevel(root)
        window.geometry("200x150")
        high = tk.Label(window, text=f"Computer Had Not Picked Yet")
        high.pack(pady=50)
        feedback_var.set(f"Computer Had Not Picked Yet")
    elif user_guess is not None:
        window = tk.Toplevel(root)
        window.geometry("200x150") 
        if user_guess > result_var.get():
            high = tk.Label(window, text=f"Too High\nTry Again")
            high.pack(pady=50)
            feedback_var.set(f"Too High\nTry Again")
        elif user_guess < result_var.get():
            low = tk.Label(window, text=f"Too Low\nTry Again")
            low.pack(pady=50)
            feedback_var.set(f"Too Low\nTry Again")
        else:
            correct = tk.Label(window, text=f"You're correct! Number of tries: {tries}\n\nDo You Want To Play Again?")
            correct.pack()
            feedback_var.set(f"You're correct! Number of tries: {tries}")
            yes_button = tk.Button(window, text='Yes', command=Restart)
            yes_button.pack(side="left", pady=20)
            no_button = tk.Button(window, text='No', command=Exit)
            no_button.pack(side="right", pady=20)
    else:
        pass

def auto_number_pick():
    window = tk.Toplevel(root)
    window.geometry("200x150")
    number = random.randrange(1, 20)
    pick = tk.Label(window, text=f"The Computer Picked a Number")
    pick.pack(pady=50)
    return number

def store_generated_number():
    result = auto_number_pick()
    result_var.set(result)

def hidden_value():
    window = tk.Toplevel(root)
    window.geometry("200x150")
    hidden_value_label = tk.Label(window, text=f"The correct guess: {result_var.get()}")
    hidden_value_label.pack(pady=50)

def Restart():
    global tries
    tries = 0
    guess_entry.delete(0, tk.END)
    result_var.set(0)
    feedback_var.set("")
    store_generated_number()

def Exit():
    root.destroy()


tries = 0

root = tk.Tk()
root.geometry('300x200')
root.title('Guessing Game')


start_button = tk.Button(root, text='Start Playing', command=store_generated_number)
start_button.pack(pady=20)

guessing_label = tk.Label(root, text='Guess a Number Between 1 to 20')
guessing_label.pack()

guess_entry = tk.Entry(root)
guess_entry.pack()

run_button = tk.Button(root, text='Try', command=play_game)
run_button.pack()

options_button = tk.Menubutton(root, text="Options", relief=tk.RAISED)
options_button.pack(pady=10)

menu = tk.Menu(options_button, tearoff=False)
options_button.config(menu=menu)

result_var = tk.IntVar()
result_var.set(0)

feedback_var = tk.StringVar()
feedback_var.set("")

result_label = tk.Label(root, textvariable=feedback_var)
result_label.pack(pady=20)

menu.add_command(label="Show hidden value", command=hidden_value)
menu.add_command(label="Restart", command=Restart)
menu.add_command(label="Exit", command=Exit)

root.mainloop()
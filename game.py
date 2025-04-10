import random
import customtkinter as ctk

def load_acronyms(file_name):
    acronyms = []
    with open(file_name, 'r') as file:
        for line in file:
            acronym, meaning = line.strip().split(' ', 1)
            acronyms.append((acronym, meaning))
    return acronyms

def check_answer(acronyms, index, user_input):
    acronym, meaning = acronyms[index]
    if user_input.lower() == meaning.lower().strip():
        return True, meaning
    else:
        return False, meaning

def play_game(acronyms):
    random.shuffle(acronyms)
    index = 0

    def next_question():
        nonlocal index
        if index < len(acronyms):
            acronym, _ = acronyms[index]
            label.configure(text=f"Acronym: {acronym}")
            entry.delete(0, ctk.END)
            entry.focus()
            index += 1
        else:
            response.config(text=f"Game over! Your score is: {score}")
            submit_button.config(state=ctk.DISABLED)

    def submit_answer():
        nonlocal score
        user_input = entry.get()
        is_correct, meaning = check_answer(acronyms, index - 1, user_input)
        if is_correct:
            score += 1
            response.configure(text="Correct!")
        else:
            score -= 1
            if score<0:
                score=0
            response.configure(text=f"Incorrect! The correct meaning is: {meaning}")
        score_label.configure(text=f"Score: {score}")
        next_question()

    root = ctk.CTk()
    root.title("Acronym Game")
    root.geometry("500x200")  # Set the size of the window

    score = 0
    score_label = ctk.CTkLabel(root, text="Score: 0", font=("Arial", 24))
    score_label.pack(pady=10)

    response = ctk.CTkLabel(root, text="", pady=10)
    response.pack()

    label = ctk.CTkLabel(root, text="Acronym: ", pady=10)
    label.pack()

    entry = ctk.CTkEntry(root, width=400)
    entry.pack()
    entry.bind("<Return>", lambda event: submit_answer())

    submit_button = ctk.CTkButton(root, text="Submit", command=submit_answer)
    submit_button.pack()
    next_question()

    root.mainloop()

if __name__ == '__main__':
    file_name = 'dat_fork.txt'
    acronyms = load_acronyms(file_name)
    play_game(acronyms)

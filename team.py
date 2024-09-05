import customtkinter as ctk
import random

def generate_teams(name_entry):
    names = name_entry.get('1.0', ctk.END).strip().split('\n')
    num_teams = int(num_teams_entry.get() or 0)
    
    random.shuffle(names)
    
    teams = [names[i::num_teams] for i in range(num_teams)]
    
    team_names = ['Team ' + str(i+1) for i in range(num_teams)]
    random.shuffle(team_names)
    
    result_text.delete('1.0', ctk.END)
    for i, team in enumerate(teams):
        result_text.insert(ctk.END, f'{team_names[i]}:\n')
        result_text.insert(ctk.END, ', '.join(team) + '\n\n')

root = ctk.CTk()
root.title('Team Generator')

name_label = ctk.CTkLabel(root, text='Enter names (one per line):')
name_label.pack()

name_entry = ctk.CTkTextbox(root, height=50, width=100)
name_entry.pack()

num_teams_label = ctk.CTkLabel(root, text='Enter number of teams:')
num_teams_label.pack()

num_teams_entry = ctk.CTkEntry(root)
num_teams_entry.pack()

generate_button = ctk.CTkButton(root, text='Generate Teams', command=lambda: generate_teams(name_entry))
generate_button.pack()

result_label = ctk.CTkLabel(root, text='Generated Teams:')
result_label.pack()

result_text = ctk.CTkTextbox(root, height=10, width=30)
result_text.pack()

root.mainloop()
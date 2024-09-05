import customtkinter as ctk

def click():
    win.destroy()

win = ctk.CTk()
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
win.title("Python GUI")
lable = ctk.CTkLabel(win, text="Hello World", font=("Arial Bold", 20))
lable.pack(padx=50, pady=20)
button = ctk.CTkButton(win, font=("Arial Bold", 24), text="NO!", command=click)
button.pack(padx=50, pady=20)


win.mainloop()
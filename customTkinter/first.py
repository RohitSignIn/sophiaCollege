import customtkinter

def button_callback():
    print("button pressed")

app = customtkinter.CTk()
app.title("my app")
app.geometry("400x150")

app.grid_rowconfigure(0, weight=1)

sideBar = customtkinter.CTkFrame(app, width=250, fg_color="#fff")
sideBar.grid(row=0, column=0, sticky="ns")

app.mainloop()
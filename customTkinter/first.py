import customtkinter

def button_callback():
    print("button pressed")

def homeLayout():
    mainLayout = customtkinter.CTkFrame(app, fg_color="#fff", corner_radius=0)

    mainLayout.grid(row=0, column=1, sticky="ewns")

    label = customtkinter.CTkLabel(mainLayout, text="Home")

    label.grid(row=0, column=0)

def aboutLayout():
    mainLayout = customtkinter.CTkFrame(app, fg_color="red", corner_radius=0)

    mainLayout.grid(row=0, column=1, sticky="ewns")

    mainLayout.grid_rowconfigure(0, weight=1)
    mainLayout.grid_columnconfigure(0, weight=1)

    label = customtkinter.CTkLabel(mainLayout, text="About")

    label.grid(row=0, column=0)

def contactLayout():
    mainLayout = customtkinter.CTkFrame(app, fg_color="green", corner_radius=0)

    mainLayout.grid(row=0, column=1, sticky="ewns")

    label = customtkinter.CTkLabel(mainLayout, text="Contact")

    label.grid(row=0, column=0)

app = customtkinter.CTk()
app.title("my app")
app.geometry("800x600")

app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

sideBar = customtkinter.CTkFrame(app, width=250, fg_color="#fff", corner_radius=0)
sideBar.grid(row=0, column=0, sticky="ns")

homeBtn = customtkinter.CTkButton(sideBar, text="Home", command=homeLayout)

aboutBtn = customtkinter.CTkButton(sideBar, text="About", command=aboutLayout)

contactBtn = customtkinter.CTkButton(sideBar, text="Contact", command=contactLayout)


homeBtn.grid(row=0, column=0, padx=5, pady=5)
aboutBtn.grid(row=1, column=0, padx=5, pady=5)
contactBtn.grid(row=2, column=0, padx=5, pady=5)




app.mainloop()
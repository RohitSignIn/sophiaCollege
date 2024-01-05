import customtkinter;
app = customtkinter.CTk()

app.geometry("800x600")
app.title("First Gui ")

app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

frame = customtkinter.CTkFrame(app, width=400, height=400, fg_color="#fff")

frame.grid(row=0, column=0, sticky="ewns", padx=25, pady=25)


btn = customtkinter.CTkButton(frame, text="First Frame")

btn.grid(row=0, column=0)  


frame.grid_columnconfigure(0, weight=1)
frame.grid_rowconfigure(0, weight=1)


app.mainloop()
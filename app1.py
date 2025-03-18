#  beautiful customtkinter app v1

import customtkinter

# configure window
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

# create main app window
app = customtkinter.CTk()
app.geometry("400x580")
app.title("CustomTkinter App")


# create a frame for Iteration #1
frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)


# add a label to the frame
label_1 = customtkinter.CTkLabel(master=frame_1, text="Iteration #1", justify=customtkinter.LEFT)
label_1.pack(pady=12, padx=10)

# add an entry widget
entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="CTkEntry")
entry_1.pack(pady=12, padx=10)

# add a button
button_1 = customtkinter.CTkButton(master=frame_1, text="CTkButton", command=lambda: print("button pressed"))
button_1.pack(pady=12, padx=10)

# add a checkbox
checkbox_1 = customtkinter.CTkCheckBox(master=frame_1, text="CTkCheckBox")
checkbox_1.pack(pady=12, padx=10)

# add a radiobutton
radiobutton_var = customtkinter.IntVar(value=0)

radiobutton_1 = customtkinter.CTkRadioButton(master=frame_1, text="CTkRadioButton Option 1", variable=radiobutton_var, value=0)
radiobutton_1.pack(pady=12, padx=10)

radiobutton_2 = customtkinter.CTkRadioButton(master=frame_1, text="CTkRadioButton Option 2", variable=radiobutton_var, value=1)
radiobutton_2.pack(pady=12, padx=10)


# add a switch
switch_1 = customtkinter.CTkSwitch(master=frame_1, text="CTkSwitch")
switch_1.pack(pady=12, padx=10)

# add a segmented button
segmented_button_var = customtkinter.StringVar(value="Value 1")
segmented_button = customtkinter.CTkSegmentedButton(frame_1, values=["Value 1", "Value 2", "Value Long"], variable=segmented_button_var)
segmented_button.pack(pady=12, padx=10)



# start the main event loop
app.mainloop()


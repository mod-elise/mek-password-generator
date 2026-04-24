import tkinter as tk
from password_generator.generator import generate_password

passwordrow = 0
sliderrow = 1
checkboxrow = 2


def pressGenerate(pwlength, uppercase, digits, symbols):
    entry.delete(0, tk.END)
    password, strength = generate_password(pwlength, uppercase, digits, symbols)
    entry.insert(tk.END, password)
    print("Strength is:", strength)
    if strength == "Weak":
        frame.config(bg="red")
    elif strength == "Medium":
        frame.config(bg="orange")
    elif strength == "Strong":
        frame.config(bg="green")


def pressCopy():
    root.clipboard_clear()
    root.clipboard_append(entry.get())
    root.update()


root = tk.Tk()
root.title("Password Generator")
entry = tk.Entry(root, width=34, font=("Arial", 18))
entry.grid(row=passwordrow, column=0, columnspan=3)
hasUppercase = tk.BooleanVar()
hasDigits = tk.BooleanVar()
hasSymbols = tk.BooleanVar()
passwordLength = tk.IntVar()


slider = tk.Scale(
    root,
    from_=4,
    to=25,
    label="Password Length",
    variable=passwordLength,
    length=400,
    orient=tk.HORIZONTAL,
).grid(row=sliderrow, column=0, columnspan=3)

frame = tk.Frame(root, bg="grey", width=50, height=50, bd=3, relief=tk.RIDGE)
frame.grid(row=sliderrow, column=4)


upCheck = tk.Checkbutton(root, text="uppercase", variable=hasUppercase).grid(
    row=checkboxrow, column=0
)
digCheck = tk.Checkbutton(root, text="digits", variable=hasDigits).grid(
    row=checkboxrow, column=1
)
specCheck = tk.Checkbutton(root, text="special", variable=hasSymbols).grid(
    row=checkboxrow, column=2
)

tk.Button(
    root,
    text="Generate",
    width=10,
    height=4,
    bg="LIGHT GREEN",
    command=lambda: pressGenerate(
        passwordLength.get(), hasUppercase.get(), hasDigits.get(), hasSymbols.get()
    ),
).grid(row=checkboxrow, column=4)

tk.Button(root, text="Copy", width=10, command=lambda: pressCopy()).grid(
    row=passwordrow, column=4
)


root.mainloop()

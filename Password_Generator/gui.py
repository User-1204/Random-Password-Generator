import tkinter as tk
from tkinter import ttk

# GUI creator function
def create_gui(callbacks):
    root = tk.Tk()
    root.title("Password Generator")
    root.geometry("480x640")  
    root.configure(bg="#E58943")   # Background color
    root.resizable(False, False)

    # Fonts and Colors
    heading_font = ('Segoe UI', 20, 'bold')
    label_font = ('Segoe UI', 12)
    entry_font = ('Segoe UI', 12)
    button_font = ('Segoe UI', 11)
    BG = "#E58943"
    FG = "#000000"
    ACCENT = "#586F8D"
    ACCENT_ACTIVE = "#586F8D"

    # Header
    tk.Label(root, text="Password Generator", font=heading_font, bg=BG, fg=FG).pack(pady=(20, 10))

    frame = tk.Frame(root, bg=BG)
    frame.pack(fill='x', padx=20)

    # Length input field
    tk.Label(frame, text="Length:", font=label_font, bg=BG, fg=FG).grid(row=0, column=0, sticky='w', pady=5)
    length_var = tk.StringVar(value="12")
    length_entry = tk.Entry(frame, textvariable=length_var, font=entry_font, width=6, relief='solid')
    length_entry.grid(row=0, column=1, sticky='w', pady=5)

    # Checkboxes
    letters = tk.BooleanVar(value=True)
    numbers = tk.BooleanVar(value=True)
    symbols = tk.BooleanVar(value=True)
    repeat = tk.BooleanVar(value=True)
    exclude = tk.BooleanVar(value=False)

    options = [
        ("Include Letters", letters),
        ("Include Numbers", numbers),
        ("Include Symbols", symbols),
        ("Allow Repetition", repeat),
        ("Exclude Ambiguous Characters", exclude)
    ]
    for i, (text, var) in enumerate(options):
        tk.Checkbutton(frame, text=text, variable=var, font=label_font,
                       bg=BG, fg=FG, anchor='w').grid(row=i+1, column=0, columnspan=2, sticky='w', pady=2)

    # Result field
    result_var = tk.StringVar()
    tk.Entry(root, textvariable=result_var, font=entry_font, width=34, justify='center',
             relief='solid', bd=1, fg="#595959").pack(pady=20)

    # Strength meter
    strength_var = tk.StringVar(value="Strength: ")
    tk.Label(root, textvariable=strength_var, font=label_font, bg=BG, fg=FG).pack()
    strength_bar = ttk.Progressbar(root, length=250, maximum=100)
    strength_bar.pack(pady=5)

    # Buttons
    btn_args = {'font': button_font, 'bg': ACCENT, 'fg': "white", 'activebackground': ACCENT_ACTIVE,
                'relief': "flat", 'width': 30, 'pady': 5}
    tk.Button(root, text="Generate Password", command=callbacks['generate'], **btn_args).pack(pady=(10, 5))
    tk.Button(root, text="Copy to Clipboard", command=callbacks['copy'], **btn_args).pack(pady=5)
    tk.Button(root, text="Export to File", command=callbacks['export'], **btn_args).pack(pady=5)

    # Footer label
    tk.Label(root, text="Made by Sakshi | 2025", font=('Segoe UI', 10), bg=BG, fg=FG).pack(side='bottom', pady=10)

    # Pressing Enter triggers generation 
    root.bind('<Return>', lambda event: callbacks['generate']())

    # Return widgets and variables for logic integration
    settings = {'length': length_var, 'letters': letters, 'numbers': numbers,
                'symbols': symbols, 'repeat': repeat, 'exclude': exclude}
    return root, settings, result_var, strength_var, strength_bar

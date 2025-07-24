import random, string, pyperclip # pip install pyperclip
from datetime import datetime
from tkinter import messagebox

# Characters that look alike (to exclude if needed)
ambiguous_chars = "O0Il1"

# Function to check strength based on length and character variety
def check_strength(password):
    length = len(password)
    has_letters = any(c.isalpha() for c in password)
    has_numbers = any(c.isdigit() for c in password)
    has_symbols = any(c in string.punctuation for c in password)
    types_used = sum([has_letters, has_numbers, has_symbols])

    if length >= 12 and types_used == 3:
        return "Strong", 80
    elif length >= 8 and types_used >= 2:
        return "Medium", 50
    else:
        return "Weak", 20

# Generates password and updates result and strength
def generate_password(settings, result_var, strength_var, strength_bar):
    try:
        length = int(settings['length'].get())
        if length <= 0:
            raise ValueError

        chars = ''
        if settings['letters'].get(): chars += string.ascii_letters
        if settings['numbers'].get(): chars += string.digits
        if settings['symbols'].get(): chars += string.punctuation
        if settings['exclude'].get():
            chars = ''.join(c for c in chars if c not in ambiguous_chars)
        if not settings['repeat'].get():
            chars = ''.join(sorted(set(chars)))

        if not chars:
            messagebox.showerror("Error", "No characters left. Adjust options.")
            return
        if not settings['repeat'].get() and length > len(chars):
            messagebox.showerror("Error", "Length too long for unique characters.")
            return

        pwd = [] # Start with an empty password
        if settings['letters'].get():
            subset = ''.join(c for c in string.ascii_letters if not settings['exclude'].get() or c not in ambiguous_chars)
            pwd.append(random.choice(subset))
        if settings['numbers'].get():
            subset = ''.join(c for c in string.digits if not settings['exclude'].get() or c not in ambiguous_chars)
            pwd.append(random.choice(subset))
        if settings['symbols'].get():
            subset = ''.join(c for c in string.punctuation if not settings['exclude'].get() or c not in ambiguous_chars)
            pwd.append(random.choice(subset))

        remain = length - len(pwd)
        if remain < 0:
            messagebox.showerror("Error", "Length too short for options.")
            return

        if settings['repeat'].get():
            pwd += [random.choice(chars) for _ in range(remain)]
        else:
            available = list(set(chars) - set(pwd))
            random.shuffle(available)
            pwd += available[:remain]

        random.shuffle(pwd)
        final = ''.join(pwd)
        result_var.set(final)
        strength, score = check_strength(final)
        strength_var.set(f"Strength: {strength}")
        strength_bar['value'] = min(score, 100)

    except ValueError:
        messagebox.showerror("Error", "Enter a valid positive number.")

# Copy result to clipboard
def copy_to_clipboard(result_var):
    pwd = result_var.get()
    if pwd:
        pyperclip.copy(pwd)
        messagebox.showinfo("Copied", "Password copied!")
    else:
        messagebox.showwarning("Warning", "No password to copy.")

# Export result to file
def export_to_file(result_var):
    pwd = result_var.get()
    if pwd:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"password_{timestamp}.txt"
        try:
            with open(filename, "w") as f:
                f.write(pwd)
            messagebox.showinfo("Saved", f"Saved as {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save: {e}")
    else:
        messagebox.showwarning("Warning", "No password to save.")

import tkinter as tk
import random
import string
import re
import keyword

def scramble_code():
    original_code = input_text.get("1.0", tk.END)
    key = int(key_entry.get())  # Get the key from the entry field

    # 1. Variable and function renaming
    replacements = {}
    for identifier in set(original_code.split()):
        if identifier.isidentifier() and not keyword.iskeyword(identifier):
            new_name = ''.join(random.choices(string.ascii_letters, k=random.randint(5, 15)))
            replacements[identifier] = new_name
    for old_name, new_name in replacements.items():
        original_code = original_code.replace(old_name, new_name)

    # 2. String encryption (using the provided key)
    encrypted_strings = {}
    for match in re.finditer(r'"([^"]*)"', original_code):
        original_string = match.group(1)
        encrypted_string = ''.join(chr(ord(c) ^ key) for c in original_string)
        encrypted_strings[original_string] = encrypted_string
    for original_string, encrypted_string in encrypted_strings.items():
        original_code = original_code.replace(f'"{original_string}"', f'"{encrypted_string}"')

    # 3. Whitespace removal and insertion
    code = original_code.replace('\n', '').replace(' ', '')
    for _ in range(random.randint(10, 30)):
        insert_position = random.randint(0, len(code))
        code = code[:insert_position] + ' ' + code[insert_position:]

    # 4. Comment insertion
    for _ in range(random.randint(5, 15)):
        comment = '# ' + ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(10, 30)))
        insert_position = random.randint(0, len(code))
        code = code[:insert_position] + comment + '\n' + code[insert_position:]

    # Display the scrambled code and the key
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, f"Scrambled code (key={key}):\n\n{code}") 

# Create the main window
window = tk.Tk()
window.title("Code Scrambler")

# Input text area
input_label = tk.Label(window, text="Enter code to scramble:")
input_label.pack()
input_text = tk.Text(window, height=10, width=50)
input_text.pack()

# Scramble button
scramble_button = tk.Button(window, text="Scramble", command=scramble_code)
scramble_button.pack()

# Key input
key_label = tk.Label(window, text="Encryption Key (integer):")
key_label.pack()
key_entry = tk.Entry(window)
key_entry.pack()

# Output text area
output_label = tk.Label(window, text="Scrambled code:")
output_label.pack()
output_text = tk.Text(window, height=10, width=50)
output_text.pack()

window.mainloop()

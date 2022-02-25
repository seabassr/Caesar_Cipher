from posixpath import split
import tkinter as tk

# GUI setup
window = tk.Tk()
window.title("Caesar Cipher")

# Plain text entry
plaintext_block = tk.Frame(window)
# Buttons for simple and complex
encryption_type_block = tk.Frame(window)
# Caesar text display
caesartext_block = tk.Frame(window)
# Key dropdown, and encryption/decryption buttons
simple_options_block = tk.Frame(window)
# Key entry, and encryption/decryption buttons
complex_options_block = tk.Frame(window)

### PLAINTEXT ###
# Plain text entry
label_plain = tk.Label(plaintext_block, text="Plain Text:", font=14)
label_plain.pack(side=tk.TOP)
entry_plain = tk.Entry(plaintext_block, font=14)
entry_plain.config(highlightbackground="grey")
entry_plain.pack(side=tk.TOP)

### CAESARTEXT ###
# Caesar text display
label_caesar = tk.Label(caesartext_block, text="Caesar Text:", font=14)
label_caesar.pack(side=tk.TOP)
entry_caesar = tk.Entry(caesartext_block, font=14)
entry_caesar.config(highlightbackground="grey", state="disabled")
entry_caesar.pack(side=tk.TOP)

### ENCRYPTION TYPE ###
# Simple Caesar encryption button
button_connect = tk.Button(encryption_type_block, text="Simple", font=14, command=lambda: show_simple_options())
button_connect.pack(side=tk.LEFT)
# Complex Caesar encryption button
button_connect = tk.Button(encryption_type_block, text="Complex", font=14, command=lambda: show_complex_options())
button_connect.pack(side=tk.RIGHT)

### SIMPLE ENCRYPTION OPTIONS ###
# Dropdown options
dropbox_options = [i for i in range(1, 25)]
dropbox_menu = tk.StringVar(simple_options_block)
dropbox_menu.set(dropbox_options[0])
simple_key = dropbox_options[0]

# Update key, when dropdown is used
def update_key(selection):
    global simple_key
    simple_key = selection

# Key dropdown
label_drop_key = tk.Label(simple_options_block, text="Key:", font=14)
label_drop_key.pack(side=tk.TOP)
drop_key = tk.OptionMenu(simple_options_block, dropbox_menu, *dropbox_options, command=update_key)
drop_key.pack(side=tk.TOP)
# Caesar encryption button
button_connect = tk.Button(simple_options_block, text="Encrypt!", font=14, command=lambda: simple_caesar_encryption())
button_connect.pack(side=tk.LEFT)
# Caesar decryption button
button_connect = tk.Button(simple_options_block, text="Decrypt!", font=14, command=lambda: simple_caesar_decryption())
button_connect.pack(side=tk.RIGHT)

### COMPLEX ENCRYPTION OPTIONS ###
# Key dropdown
label_entry_key = tk.Label(complex_options_block, text="Key:", font=14)
label_entry_key.pack(side=tk.TOP)
entry_key = tk.Entry(complex_options_block, font=14)
entry_key.pack(side=tk.TOP)
# Caesar encryption button
button_connect = tk.Button(complex_options_block, text="Encrypt!", font=14, command=lambda: complex_caesar_encryption)
button_connect.pack(side=tk.LEFT)
# Caesar decryption button
button_connect = tk.Button(complex_options_block, text="Decrypt!", font=14, command=lambda: complex_caesar_decryption())
button_connect.pack(side=tk.RIGHT)

### DISPLAYING BLOCKS ###
plaintext_block.pack(side=tk.TOP, padx=(15, 15), pady=(10, 10))
caesartext_block.pack(side=tk.TOP, padx=(15, 15), pady=(10, 10))
encryption_type_block.pack(side=tk.TOP, padx=(15, 15), pady=(10, 10))

# Simple caesar encryption
def simple_caesar_encryption():
    global simple_key
    plaintext = entry_plain.get()
    caesartext = ""

    for i in range(len(plaintext)):
        special = plaintext[i]
        new_special = special.lower()

        if new_special == " ":
            caesartext += ' '
        elif special.isalpha():
            caesartext += chr((ord(new_special) + simple_key - 97) % 26 + 97)

    entry_caesar.config(state=tk.NORMAL)
    entry_caesar.delete(0, tk.END)
    entry_caesar.insert(tk.END, caesartext)
    entry_caesar.config(state=tk.DISABLED)

# Simple caesar decryption
def simple_caesar_decryption():
    global simple_key
    plaintext = entry_plain.get()
    caesartext = ""

    for i in range(len(plaintext)):
        special = plaintext[i]
        new_special = special.lower()

        if new_special == " ":
            caesartext += ' '
        elif special.isalpha():
            caesartext += chr((ord(new_special) - simple_key - 97) % 26 + 97)

    entry_caesar.config(state=tk.NORMAL)
    entry_caesar.delete(0, tk.END)
    entry_caesar.insert(tk.END, caesartext)
    entry_caesar.config(state=tk.DISABLED)

def split(key):
    return list(key)

# Complex caesar encryption
def complex_caesar_encryption():
    plaintext = entry_plain.get()
    complex_key = entry_key.get()
    complex_key = complex_key.replace(" ", "")
    complex_key = complex_key.lower()
    key = split(complex_key)
    caesartext = ""

    for i in range(len(plaintext)):
        special = plaintext[i]
        new_special = special.lower()

        if new_special == " ":
            caesartext += ' '
        elif special.isalpha():
            caesartext += chr((ord(new_special) + complex_key - 97) % 26 + 97)

    entry_caesar.config(state=tk.NORMAL)
    entry_caesar.delete(0, tk.END)
    entry_caesar.insert(tk.END, caesartext)
    entry_caesar.config(state=tk.DISABLED)

# Complex caesar decryption
def complex_caesar_decryption():
    caesartext = entry_plain.get()
    complex_key = entry_key.get()
    plaintext = ""

    for i in range(len(caesartext)):
        special = caesartext[i]
        new_special = special.lower()
        
        if new_special == " ":
            plaintext += ' '
        elif special.isalpha():
            plaintext += chr((ord(new_special) - complex_key - 97) % 26 + 97)

    entry_caesar.config(state=tk.NORMAL)
    entry_caesar.delete(0, tk.END)
    entry_caesar.insert(tk.END, plaintext)
    entry_caesar.config(state=tk.DISABLED)

def show_simple_options():
    complex_options_block.forget()
    simple_options_block.pack(side=tk.BOTTOM, padx=(15, 15), pady=(10, 15))

def show_complex_options():
    simple_options_block.forget()
    complex_options_block.pack(side=tk.BOTTOM, padx=(15, 15), pady=(10, 15))

# Loop GUI window
window.mainloop()
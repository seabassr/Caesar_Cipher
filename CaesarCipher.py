import tkinter as tk

# GUI setup
window = tk.Tk()
window.title("Caesar Cipher")

# Plain text entry
plaintext_block = tk.Frame(window)
# Buttons for simple and complex
encryption_block = tk.Frame(window)
# Key dropdown, and encryption/decryption buttons
options_block = tk.Frame(window)
# Caesar text display
caesartext_block = tk.Frame(window)

# PLAINTEXT
# Plain text entry
label_plain = tk.Label(plaintext_block, text="Plain Text:", font=14)
label_plain.pack(side=tk.TOP)
entry_plain = tk.Entry(plaintext_block, font=14)
entry_plain.config(highlightbackground="grey")
entry_plain.pack(side=tk.TOP, pady=(5, 10))

# ENCRYPTION
# Simple Caesar encryption button
button_connect = tk.Button(encryption_block, text="Simple", font=14, command=lambda: caesar_encryption())
button_connect.pack(side=tk.LEFT, pady=(5, 10))

# Complex Caesar encryption button
button_connect = tk.Button(encryption_block, text="Complex", font=14, command=lambda: caesar_encryption())
button_connect.pack(side=tk.RIGHT, pady=(5, 10))

# OPTIONS
# Dropdown options
dropbox_options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
dropbox_menu = tk.StringVar(options_block)
dropbox_menu.set(dropbox_options[0])
key = dropbox_options[0]

# Update key, when dropdown is used
def update_key(selection):
    global key
    key = selection

# Key dropdown
label_key = tk.Label(options_block, text="Key:", font=14)
label_key.pack(side=tk.TOP)
entry_key = tk.OptionMenu(options_block, dropbox_menu, *dropbox_options, command=update_key)
entry_key.pack(side=tk.TOP, pady=(5, 10))


# Caesar encryption button
button_connect = tk.Button(options_block, text="Encrypt!", font=14, command=lambda: caesar_encryption())
button_connect.pack(side=tk.LEFT, pady=(5, 10))

# Caesar decryption button
button_connect = tk.Button(options_block, text="Decrypt!", font=14, command=lambda: caesar_decryption())
button_connect.pack(side=tk.RIGHT, pady=(5, 10))

# CAESARTEXT
# Caesar text display
label_caesar = tk.Label(caesartext_block, text="Caesar Text:", font=14)
label_caesar.pack(side=tk.TOP)
entry_caesar = tk.Entry(caesartext_block, font=14)
entry_caesar.config(highlightbackground="grey", state="disabled")
entry_caesar.pack(side=tk.TOP, pady=(5, 10))

# Display blocks
plaintext_block.pack(side=tk.TOP, padx=(15, 15), pady=(10, 10))
encryption_block.pack(side=tk.TOP, padx=(15, 15), pady=(10, 10))
options_block.pack(side=tk.TOP, padx=(15, 15), pady=(10, 10))
caesartext_block.pack(side=tk.TOP, padx=(15, 15), pady=(10, 10))

# Simple caesar encryption
def caesar_encryption():
    global key
    plaintext = entry_plain.get()
    caesartext = ""

    for i in range(len(plaintext)):
        special = plaintext[i]
        new_special = special.lower()
        if new_special == " ":
            caesartext += ' '
        elif special.isalpha():
            caesartext += chr((ord(new_special) + key - 97) % 26 + 97)

    entry_caesar.config(state=tk.NORMAL)
    entry_caesar.delete(0, tk.END)
    entry_caesar.insert(tk.END, caesartext)
    entry_caesar.config(state=tk.DISABLED)

# Simple caesar decryption
def caesar_decryption():
    global key
    plaintext = entry_plain.get()
    caesartext = ""

    for i in range(len(plaintext)):
        special = plaintext[i]
        new_special = special.lower()
        if new_special == " ":
            caesartext += ' '
        elif special.isalpha():
            caesartext += chr((ord(new_special) - key - 97) % 26 + 97)

    entry_caesar.config(state=tk.NORMAL)
    entry_caesar.delete(0, tk.END)
    entry_caesar.insert(tk.END, caesartext)
    entry_caesar.config(state=tk.DISABLED)

# Loop GUI window
window.mainloop()
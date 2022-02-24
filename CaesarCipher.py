import tkinter as tk

# GUI
window = tk.Tk()
window.title("Caesar Cipher")

# Plain text and key block
top_block = tk.Frame(window)

# Plain text
label_plain = tk.Label(top_block, text="Plain Text:", font=14)
label_plain.pack(side=tk.TOP)
entry_plain = tk.Entry(top_block, font=14)
entry_plain.config(highlightbackground="grey")
entry_plain.pack(side=tk.TOP, pady=(5, 10))

options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
variable = tk.StringVar(top_block)
variable.set(options[0])
key = options[0]

def update_key(selection):
    global key
    key = selection

# Key
label_key = tk.Label(top_block, text="Key:", font=14)
label_key.pack(side=tk.TOP)
entry_key = tk.OptionMenu(top_block, variable, *options, command=update_key)
entry_key.pack(side=tk.TOP, pady=(5, 10))
top_block.pack(side=tk.TOP, padx=(15, 15), pady=(10, 10))

# Caesar button block
middle_block = tk.Frame(window)

# Caesar encryption button
button_connect = tk.Button(middle_block, text="Encrypt!", font=14, command=lambda: caesar_encryption())
button_connect.pack(side=tk.LEFT, pady=(5, 10))

# Caesar decryption button
button_connect = tk.Button(middle_block, text="Decrypt!", font=14, command=lambda: caesar_decryption())
button_connect.pack(side=tk.RIGHT, pady=(5, 10))
middle_block.pack(side=tk.TOP, padx=(15, 15), pady=(10, 10))

# Caesar text block
bottom_block = tk.Frame(window)

# Caesar text
label_caesar = tk.Label(bottom_block, text="Caesar Text:", font=14)
label_caesar.pack(side=tk.TOP)
entry_caesar = tk.Entry(bottom_block, font=14)
entry_caesar.config(highlightbackground="grey", state="disabled")
entry_caesar.pack(side=tk.TOP, pady=(5, 10))
bottom_block.pack(side=tk.TOP, padx=(15, 15), pady=(10, 10))

L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

def caesar_encryption():
    global key
    plaintext = entry_plain.get()
    caesartext = ""

    for c in plaintext.upper():
        if c.isalpha():
            caesartext += I2L[ (L2I[c] + key)%26 ]
        else:
            caesartext += c

    entry_caesar.config(state=tk.NORMAL)
    entry_caesar.delete(0, tk.END)
    entry_caesar.insert(tk.END, caesartext)
    entry_caesar.config(state=tk.DISABLED)

def caesar_decryption():
    global key
    plaintext = entry_plain.get()
    caesartext = ""
    
    for c in plaintext.upper():
        if c.isalpha():
            caesartext += I2L[ (L2I[c] - key)%26 ]
        else:
            caesartext += c

    entry_caesar.config(state=tk.NORMAL)
    entry_caesar.delete(0, tk.END)
    entry_caesar.insert(tk.END, caesartext)
    entry_caesar.config(state=tk.DISABLED)

# Loop GUI window
window.mainloop()
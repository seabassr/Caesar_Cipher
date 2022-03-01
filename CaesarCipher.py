import tkinter as tk

# GUI SETUP #
root = tk.Tk()
root.title("Caesar Cipher")
root.resizable(False, False)
# Setting GUI variables
background_color = 'black'
highlight_color2 = 'grey'
font_size = 16
entry_width = 40
button_width = 6
padding_x = 20
padding_y = 20
# Setting GUI background
background_image = tk.PhotoImage(file="glitch.png")
label_bg = tk.Label(root, image=background_image, bg=background_color)
label_bg.place(x=0, y=0)

# Plain text entry
plaintext_block = tk.Frame(root, bg=background_color)
# Buttons for simple and complex
encryption_type_block = tk.Frame(root, bg=background_color)
# Caesar text display
ciphertext_block = tk.Frame(root, bg=background_color)
# Key dropdown, and encryption/decryption buttons
simple_options_block = tk.Frame(root, bg=background_color)
simple_button_block = tk.Frame(simple_options_block, bg=background_color)
# Key entry, and encryption/decryption buttons
complex_options_block = tk.Frame(root, bg=background_color)
complex_button_block = tk.Frame(complex_options_block, bg=background_color)

# PLAINTEXT #
# Plain text entry
label_plain = tk.Label(plaintext_block, text="Plain Text:", font=font_size, bg=background_color)
label_plain.pack(side=tk.TOP)
entry_plain = tk.Entry(plaintext_block, font=font_size, width=entry_width)
entry_plain.config(highlightbackground=highlight_color2)
entry_plain.pack(side=tk.TOP)

# CAESAR TEXT #
# Caesar text display
label_caesar = tk.Label(ciphertext_block, text="Caesar Text:", font=font_size, bg=background_color)
label_caesar.pack(side=tk.TOP)
entry_caesar = tk.Entry(ciphertext_block, font=font_size, width=entry_width)
entry_caesar.config(highlightbackground=highlight_color2, state="disabled")
entry_caesar.pack(side=tk.TOP)

# ENCRYPTION TYPE #
# Simple Caesar encryption button
button_simple = tk.Button(encryption_type_block, text="Simple", font=font_size, width=button_width,
                          highlightbackground=background_color, command=lambda: show_simple_options())
button_simple.pack(side=tk.LEFT)
# Complex Caesar encryption button
button_complex = tk.Button(encryption_type_block, text="Complex", font=font_size, width=button_width,
                           highlightbackground=background_color, command=lambda: show_complex_options())
button_complex.pack(side=tk.RIGHT)

# SIMPLE ENCRYPTION OPTIONS #
# Dropdown options
dropbox_options = [i for i in range(1, 26)]
dropbox_menu = tk.StringVar(simple_options_block)
dropbox_menu.set("1")
simple_key = dropbox_options[0]


# Update key, when dropdown is used
def update_key(selection):
    global simple_key
    simple_key = selection


# Key dropdown
label_drop_key = tk.Label(simple_options_block, text="Key:", font=font_size, bg=background_color)
label_drop_key.pack(side=tk.TOP)
drop_key = tk.OptionMenu(simple_options_block, dropbox_menu, *dropbox_options, command=update_key)
drop_key.pack(side=tk.TOP)
# Caesar encryption button
button_simple_encrypt = tk.Button(simple_button_block, text="Encrypt", font=font_size, width=button_width,
                                  highlightbackground=background_color, command=lambda: simple_caesar_encryption())
button_simple_encrypt.pack(side=tk.LEFT)
# Caesar decryption button
button_simple_decrypt = tk.Button(simple_button_block, text="Decrypt", font=font_size, width=button_width,
                                  highlightbackground=background_color, command=lambda: simple_caesar_decryption())
button_simple_decrypt.pack(side=tk.RIGHT)

# COMPLEX ENCRYPTION OPTIONS #
# Key dropdown
label_entry_key = tk.Label(complex_options_block, text="Key:", font=font_size, bg=background_color)
label_entry_key.pack(side=tk.TOP)
entry_key = tk.Entry(complex_options_block, font=font_size, width=entry_width, highlightbackground=highlight_color2)
entry_key.pack(side=tk.TOP)
# Caesar encryption button
button_complex_encrypt = tk.Button(complex_button_block, text="Encrypt", font=font_size, width=button_width,
                                   highlightbackground=background_color, command=lambda: complex_caesar_encryption())
button_complex_encrypt.pack(side=tk.LEFT)
# Caesar decryption button
button_complex_decrypt = tk.Button(complex_button_block, text="Decrypt", font=font_size, width=button_width,
                                   highlightbackground=background_color, command=lambda: complex_caesar_decryption())
button_complex_decrypt.pack(side=tk.RIGHT)

# DISPLAYING BLOCKS #
plaintext_block.pack(side=tk.TOP, padx=(padding_x, padding_x), pady=(padding_y, padding_y))
ciphertext_block.pack(side=tk.TOP, padx=(padding_x, padding_x), pady=(padding_y, padding_y))
encryption_type_block.pack(side=tk.TOP, padx=(padding_x, padding_x), pady=(padding_y, padding_y))


# SHOW METHODS #
# Show simple encryption options
def show_simple_options():
    # Reset key dropdown menu
    global simple_key
    dropbox_menu.set("1")
    simple_key = dropbox_options[0]

    # Disable simple button, and enable complex button
    button_simple.config(state="disabled")
    button_complex.config(state="normal")
    # Hide complex options, show simple options
    complex_options_block.forget()
    simple_options_block.pack(side=tk.BOTTOM, padx=(15, 15), pady=(10, 15))
    simple_button_block.pack(side=tk.BOTTOM)


# Show complex encryption options
def show_complex_options():
    # Disable complex button, and enable simple button
    button_complex.config(state="disabled")
    button_simple.config(state="normal")
    # Hide simple options, show complex options
    simple_options_block.forget()
    complex_options_block.pack(side=tk.BOTTOM, padx=(15, 15), pady=(10, 15))
    complex_button_block.pack(side=tk.BOTTOM)


# USED IN ENCRYPTION AND DECRYPTION METHODS #
symbols_list = ["$", "@", "%", "!", "*", ".", ","]


def symbol_to_letters(letter):
    # Add special text to ciphertext
    if letter == "$":
        return '/s'
    elif letter == "@":
        return '/a'
    elif letter == "%":
        return '/p'
    elif letter == "!":
        return '/e'
    elif letter == "*":
        return '/t'
    elif letter == ".":
        return '/q'
    elif letter == ",":
        return '/c'


def letters_to_symbols(letter):
    # Add symbol to plaintext
    if letter == "s":
        return '$'
    elif letter == "a":
        return '@'
    elif letter == "p":
        return '%'
    elif letter == "e":
        return '!'
    elif letter == "t":
        return '*'
    elif letter == "q":
        return '.'
    elif letter == "c":
        return ','


def update_caesar_box(text):
    # Display text
    entry_caesar.config(state=tk.NORMAL)
    entry_caesar.delete(0, tk.END)
    entry_caesar.insert(tk.END, text)
    entry_caesar.config(state=tk.DISABLED)


# Convert key into numbers
def letters_to_numbers(complex_key):
    # List will hold each letter value
    convert = []

    # Turn letters into numbers, and add to list
    for letter in complex_key:
        convert.append(ord(letter) - 96)

    # Return list
    return convert


# SIMPLE ENCRYPTION METHODS #
# Simple caesar encryption
def simple_caesar_encryption():
    # Get key and plaintext
    global simple_key
    plaintext = entry_plain.get()
    ciphertext = ""

    # Loop through plain text, and go forwards base on key
    for i in range(len(plaintext)):
        letter = plaintext[i]
        letter = letter.lower()

        # If space detected, add space, else encrypt
        if letter == " ":
            ciphertext += ' '
        elif any(symbols in letter for symbols in symbols_list):
            ciphertext += symbol_to_letters(letter)
        elif letter.isalpha():
            ciphertext += chr((ord(letter) + simple_key - 97) % 26 + 97)

    # Display encrypted text
    update_caesar_box(ciphertext)


# Simple caesar decryption
def simple_caesar_decryption():
    # Get key and encrypted text
    global simple_key
    ciphertext = entry_plain.get()
    plaintext = ""
    # If there isn't any symbols
    skip = -1

    # Loop through encrypted text, and go backwards base on key
    for i in range(len(ciphertext)):
        letter = ciphertext[i]
        letter = letter.lower()

        if skip == i:
            # If used as symbol, skip
            continue
        elif letter == " ":
            # If space detected, add space, else decrypt
            plaintext += ' '
        elif letter == "/":
            # Add symbol to plaintext, skip the next letter
            skip = i + 1
            letter = ciphertext[skip]
            letter = letter.lower()
            plaintext += letters_to_symbols(letter)
        elif letter.isalpha():
            plaintext += chr((ord(letter) - simple_key - 97) % 26 + 97)

    # Display plain text
    update_caesar_box(plaintext)


# COMPLEX ENCRYPTION METHODS #
# Complex caesar encryption
def complex_caesar_encryption():
    # Get plaintext and key
    plaintext = entry_plain.get()
    complex_key = entry_key.get()
    ciphertext = ""

    if len(complex_key) < 1:
        ciphertext = "INVALID KEY"
    else:
        # Remove spaces and lowercase everything in key
        complex_key = complex_key.replace(" ", "")
        complex_key = complex_key.lower()
        # Convert letters to number, get length of list
        key_list = letters_to_numbers(complex_key)
        key_length = len(key_list)
        key_position = 0

        # Loop through plain text, and go forwards base on key
        for i in range(len(plaintext)):
            letter = plaintext[i]
            letter = letter.lower()

            if letter == " ":
                # If space detected, add space, else encrypt
                ciphertext += ' '
            elif any(symbols in letter for symbols in symbols_list):
                ciphertext += symbol_to_letters(letter)
            elif letter.isalpha():
                # Loop numbers in key, if smaller than plain text
                if key_position < key_length:
                    key = key_list[key_position]
                    key_position += 1
                else:
                    key_position = 0
                    key = key_list[key_position]

                ciphertext += chr((ord(letter) + int(key) - 97) % 26 + 97)

    # Display encrypted text
    update_caesar_box(ciphertext)


# Complex caesar decryption
def complex_caesar_decryption():
    # Get encrypted text and key
    ciphertext = entry_plain.get()
    complex_key = entry_key.get()
    plaintext = ""

    if len(complex_key) < 1:
        plaintext = "INVALID KEY"
    else:
        # Remove spaces and lowercase everything in key
        complex_key = complex_key.replace(" ", "")
        complex_key = complex_key.lower()
        # Convert letters to number, get length of list
        key_list = letters_to_numbers(complex_key)
        key_length = len(key_list)
        key_position = 0
        # If there isn't any symbols
        skip = -1

        # Loop through encrypted text, and go backwards base on key
        for i in range(len(ciphertext)):
            letter = ciphertext[i]
            letter = letter.lower()

            if skip == i:
                # If used as symbol, skip
                continue
            elif letter == " ":
                # If space detected, add space, else decrypt
                plaintext += ' '
            elif letter == "/":
                # Add symbol to plaintext, skip the next letter
                skip = i + 1
                letter = ciphertext[skip]
                letter = letter.lower()
                plaintext += letters_to_symbols(letter)
            elif letter.isalpha():
                # Loop numbers in key, if smaller than encrypted text
                if key_position < key_length:
                    key = key_list[key_position]
                    key_position += 1
                else:
                    key_position = 0
                    key = key_list[key_position]

                plaintext += chr((ord(letter) - int(key) - 97) % 26 + 97)

    # Display plain text
    update_caesar_box(plaintext)


# LOOP GUI WINDOW #
root.mainloop()

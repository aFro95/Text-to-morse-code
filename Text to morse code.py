print("Welcome Text to Morse Code Converter. The place to keep your messages a secret")
message = input('Message to convert to Morse Code: ')
space_letters = '   '
space_words = '       '
morse_code_dict = {'a': '. ___',
                   'b': '___ . . .',
                   'c': '___ . ___ .',
                   'd': '___ . .',
                   'e': '.',
                   'f': '. . ___ ',
                   'g': '___ ___ .',
                   'h': '. . . .',
                   'i': '. .',
                   'j': '. ___ ___ ___',
                   'k': '___ . ___',
                   'l': '. ___ . .',
                   'm': '___ ___',
                   'n': '___ .',
                   'o': '___ ___ ___',
                   'p': '. ___ ___ .',
                   'q': '___ ___ . ___',
                   'r': '. ___ .',
                   's': '. . .',
                   't': '___',
                   'u': '. . ___',
                   'v': '. . . ___',
                   'w': '. ___ ___',
                   'x': '___ . . ___',
                   'y': '___ . ___ ___',
                   'z': '___ ___ . .',
                   '0': '___ ___ ___ ___ ___',
                   '1': '. ___ ___ ___ ___',
                   '2': '. . ___ ___ ___',
                   '3': '. . . ___ ___',
                   '4': '. . . . ___',
                   '5': '. . . . .',
                   '6': '___ . . . .',
                   '7': '___ ___ . . .',
                   '8': '___ ___ ___ . .',
                   '9': '___ ___ ___ ___ .'}

msg_split = message.lower().split()
cipher_text = ''
if len(msg_split) == 1:
    letters = msg_split[0].split()
    for letter in msg_split[0]:
        morse_code = morse_code_dict[letter]
        cipher_text += morse_code
        cipher_text += space_letters
elif len(msg_split) > 1:
    for word in msg_split:
        for letter in word:
            morse_code = morse_code_dict[letter]
            cipher_text += morse_code
            cipher_text += space_letters
        cipher_text += space_words
print(f"Your morse coded text: {cipher_text}")
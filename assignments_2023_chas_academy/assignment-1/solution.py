def solution(input_string):
    #lowercase alphabet ordered a-z and same alphabet but in reversed order z-a
    import string
    alphabet = (string.ascii_lowercase)
    alphabet_reverse = (string.ascii_lowercase[::-1])
    string = ""

    #loop characters in text: add reversed letters and add symbols the same as they look.
    text = [*input_string]
    for letter in text:
        if letter in alphabet:
            alfabet_position = alphabet.index(letter)
            string += alphabet_reverse[alfabet_position]
        else:
            string += letter

    return string

def camelcase(words):
    '''Convert word to have uppercase first leter, rest in lowercase'''
    output =''
    words = words.split(' ')                                        # Break by spaces
    output += (words[0].lower())                             # Lowercase first word
    for word in words[1:]:
        output += (word[0].upper() + word[1:].lower())   # camelCase everything

    return output
    # Slices don't produce index out of bounds errors.
    # So this still works on empty strings, strings of length 1

def display_banner():
    '''Display program name in a banner'''
    msg = 'AWESOME camelCaseGenerator PROGRAM'
    stars = '*' * len(msg)
    print('\n', stars, '\n', msg, '\n',  stars, '\n')

def display_instruction():
    '''Display program instruction'''
    instruction = "Enter a sentence to convert to camelcase.\nEach words will change with camelcase\n"

    print(instruction)

def main():

    display_banner()

    display_instruction()

    words = input('Enter your sentence:  ')
    output = camelcase(words)
    print(output)


if __name__ == '__main__':
    main()

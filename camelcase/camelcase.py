def camelcase(words):
    '''Convert word to have uppercase first leter, rest in lowercase'''
    words = words.strip()   # Strip leading and following spaces

    # Add to a new string newWords if the character is alpha numeric or space
    newWords = ''
    for c in words:
        if c.isalnum() or c == ' ':
            newWords += c

    newWords = newWords.split(' ')  # Break by spaces

    output = ''

    output += (newWords[0].lower())                      # Lowercase first word
    for word in newWords[1:]:
        if word == '':                                  # Removes empty indexes
            newWords.remove(word)
        else:
            output += (word[0].upper() + word[1:].lower())   # camelCase everythingelse

    return output


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

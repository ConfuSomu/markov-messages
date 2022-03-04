import random
import sys

import format

USAGE_MESSAGE = f"""Usage:
    {sys.argv[0]} {format.ANSI.underline}messages file{format.ANSI.reset} {format.ANSI.underline}length (words) of generated message{format.ANSI.reset}"""

# Generate a markov chain from a text file containing messages
# length is the number of words that the generated message will contain
# function taken from https://medium.com/analytics-vidhya/making-a-text-generator-using-markov-chains-e17a67225d10 or https://gist.github.com/hiowatah/7542d41740ebe7b3441b8634ea0501eb#file-markov_chains
def markov(messages_text_file, length):
    messages = open(messages_text_file, 'r').read()
    messages = ''.join([i for i in messages if not i.isdigit()]).replace("\n", " ").split(' ')
    
    index = 1
    chain = {}
    
    for word in messages[index:]:
        key = messages[index-1]
        if key in chain:
            chain[key].append(word)
        else:
            chain[key] = [word]
        index += 1
    
    word1 = random.choice(list(chain.keys()))
    message = word1.capitalize()

    while len(message.split(' ')) < length:
        word2 = random.choice(chain[word1])
        word1 = word2
        message += ' ' + word2
    return message

if __name__ == "__main__":
    try:
        print(markov(sys.argv[1], int(sys.argv[2])))
    except IndexError:
        sys.exit(USAGE_MESSAGE)
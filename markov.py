"""Generate Markov text from text files."""

from random import choice

file_path = "green-eggs.txt"

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text_file = open(file_path, mode='r') #mode=r means you can read but not edit file when opened
    all_of_it = text_file.read()

   
    return all_of_it 


def make_chains(text_string) :
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

   # text_string is all_of_it
   # split string by whitespace words = split string
    
    words = text_string.split() #leave blank to capture all white space characters


    for i in range(len(words) - 2):
        
        chains_key = (words[i], words[i+1]) #{('could', 'you')}
        # print(chains_key)
        chains_value = words[i + 2] #"you"
       
        if chains_key not in chains:
            chains[chains_key] = []
            
        chains[chains_key].append(chains_value)


    print(chains)

make_chains(open_and_read_file(file_path))


""" 

dict = {'blue', [1, 3, 5]}

dict[blue] = 



"""






def make_text(chains):
    """Return text from chains."""

    words = []

    

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)

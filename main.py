# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content():

    # [assignment] Add your code here
    with open(r"./story.txt", "r") as file:

    #read content of file to string   
        data = file.read()
        
        return data


print(read_file_content())

def count_words():
    text = read_file_content()
    # [assignment] Add your code here
 
    word1 = text.count("glass")
    word2 = text.count("professor")

    dictionary = {"glass": word1, "professor": word2}
    return(dictionary)

print(count_words())
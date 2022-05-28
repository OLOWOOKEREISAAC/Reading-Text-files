def read_file_content(filename):
    with open(filename  , 'r') as open_file:
        file = open_file.read()
    return file
    

def count_words():
    text = read_file_content("C:/Users/Kenny/Desktop/ME/zuri/BE/Reading-Text-Files/story.txt")
    each_word = text.split()
    word_count = {}
    for words in each_word:
        if words in word_count:
            word_count[words] += 1
        else:
            word_count[words] = 1
    
    print(word_count)

read_file_content("C:/Users/Kenny/Desktop/ME/zuri/BE/Reading-Text-Files/story.txt")
count_words()
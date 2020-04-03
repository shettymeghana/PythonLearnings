#Write a python program to find the number of characters, word and lines in input text which is provided by user

def wordCount(input_text):  #To count the word in provided multiline string
    word_count = 0
    for item in input_text:
        word_count = word_count + len(item.split())
    print "Number of words in provied multiline user input are: ",word_count

def charCount(input_text): #To count the characters in provided multiline string
    char_count = 0
    for item in input_text:
        char_count += len(item)
    print "Number of characters in provied multiline user input are: ",char_count

def lineCount(input_text):
    print "Number of lines in provied multiline user input are: ", len(input_text)

def main(): #to take multiline strings from user
    print "Enter your content. Ctrl-D or Ctrl-Z ( windows ) to save it.\nEnter text here\n"
    input_text = []
    while True:
        try:
            line = raw_input('')
        except EOFError:
            break
        input_text.append(line)
    wordCount(input_text)
    charCount(input_text)
    lineCount(input_text)

if __name__ == '__main__':
    main()

#Read text file and print words count present in text file.
def main():
    f = open('meghu.txt','w+')
    for i in range(0,10):
        f.write("This is line %d\n"%(i+1))
    f.close()
    # Read the entire file
    f = open('meghu.txt','r')
    if f.mode == 'r':
        contents = f.read()
        print "**********Reading entire file********\n",contents
        #print "====+======+=======+======+=======+"
    f = open('meghu.txt', 'r')
    if f.mode == 'r':
        f1 = f.readlines()
        print "*********Reading line by line*********\n"
        for x in f1:
            print x
    f = open('meghu.txt','a+')
    for i in range(2):
        f.write("Appended line %d\n"%(i+1))
    f.close()
    f = open('meghu.txt','r')
    if f.mode == 'r':
        contents1 = f.read()
        print "**********Reading entire file after Append********\n", contents1
        l = len(contents1.splitlines())
        word_count = contents1.split()
        #Sprint word_count
        print "Number of words in meghu.txt is %d" %len(word_count)
        print "Number of lines in meghu.txt is %d" %l
if __name__ == '__main__':
    main()



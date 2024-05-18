import sys


def read_txt(file_name):
    with open(file_name, 'r') as f:
        text = f.read()
    return text

def count_characters(file_name):
        count_ch = 0
        for ch in read_txt(file_name):
            count_ch+=1
        return count_ch

def count_lines(file_name):
        count_ln = 0
        for ch in read_txt(file_name):  
            if ch=='\n':
                count_ln+=1
        if count_ln!=0:
            count_ln+=1 #last line without '\n'
        return count_ln

def count_words(file_name):
        count_words =  0
        for w in read_txt(file_name).split():
            count_words+=1
        return count_words

def main():
    if len (sys.argv)!=2:
        exit(f"Usage: {sys.argv[0]} FileName")
        
    file_name = sys.argv[1]
    characters, lines, words = count_characters(file_name), count_lines(file_name), count_words(file_name)
    print(f"characters:{characters}, lines:{lines}, words:{words}")

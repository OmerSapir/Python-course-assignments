import sys

def count(file_name):
    count_dict = {'characters': 0, 'words': 0, 'lines': 0} 
    with open(file_name, 'r') as f:
        text = f.read()
        for ch in text:
            count_dict['characters']+=1
            if ch=='\n':
                count_dict['lines']+=1
        if count_dict['lines']!=0:
            count_dict['lines']+=1 #last line without '\n'
        for w in text.split():
            count_dict['words']+=1
    return count_dict



def main():
    if len (sys.argv)!=2:
        exit(f"Usage: {sys.argv[0]} FileName")
        
    file_name = sys.argv[1]
    result = count(file_name)
    print(result)


main()
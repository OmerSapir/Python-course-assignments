def count(file_name):
    count_dict = {'characters': 0, 'words': 0, 'lines': 0} 
    with open(file_name) as fn:
        text = fn.read()
        for ch in text:
            count_dict['characters']+=1
            if ch=='\n':
                count_dict['lines']+=1
        if count_dict['lines']!=0:
            count_dict['lines']+=1 #last line without '\n'
        for w in text.split():
            count_dict['words']+=1
    print(count_dict)
def count_words(filename):
    try:
        with open(filename) as f:
            content = f.read()
    except:
        return f'The file {filename} doesnt exist'
    else:
        words = content.split()
        num_words = len(words)
        return f'The file {filename} has {num_words} words'
        
        
        
if __name__ == '__main__':
    files = ['second_act/guest_book.txt', 'second_act/guest.txt', 'text.txt']
    for e in files:
        print(count_words(e)) # relative file names_guest
    
    
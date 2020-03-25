import string

def main():
    dict1 = {}
    file_input = open('61654.txt', encoding='utf8')
    book_file = file_input
    exclude = set(string.punctuation)
    book_file = ''.join(chr for chr in book_file if chr not in exclude)
    book_file = book_file.lower()
    word_list = book_file.split()
    
    for i in word_list:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] += 1

    words = list(dict1.items())
    words.sort(key=lambda tup: tup[1], reverse=True)
    for i in range(min(10, len(words))):
        print(words[i])
    
main()
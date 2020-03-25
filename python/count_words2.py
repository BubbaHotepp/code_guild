import string

def main():
    dict1 = {}
    file_input = open('pg61664.txt', encoding='utf8') #pg61664.txt or 61654.txt
    book_file = file_input
    exclude = set(string.punctuation)
    book_file = ''.join(chr for chr in book_file if chr not in exclude)
    book_file = book_file.lower()
    word_list = book_file.split()
    
    for i in word_list and (i+1) in word_list:
        if i not in dict1:
            dict1[i] = 0
        else:
            dict1[] += 1

    words = list(dict1.items()) # .items() returns a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        print(words[i])
    
main()

# if i in word_list and (i+1) in word_list:
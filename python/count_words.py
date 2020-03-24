import string

def main():
    dict1 = {}
    file_input = open('61654.txt', encoding='utf8')
    book_file = file_input
    exclude = set(string.punctuation)
    book_file = ''.join(ch for ch in book_file if ch not in exclude)
    book_file = book_file.lower()
    book_file = book_file.split()
    length = len(book_file)
    count = 0
    while count < length:
        for i in book_file:
            if i != dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1
        count += 1        
    words = list(dict1.items()) # .items() returns a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        print(words[i])
    
main()
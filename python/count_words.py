import string
# def word_counter():
#     stuff here

def main():
    dict1 = {}
    file_input = open('61654.txt', encoding='utf8')
    book_file = file_input
    exclude = set(string.punctuation)
    book_file = ''.join(ch for ch in book_file if ch not in exclude)
    book_file = book_file.lower()
    book_file = book_file.split()
    length = len(book_file)
    while length > 0:
        for i in book_file:
            if i != dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1
        length -= 1        
    # print("Occurrences of the word:")
    # print(k)
    print(dict1)
main()
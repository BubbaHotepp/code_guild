import string

def main():
    dict1 = {}
    file_input = open('61654.txt', encoding='utf8') #pg61664.txt or 61654.txt
    book_file = file_input
    exclude = set(string.punctuation)
    book_file = ''.join(chr for chr in book_file if chr not in exclude)
    book_file = book_file.lower()
    word_list = book_file.split()

    for i in range(len(word_list) - 1):
        word_pair = str(word_list[i] + ' ' + word_list[i + 1])
        if word_pair not in dict1:
            dict1[word_pair] = 1
        else:
            dict1[word_pair] += 1

    pairs = list(dict1.items()) 
    pairs.sort(key=lambda tup: tup[1], reverse=True)
    for i in range(min(10, len(pairs))):  
        print(pairs[i])
    
main()
import string

# def main():
#     user_input = input('Please enter plain text to encode: ')

#     code_chart = string.ascii_letters

#     print(code_chart)

#     x = 13

#     y = [code_chart[(code_chart.find(i) + x) % 26] for i in user_input]

#     encode = "".join(y)
    
#     print(encode)

# main()  

def encode(x):
   
    def convert(x):
        
        y, i = ord(x), x.lower()
        
        return chr((y + 13)%26)
        
        
        return x
    
    return ''.join(map(convert, x))

print(encode('Hello World'))


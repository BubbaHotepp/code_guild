import random

def eyes():
    eye_list = [':',';','=','|','8']
    return random.choice(eye_list)

def nose():
    nose_list = ['-','','^','*']
    return random.choice(nose_list)
    
def mouth():
    mouth_list = ['O','D','P','(','/','>',')']
    return random.choice(mouth_list)

def main():
    print('Welcome to the random Emoticon Generator.\n')
    print(f'Here is your emoticon: {eyes()}{nose()}{mouth()}')
    
main()
    
    
  




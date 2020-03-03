import random

def user_question(x):
    print('Welcome diviner! Prepare to be astonished at the power of 8.')
    x = input('Ask your question of the mystical Magic 8 Ball!!')
    return x

def answers_list(x):
    x = ['It is certain.', 'You can count on it.', 'No doubt fool.', 'Pretty sure.', 'Well, it could be.', 'Absolutely.', 'Yes!', 'No!', 'I really shouldn\'t tell you that.', 'Ask me again later.', 'The future is uncertain right now.', 'I wouldn\'t count on it.', 'My sources say you\'re dreaming.', 'Answer is a little hazy, try again.', 'Not looking so good.', 'The spirits point to yes.', 'Of course, you can trust it is so.', 'Ummm, How\'s the weather?']
    return x

def user_output(x):
    x = random.choice(x)
    return x

print(user_output(answers_list))
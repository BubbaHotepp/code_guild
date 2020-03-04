import random

print('Welcome diviner. \nBe prepared to be amazed and astounded by the Magic 8 Ball.')

print(input('Ask your question of the mystical Magic 8 Ball!!'))
    
def rand_choice():
    answers = ['It is certain.', 'You can count on it.', 'No doubt fool.', 'Pretty sure.', 'Well, it could be.', 'Absolutely.', 'Yes!', 'No!', 'I really shouldn\'t tell you that.', 'Ask me again later.', 'The future is uncertain right now.', 'I wouldn\'t count on it.', 'My sources say you\'re dreaming.', 'Answer is a little hazy, try again.', 'Not looking so good.', 'The spirits point to yes.', 'Of course, you can trust it is so.', 'Ummm, How\'s the weather?']
    return random.choice(answers)

print(f'The Glorious Magic 8 Ball says: {rand_choice()} ' )
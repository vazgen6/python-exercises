import random

devs = ['Artyom', 'Hovsep', 'Narek', 'Vazgen']
categories = ['System', 'Accounting', 'Chartering', 'Tech Management']

random.shuffle(devs)
random.shuffle(categories)

for dev in devs:
    category = random.choice(categories)
    categories.remove(category)
    print('{} does {}'.format(dev, category))

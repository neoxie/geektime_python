x = range(-10, 10)
y = [value * 2 + 5 if value > 0 else -value * 2 + 5 for value in x]
print(y)

z = [-value * 2 + 5 for value in x if value < 0]
print(z)

text = ' Today,  is, Sunday'
text_list = [s.strip() for s in text.split(',') if len(s.strip()) >= 5]
print(text_list)

import re 

def ufl(word):
    res = word.capitalize()
    return res

m = re.compile('_')

test = 'hi_to_you_all'

words = list(re.split(m, test))

camelcase = ""

camelcase += words[0]

for i in range(1, len(words)):
    camelcase += words[i].capitalize()

print(camelcase)





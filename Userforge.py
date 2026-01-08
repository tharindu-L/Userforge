from itertools import product

def varients(word):
    return[word,word.capitalize(),word.upper()]

names=["tharindu"]
roles=["admin","administrator"]
separators=['','_']

with open("usernames.txt","w") as f:
    for names,roles,separators in product(names,roles,separators):
        for namev,rolev in product(varients(names),varients(roles)):
            f.write(f"{namev}{separators}{rolev}\n")

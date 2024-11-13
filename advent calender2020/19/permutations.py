"""
def get_permutation(string, i=0):

    if i == len(string):   	 
        print("".join(string))

    for j in range(i, len(string)):

        words = [c for c in string]
   
        # swap
        words[i], words[j] = words[j], words[i]
   	 
        get_permutation(words, i + 1)

print(get_permutation('yup'))  """


dict = {1: "a", 2: "b", 3: "c"}
vastaukset = []
og = 'matti'

def get_permutation(string, i=0):

    if i == len(string):  
        sana = "".join(string)
        if sana not in vastaukset and sana != og:   # annii voi tulla useasti sanasta niina
            vastaukset.append(sana)

    for j in range(i, len(string)):

        words = [c for c in string]
   
        # swap
        words[i], words[j] = words[j], words[i]
   	 
        get_permutation(words, i + 1)


def muunna():
    strings = []    
    for v in vastaukset:
        s = ""
        for kirjain in v:
            s += dict[int(kirjain)]
        
    print(strings)


print(get_permutation(og))
print(vastaukset)
muunna()
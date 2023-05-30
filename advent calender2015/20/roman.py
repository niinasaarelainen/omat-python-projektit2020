roman = {}
roman["M"]= 1000
roman["D"]= 500
roman["C"]= 100
roman["L"]= 50
roman["X"]= 10
roman["V"]= 5
roman["I"]= 1

def muunna(str):
    sum = 0
    for letter in str:
        sum += roman[letter]
    return sum

def muunna_subtractive(str):
    sum = 0
    i = 0
    while (i < len(str)-1): # ei voi tutkia vikaa, koska mahdollisesti tutk. vika +1
        k1 = str[i]
        #print(i, k1)        
        k2 = str[i+1]
        if roman[k1] < roman[k2]:  # IX
            erotus = roman[k2] - roman[k1]
            sum += erotus
            i += 2
        else:    # II   tai XI
            summa = roman[k1] 
            sum += summa
            i += 1

    if i == len(str)-1:   # vika luku jää joskus käsittelemättä, joskus ei
        sum += roman[str[-1]] 
    return sum

print("len:", len("MDCCXXVIIII"))
print(muunna("MDCCXXVIIII"))
print(muunna_subtractive("MDCCXXVIIII"))

print("len:", len("MDCCXXVIII"))
print(muunna("MDCCXXVIII"))
print(muunna_subtractive("MDCCXXVIII"))

print("len:", len("IX"))
print(muunna("IX"))
print(muunna_subtractive("IX"))

print("len:", len("XIX"))
print(muunna("XIX"))
print(muunna_subtractive("XIX"))

print("len:", len("CDIII"))  # 403
print(muunna("CDIII"))
print(muunna_subtractive("CDIII"))

print("len:", len("MCDIII"))  # 1403
print(muunna("MCDIII"))
print(muunna_subtractive("MCDIII"))

print("len:", len("MMCDIII"))  # 2403
print(muunna("MMCDIII"))
print(muunna_subtractive("MMCDIII"))
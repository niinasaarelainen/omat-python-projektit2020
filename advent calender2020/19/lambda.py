l = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
s = sorted(l, key = lambda x: x[1])
print(s)

l = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
s = sorted(l, key = lambda x: -int(x['model']))
print(s)

l= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pair = list(filter(lambda x: (x % 2 == 0), l))  
print(pair)
odd = list(filter(lambda x: (x % 2 == 1), l))  
print(odd)

square_nums = list(map(lambda x: x ** 2, l))
print(square_nums)

str = "moi"
c= "m"
str="ei"
tottako = list(map(lambda x: (x == c), str))[0]   # oma
print(tottako)

starts_with = lambda x: True if x.startswith('P') else False   # huom!! syntaksi syötteen antoon
print(starts_with('Python'))

is_number = lambda x: True if x.isnumeric() else False   # huom!! syntaksi syötteen antoon
print("32", is_number('32'))
print("2b", is_number('2b'))
print("b", is_number('b'))
print("1111", is_number('1111'))


fibo_result = [0,1]

for i in range(15):
    uusi_nro = list(map(lambda x: fibo_result[-1] + fibo_result[-2], fibo_result))[-1]
    fibo_result.append(uusi_nro)

print(fibo_result)

l1 = [1, 2, 3, 5, 7, 8, 9, 10]
l2 = [1, 2, 4, 8, 9]
intersection = list(filter(lambda x: (x in l2), l1))  
print(intersection)

l = ["Monday","Friday","Sunday","didididay"]
lennhgt = list(filter(lambda x: (len(x) == 6), l))  
print(lennhgt)

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = list(map(lambda x, y: x + y, l1, l2))    # !!! kaksi listaa luetaan samassa !!!!!
print(l3)

l = [['S ROY', 1.0], ['B BOSE', 3.0], ['N KAR', 2.0], ['C DUTTA', 1.0], ['G GHOSH', 1.0]]
print(list(set([item[1] for item in l ]))[1])

l = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
vastaukset = []
totuusarvot = []
for sana in l:
    totuusarvot.append(list(map(lambda x, y: x == y, sana, reversed(sana))))

print("\n", totuusarvot)
print(len(totuusarvot))
for i in range(len(totuusarvot)):
    if False not in totuusarvot[i]:
        vastaukset.append(l[i])
print(vastaukset)

l = ['bcda', 'abce', 'cbda', 'cbea', 'adcb']
malli = 'abcd'
print(l)
totuusarvot = list(map(lambda x: set(x) == set(malli), l))  # huom! älä laita mallia 2.parametriksi
                                                                # se on 4-kirjaiminen, ja homma tehtäisiin vain 4 krt !!!!!
print(totuusarvot)
vastaukset = [l[i] for i in range(len(totuusarvot)) if totuusarvot[i] == True]
print(vastaukset)

l = [2, 4, 6, 9, 11]
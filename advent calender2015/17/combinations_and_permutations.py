import itertools

subsets = list(itertools.combinations("moro", 2))
print(subsets)  # 2 "eri" mo
print(set(subsets))  # vain yksi mo

subsets = list(itertools.combinations("moro", 4))
print(subsets)  # 2 "eri" mo
print(set(subsets))  # vain yksi mo

print(list(itertools.permutations(range(3))))
print(list(itertools.permutations("matti")))



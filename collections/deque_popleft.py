import collections
 
# initializing deque
de = collections.deque([1, 2, 3])
print("deque: ", de)
 
# using append() to insert element at right end
# inserts 4 at the end of deque
de.append(4)
 
# printing modified deque
print("\nThe deque after appending at right is : ")
print(de)
 
# using appendleft() to insert element at left end
# inserts 6 at the beginning of deque
de.appendleft(6)
 
# printing modified deque
print("\nThe deque after appending at left is : ")
print(de)

# using pop() to delete element from right end
# deletes 4 from the right end of deque
de.pop()
 
# printing modified deque
print("\nThe deque after deleting from right is : ")
print(de)
 
# using popleft() to delete element from left end
# deletes 6 from the left end of deque
de.popleft()
 
# printing modified deque
print("\nThe deque after deleting from left is : ")
print(de)

de = collections.deque((2, 4, 6))
for i in range(3):
    de.append(8)
print(de)
c = de.count(8)
print(c)
de.popleft()
print(de)
de.remove(6)
print(de)

l = ['PHP', 'PHP', 'Python', 'PHP', 'Python', 'JS', 'Python', 'Python', 'PHP', 'Python', 'Q', 'Q']
counts = [(e, l.count(e)) for e in l ]
print(sorted(counts)) # aakkosiin

counts.sort(key=lambda x: x[1])
counts = list(dict.fromkeys(counts))  # delete doubles: dictionary--> list
print(counts)

counts = {(e, l.count(e)) for e in l }
print(counts) # ei missään järj

print("\n map:")
pairs = [(e, l.count(e)) for e in l ]
d = dict(map(lambda pair: (pair[0], pair[1]), pairs))
print(d)
l  = list(d.items())  # huom! items!!  muuten tulee vain keys
print(l)
l.sort(key=lambda x: x[1])
print("vähiten", l[0])
print("eniten löytyy sanaa", l[-1][0], "nimittäin", l[-1][1], "kpl")
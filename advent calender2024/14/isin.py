passing = [10, 15, 2, 5 ,1 , 2, 3]
failing = [10, 15, 2, 5 ,1 , 2, 5]
pattern = [1, 2, 3]

def isin(pattern, sequence):
    for i in range(len(sequence) - len(pattern) + 1):
        if sequence[i:i+len(pattern)] == pattern:
            return i
    return False

print(isin(pattern, passing))
print(isin(pattern, failing))
print()


def guess_seq_len(seq):
    guess = 1
    max_len = len(seq) // 2
    for x in range(2, max_len):
        if seq[0:x] == seq[x:2*x] :
            return x, seq[0:x]

    return guess

list_a = [111,0,3,1,111,0,3,1,111,0,3,1] 
list_b = [67,4,67,4,67,4,67,4,2,9,0]
list_c = [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,23,18,10]

print (guess_seq_len(list_a))
print (guess_seq_len(list_b))
print (guess_seq_len(list_c))
print (guess_seq_len(range(500)))   # test of no repetition
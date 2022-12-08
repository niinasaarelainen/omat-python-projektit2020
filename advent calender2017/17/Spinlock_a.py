
number_of_steps = 338  # puzzle input
#number_of_steps = 4    # helpotettu versio
ar = [0]

def circulate():
    ind = 0
    for i in range(2018):
        ind += number_of_steps 
        ind = ind % len(ar)
        ar.insert(ind + 1 , i+1)
        



circulate() 
ind = ar.index(2017)
print(ar[ind + 1])   # too high 1576
    



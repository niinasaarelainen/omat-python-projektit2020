
house_numbers = []
lahjamaara = 34000000
#lahjamaara = 120

taloja = 788000
#taloja = 51

def alusta_talot():
    for talo in range(taloja):
        house_numbers.append(11)


def jaa_lahjat():
    for aloitustalo in range(1, taloja):
        for intervalli in range(aloitustalo, 50, aloitustalo + 1):
            house_numbers[intervalli] += (aloitustalo + 1)  * 11
            
def monesko():
    for i in range(len(house_numbers)):
        if house_numbers[i] >= lahjamaara:
            return i + 1


        

alusta_talot()
jaa_lahjat()   # 2882880  too high   776160 too low
print(house_numbers)
print(monesko())
    


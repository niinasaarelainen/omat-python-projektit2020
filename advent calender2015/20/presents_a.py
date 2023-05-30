
house_numbers = []
lahjamaara = 34000000
taloja = 788000

def alusta_talot():
    for talo in range(taloja):
        house_numbers.append(taloja)


def jaa_lahjat():
    for aloitustalo in range(1, taloja):
        for intervalli in range(aloitustalo, taloja, aloitustalo + 1):
            house_numbers[intervalli] += (aloitustalo + 1)  * 10
            if house_numbers[intervalli] >= lahjamaara:
                return intervalli + 1


        

alusta_talot()
print(jaa_lahjat())   # 2882880  too high   776160 too low
    



min = 183564
max = 657474  

"""
* It is a six-digit number.
* The value is within the range given in your puzzle input.
* Two adjacent digits are the same (like 22 in 122345).
* Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679)
"""


def criteria_check():
    correct = 0
    for luku in range(min, max + 1):
        ok = False
        edellinen = str(luku)[0]
        for digit in range(1, 6):
            if str(luku)[digit] < edellinen:
                ok = False
                break
            elif str(luku)[digit] == edellinen:
                ok = True
            edellinen = str(luku)[digit]

        if ok:
            print(luku)
            correct += 1

    print("correct", correct)   # 1638   too high



criteria_check()
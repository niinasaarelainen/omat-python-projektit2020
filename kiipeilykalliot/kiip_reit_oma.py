class Kiipeilyreitti:
    def __init__(self, nimi: str, pituus: int, grade: str):
        self.nimi = nimi
        self.pituus = pituus
        self.grade = grade

    def __gt__(self, verrokki):
        return self.nimi > verrokki.nimi

    def __str__(self):
        return f"{self.nimi}, pituus {self.pituus} metriä, grade {self.grade}"


def vaikeuden_mukaan(reitit: list):
    return sorted(pituuden_mukaan(reitit), key=lambda alkio: alkio.grade, reverse = True)     

def vaikeuden_mukaan_2xlambda(reitit: list):
    return sorted(reitit, key=lambda alkio: (alkio.grade, -alkio.pituus), reverse = True)  


def pituuden_mukaan(reitit: list):
    return sorted(reitit, key=lambda alkio: alkio.pituus, reverse = True)    

def normi_sorted(reitit: list):
    return sorted(reitit)  #  reverse = True  toimii täälläkin


if __name__ == "__main__":
    r1 = Kiipeilyreitti("Kantti", 38, "6A+")
    r2 = Kiipeilyreitti("Smooth operator", 9, "7A")
    r3 = Kiipeilyreitti("Syncro", 14, "8C+")
    r4 = Kiipeilyreitti("Suuri leikkaus", 36, "6B")
    r5 = Kiipeilyreitti("Hedelmätarha", 8, "6A")
    r6 = Kiipeilyreitti("Possu ei pidä", 12 , "6B+")
    r7 = Kiipeilyreitti("Pieniä askelia", 13, "6A+")
    r8 = Kiipeilyreitti("Ruotsalaisten reitti", 42, "5+")
    vaik = vaikeuden_mukaan([r1, r2, r3, r4, r5, r6, r7, r8])
    vaik_2xlambda = vaikeuden_mukaan_2xlambda([r1, r2, r3, r4, r5, r6, r7, r8])
    pit = pituuden_mukaan([r1, r2, r3, r4, r5, r6, r7, r8])

    print("\nvaik mukaan:")
    for reitti in vaik:
        print(reitti)

    print("\nvaikx2_lambda mukaan:")
    for reitti in vaik_2xlambda:
        print(reitti)

    print("\npit mukaan:")
    for reitti in pit:
        print(reitti)

    print("\n normi:")
    for reitti in normi_sorted([r1, r2, r3, r4, r5, r6, r7, r8]):
        print(reitti)

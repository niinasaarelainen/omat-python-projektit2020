data = []  
apinat = []
apinat_hash = []  # sis. Monkey0-3 = hashes
monkeys = []   #olioita !!


class Monkey():
    def __init__(self, id, starting_items, divisible, true, false ) -> None:
        self.inspected_count = 0
        self.id = id
        self.starting_items = starting_items
        self.divisible = divisible
        self.true = true
        self.false = false

    def inspect(self):
        self.tulokset = []
        self.inspected_count += len(self.starting_items)
        for item in self.starting_items:
            self.worry_level = item
            self.toiminto()
            self.tulokset.append(self.test())
        self.starting_items = []
        return self.tulokset

    def toiminto(self):
        if self.id == 0:
            self.worry_level = self.worry_level * 19
        if self.id == 1:
            self.worry_level = self.worry_level + 6
        if self.id == 2:
            self.worry_level = self.worry_level * self.worry_level 
        if self.id == 3:
            self.worry_level = self.worry_level + 3

    def test(self):
        #self.worry_level = self.worry_level // 3
        if self.worry_level % self.divisible == 0:
            return [self.true, self.worry_level]  # apinan numero, worry
        else:
            return [self.false, self.worry_level] 
        
    def lisaa_starting_item(self, item):
        self.starting_items.append(item)



def readfile():  
    f = open("data_0-3.txt", "r")         
    for rivi in f:
        data.append(rivi.strip())


def muodosta_apinat():
    apina = []
    for rivi in data:
        if rivi == "":
            apinat.append(apina)
            apina = []
        else:
            apina.append(rivi)
    apinat.append(apina)

def muodosta_hash():
    id = 0
    for monkey in apinat:
        starting_items = []
        st = monkey[1].split(": ")[1]
        st = st.split(", ")
        for item in st:
            starting_items.append(int(item))
        divisible = int(monkey[3].split(" ")[3])
        true = int(monkey[4].split(" ")[5])
        false = int(monkey[5].split(" ")[5])
        monkeys.append(Monkey(id, starting_items, divisible, true, false))
        id += 1




   
readfile()
muodosta_apinat()
muodosta_hash()
for m in monkeys:
    print(m.starting_items)

print()
for x_times in range(20):
    for m in monkeys:
        tulokset = m.inspect()
        print(tulokset)
        for tulos in tulokset:
            id, worry = tulos
            monkeys[id].lisaa_starting_item(worry)

print()
s =sorted([ m.inspected_count for m in monkeys])
print([ m.inspected_count for m in monkeys])
#print(s[-1] * s[-2])
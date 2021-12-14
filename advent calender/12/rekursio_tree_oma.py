
data = []
verkko = {}

def readfile():   # a-kohta
    global data
    f = open("data_easy.txt", "r") # a-kohta !!!!      
    for rivi in f:
        data.append(rivi.split("-"))     # ['start', 'A\n'] x 7


def luo_verkko():
    global verkko
    for a, b in data:
        a = a.strip()
        b = b.strip()
        if a not in verkko:
            verkko[a] = [b]
        if b not in verkko:
            verkko[b] = [a]
        if b not in verkko[a]:
            verkko[a].append(b) 
        if a not in verkko[b]:
            verkko[b].append(a) 

    print(verkko)


"""
    start
    /   \
c--A-----b--d
    \   /
     end
"""

verkko2 = {
  "start": ["A", "b"],
  "A": ["end", "b", "c"],
  "b": ["end", "A"],
  "c": ["A"],
  # "d": ["b"],
  "end" : []
}


polut = []

def kay_lapi_a(solmu, polku):  
  global montako
  if solmu in polku and solmu[0] in "abcdefghijklmnopqrstuwxyz":  
      return 

  polku.append(solmu)
  

  if solmu == 'end':
      print('->'.join(polku))
      polut.append(polku)
      return 
  
  # muuta seuraava
  for s in verkko[solmu]:  # = seuraajat
      uusi_polku = polku[:]
      kay_lapi_a(s, uusi_polku)


def tutki_duplikaatit(solmu, polku):
     # a single small cave can be visited at most twice, and the remaining small caves can be visited at most once. 
     # [ for kirjain in  if eka_kirjain in ]
     #print("polku", polku)    # ['start', 'A']
     #maarat = {}
     #print(solmu, solmu == "start", "start" in polku)
     
     for tunnus in polku:
        
        montako = polku.count(tunnus) 
        print(tunnus, polku, montako)
        eka_kirjain = solmu[0]
        if "start" in polku and solmu == "start":
            return True
        elif "end" in polku and solmu == "end":
            return True
        elif montako == 2 and eka_kirjain in "abcdefghijklmnopqrstuvwxyz":
            return True
        else:
            return False  


def kay_lapi_b(solmu, polku):   
  eka_kirjain = solmu[0]
  if solmu in polku and eka_kirjain in "abcdefghijklmnopqrstuvwxyz":        
        if tutki_duplikaatit(solmu, polku):
            return 

  polku.append(solmu)
  

  if solmu == 'end':
      print('->'.join(polku))
      polut.append(polku)
      return 
  
  # muuta seuraava
  for s in verkko[solmu]:  # = seuraajat
      uusi_polku = polku[:]
      kay_lapi_b(s, uusi_polku)


readfile()
luo_verkko()
#kay_lapi_a("start", [])
kay_lapi_b("start", [])
print(len(polut))
print(polut)


data = []

def readfile():   # a-kohta
    global data
    f = open("data_easy.txt", "r") # a-kohta !!!!      
    for rivi in f:
        data.append(rivi.split("-"))
    print(data)


"""
    start
    /   \
c--A-----b--d
    \   /
     end
"""

verkko = {
  "start": ["A", "b"],
  "A": ["end", "b", "c"],
  "b": ["end", "A"],
  "c": ["A"],
  # "d": ["b"],
  "end" : []
}


polut = []

def kay_lapi(solmu, polku):  
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
      kay_lapi(s, uusi_polku)

readfile()
kay_lapi("start", [])
print(len(polut))

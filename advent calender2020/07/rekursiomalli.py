verkko = {
  "start": ["A", "b"],
  "A": ["end", "b", "c"],
  "b": ["end", "A"],
  "c": ["A"],
  # "d": ["b"],
  "end" : []
}

polut = []

def kay_lapi_a(solmu, polku): 
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



kay_lapi_a("start", [])
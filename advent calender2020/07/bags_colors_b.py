

laukkujen_sisalto = {}
polut = []


def readfile():   
    f = open("data_easy.txt", "r")         
    for rivi in f:
        split1 = rivi.split(" bags contain ")
        laukkujen_sisalto[split1[0]] = split1[1].strip().split(", ")

    print(laukkujen_sisalto)


def kay_lapi(solmu, polku): 
  if "other bags" in solmu :  
      return 

  polku.append(solmu)

  if "other bags" in solmu:
      print('->'.join(polku))
      polut.append(polku)
      return 
  
  for s in laukkujen_sisalto[solmu]:  # = seuraajat
      uusi_polku = polku[:]
      splitted = s.split(" ")
      s = splitted[1] + " " + splitted[2]
      print(s)
      kay_lapi(s, uusi_polku)
  

 

readfile()
kay_lapi("shiny gold", [])

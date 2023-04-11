import pygame

def nollaa_array():
    global matriisi
    for i in range(matriisin_koko):
        matriisi.append([])
        for j in range(matriisin_koko):
            matriisi[-1].append(0)
    


matriisi = []
matriisin_koko = 20
solun_koko = 10
window = pygame.display.set_mode((900, 900))
colour = (0,0,255) #green

circle_radius = 10   # halkaisija 20
border_width = 0 #0 = filled circle
kello = pygame.time.Clock()



nollaa_array()



def main():
    tila = 0
    montako_askelta = 1
    steps_samaan_suuntaan = 0
    kasvata_askelmaaraako = 0
    x = 450
    y = 450
    x_ind = int(matriisin_koko / 2) 
    y_ind = int(matriisin_koko / 2)
    matriisi[y_ind][x_ind] = 1
    pygame.draw.circle(window, colour, (x, y), circle_radius, border_width)
    summa = 0

    while summa <= 265149:
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                pygame.quit() 

       
        
        pygame.draw.circle(window, colour, (x, y), circle_radius, border_width)
        

        if steps_samaan_suuntaan == montako_askelta:
            steps_samaan_suuntaan = 0
            tila += 1  
            kasvata_askelmaaraako += 1          
            if kasvata_askelmaaraako % 2 == 0:
                montako_askelta += 1

        print(montako_askelta)

        if tila % 4 == 0:  # oik
            x += circle_radius * 2 
            x_ind += 1 
        
        if tila  % 4 == 1:  # ylös
            y -= circle_radius * 2
            y_ind -= 1

        if tila  % 4 == 2:  # vasen
            x -= circle_radius * 2
            x_ind -= 1

        if tila  % 4 == 3:  # alas
            y += circle_radius * 2
            y_ind += 1       

        summa = 0  
       
        for i in range (-1, 2): # -1 to 1
            for j in range (-1, 2): # -1 to 1:
                summa += matriisi[y_ind + i][x_ind + j ]  
                print("summa", summa) 
        matriisi[y_ind][x_ind] = summa
        
        steps_samaan_suuntaan += 1

        pygame.display.flip() 
        kello.tick(10)
        
        print(matriisi[9])
        print(matriisi[10])
        print(matriisi[11])
        


main()


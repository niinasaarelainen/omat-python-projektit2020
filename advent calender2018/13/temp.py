# liikuttelu vuorotellen, ongelma että tulee 3 x kaannos
# kun cart on kaantoruudussa

mika_cart = 0
    while kesken:        
        naytto.fill(BLACK)
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()  

        c = carts[mika_cart]
        c.liiku()
        for c in carts:
            piirra(c)
        mika_cart = (mika_cart + 1) % len(carts)

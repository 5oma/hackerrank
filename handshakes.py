def handshake(n):
    # n personas como parámetro 
    # define el conteo total de saludos
    if n == 0 or n == 1: 
         handshakes = 0
    elif n == 2:
         handshakes = 1
    elif n > 2 and n < (10 ** 6):         
         # usaremos una combinación de 2 items
         # calculando factorial n  
         fact = 1

         for i in range(1, n + 1):
             fact = fact * i
        
        #factorial n - 2
         fact_n = 1
         n = n - 2

         for i in range(1, n + 1):
             fact_n = fact_n * i
        
        #combinación
         handshakes = int(fact / (fact_n * 2)) 
    return handshakes 

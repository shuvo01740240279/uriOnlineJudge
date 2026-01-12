
A, B, C = sorted(map(float,input().split()), reverse = True) 

if(A>= (B+C)  ):
    print("NAO FORMA TRIANGULO")
    
else:
    #angle
    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")
    elif A**2 > B**2 + C**2:
         print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")
        
    # sides  
    if A==B==C:
        print("TRIANGULO EQUILATERO")
    elif (A==B or B==C or C==A ):
        print("TRIANGULO ISOSCELES")
A, B, C = map( float, input().split() )

if (A+B>C) and (A+C>B) and (B+C>A):
    perimeter = (A+B+C)
    print(f"Perimetro = {perimeter:.1f}")
else:
    trapeziumArea= ((A+B)/2)*C
    print(f"Area = {trapeziumArea:.1f}")
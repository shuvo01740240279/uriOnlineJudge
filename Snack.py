
x, y = map(int, input().split())

if x == 1:
    price = 4.00
elif x == 2:
    price = 4.50
elif x == 3:
    price = 5.00
elif x == 4:
    price = 2.00
elif x == 5:
    price = 1.50
    
total = price * y
print(f"Total: R$ {total:.2f}")    
    
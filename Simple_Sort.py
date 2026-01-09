#taking input 
a, b, c = map(int, input().split())
#creating list 
numbers = [a, b, c]
#sorting numbers 
numbers.sort()
#printing the value
for number in numbers:
    print(f"{number}")

#blank line 
print()

# print the privious value
print(f"{a}\n{b}\n{c}")



















































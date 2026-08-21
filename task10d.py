first = 0
second = 1

print(first)
print(second)

for i in range(98):
    next_num = first + second
    print(next_num)
    
    first = second
    second = next_num
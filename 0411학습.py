for i in range(1,4):
    for j in range(1,6):
        print(j, end='   ')
    print()

print()

for i in range(1,4):
    for j in range(1,6):
        print(i*j, end='  ')
    print()

print()

for i in range(1,4):
    for j in range(1,6):
        print(j+i, end='  ')
    print()

print()

for i in range(3):
    for j in range(1,6):
        print(i*j, end='  ')
    print()
print()

for i in range(1,10):
    for j in range(2,5):
        print(j,'*',i,'=',i*j, end=' ')
    print()

print()

for i in range(1,10):
    for j in range(2,5):
        print('{:3}*{:3}={:3}'.format(j, i, i*j), end=' ')
    print()

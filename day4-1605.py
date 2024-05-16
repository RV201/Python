#Inverted pyramid
print('\n Inverted pyramid')
for i in range(5):
    x='* '
    x=x*(5-i)
    print(f' {x:^10}')
#LeftSided pyramid
print('\n Left Sided pyramid')
for i in range(5):
    x='* '
    x=x*i
    print(f' {x: <10}')
#Right Sided pyramid
print('\n Right Sided pyramid')
for i in range(5):
    x='* '
    x=x*i
    print(f' {x: >10}')
    
    
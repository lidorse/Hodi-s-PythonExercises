#Question N.1
x = int(input('enter a number: '))
for i in range(1,x):
    if x%i==0:
        print(i)

#Question N.2
counter = 0
lst = []
while True:
    x = int(input('Please choose a number: '))
    if x >= 0:
        counter += x
        lst.append(x)
        avg = counter/len(lst)
        print(f'avg={avg},sum={counter}')
    else:
        print('Thank you.Goodbye!')
        break


#Question N.3
lst = []
while True:
    x = input('Say what\'s that in your mind in 1 word:')
    lst.append(x)
    #print(lst)
    z = lst.count(x)
    #print(z)
    if z == 2:
        print(f'You entered the word {x} twice. Goodbye!')
        break

    if x in lst:
        print(f'You entered the word {x} twice. Goodbye!')
        break

#אחרי 3 ניסיונות אשנה את הCOUNT לשלושה מספרים דומים


# Question N.4
lst1 = []
lst2 = []

while True:
    a = int(input('Please append a number for list num.1: '))
    b = int(input('Please append a number for list num.2: '))
    c = input('To even the lists please enter q, To continue press any key: ')
    lst1.append(a)
    lst2.append(b)
    if c == 'q':
        for i in lst1:
            n1 = i
        for i in lst2:
            n2 = i
        if n1 > n2:
            print(lst1)
        elif n2 > n1:
            print(lst2)
        break
    #if a == 0 or b == 0:
        #continue

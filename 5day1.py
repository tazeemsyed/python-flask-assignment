#from range n to m print all no. divisible by 5 and 7 both
n= int(input('enter n = '))
m=int(input('enter m = '))
print('the number divisible both by 5 and 7 in range ', n ,'to', m,'are :\n')

for i in range (n,m):
    if i%7==0:
        if i%5 ==0:
            print(i,'\t\n')

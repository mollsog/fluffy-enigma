
#QUESTION FOUR
n = int(input())

#a,b and c checks if n is a multiple of 3,5 and 7 then answers true or false 
a = (n%3 ==0)
b = (n%5 == 0)
c = (n%7 == 0)

#Prints the answers
print(f'Is {n} a multiple of 3? {a}')
print(f'Is {n} a multiple of 5? {b}')
print(f'Is {n} a multiple of 7? {c}')

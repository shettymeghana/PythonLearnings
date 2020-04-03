#Write a python  program to get the sum of a square of odd numbers between 22 and 389
odd = []
sum = 0
for i in range(22, 389+1):
    if i % 2 != 0:
        odd.append(i)
        sum = sum + (i*i)
print "Odd numbers between 22 and 389 are :" , odd
print "Sum of squaes of odd numbers between 22 and 389 is : " ,sum
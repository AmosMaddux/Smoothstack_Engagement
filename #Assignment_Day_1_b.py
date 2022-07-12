#Assignment_Day_1_b
# by Amos Maddux in July 2022

import math

#Exercise 1
print(50+50)
print(100-10)

#Exercise 2
print(30*6) #multiplication
print(6^6) #XOR bitwise operator. Retorns 0
print(6**6) #exponent 6 to the power of 6
print(6+6+6+6+6+6) #addition

#Exercise 3
print("Hello World")
print("Hello World : 10")



#Exercise 4
#  A = P (r (1+r)^n) / ( (1+r)^n -1 )
# Loan payment formula. P = initial amount, r = yearly interest divided by pay periods per year, n = total pay periods
monthlyInterest = 6/100/12
monthlyPayment = (800000*(monthlyInterest*(1+monthlyInterest)**103)) / ((1 + monthlyInterest)**103 - 1)
print(math.ceil(monthlyPayment))
    




    




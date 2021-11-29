#probability distribution functions
import sympy
import numpy as np
x=sympy.Symbol('x')
pdf=str(input("Enter the probability distribution function: "))
pdf=pdf.replace('^','**')
pdf=sympy.sympify(pdf)
#calculate the mean
print("calculating the mean...")
#Enter range
print("Enter the range: ")
a=float(input("Enter a: "))
b=float(input("Enter b: "))
mean=sympy.integrate(pdf*x, (x, a, b))
print("Mean = ", mean)
#calculate the variance
print("calculating the variance...")
variance=sympy.integrate(pdf*(x-mean)**2, (x, a, b))
print("Variance = ", variance)
#calculate the standard deviation
print("calculating the standard deviation...")
standard_deviation=sympy.sqrt(variance)
print("Standard deviation = ", standard_deviation)
#cumulative distribution function
import sympy as sy
x=sy.Symbol('x')
cdf=str(input("Enter the cumulative distribution function: "))
cdf=cdf.replace('^','**')
cdf=sy.sympify(cdf)
#calculate the mean
print("calculating the mean...")
#Enter range
print("Enter the range: ")
a=float(input("Enter the lower limit: "))
b=float(input("Enter the upper limit: "))
mean=cdf(b)-cdf(a)
print("Mean = ", mean)
#calculate the variance
print("calculating the variance...")
variance=sy.integrate(cdf*(x-mean)**2, (x, a, b))
print("Variance = ", variance)
#calculate the standard deviation
print("calculating the standard deviation...")
standard_deviation=sy.sqrt(variance)
print("Standard deviation = ", standard_deviation)
#calculate the median
print("calculating the median...")
median=sy.integrate(cdf, (x, a, b))
print("Median = ", median)

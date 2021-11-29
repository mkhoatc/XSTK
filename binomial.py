#binomial distribution
from math import exp, factorial
def binomial(n, k, p):
    return (factorial(n) / (factorial(k) * factorial(n-k))) * (p**k) * (1-p)**(n-k)
n=int(input("Enter n: "))
k=int(input("Enter k: "))
p=float(input("Enter p: "))
print("P(X=k)=P(n,k) = ", binomial(n, k, p))
#calculate the mean and variance of a binomial distribution
mean=n*p
variance=n*p*(1-p)
standard_deviation=variance**0.5
print("Mean = ", mean)
print("Variance = ", variance)
print("Standard Deviation = ", standard_deviation)
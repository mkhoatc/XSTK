#poisson distribution
from math import exp, factorial
def poisson(k, lam):
    return (lam**k / factorial(k)) * exp(-lam)
k=int(input("Enter k: "))
lam=float(input("Enter lam: "))
print("P(k) = ", poisson(k, lam))
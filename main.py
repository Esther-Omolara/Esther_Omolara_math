def power(base, exponent):
  """Display the mathematical function power"""
  powe= base**exponent
  return powe
X= power(2, 3)
print(X)

def factorial(n):
     """Display the mathematical function factorial"""
     factor = 1
     for value in range(1, n+1):
         factor = factor*value
     return factor
Y= factorial(5)
print(Y)

def permutation(n, k):
    """Display the mathematical function permutation"""
    number = 1
    for value in range(n, n-k, -1):
        number = number*value
    return number
Z= permutation(5, 2)
print(Z)

def combination(n,k):
    """Display the mathematical function combination"""
    num = 1
    for value in range( n, n - k, -1):
        num = num*value
    denom = 1
    for value in range(1, k+1):
        denom = denom *value
    return num // denom
A = combination(5, 2)
print(A)


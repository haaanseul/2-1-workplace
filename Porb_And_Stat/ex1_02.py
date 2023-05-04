# Basic Combinatorics

#1
def fun_sum(N1, N2):
    return N1 + N2

#2
def fun_product(N1,N2):
    return N1*N2

#factorial
def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)

#3
def fun_combination(N,k):
    return factorial(N)/(factorial(N-k)*factorial(k))

#4
def fun_permutation(N,k):
    return factorial(N)/factorial(N-k)

#5
def fun_combination_repetition(N,k):
    return factorial(N+k-1)/(factorial(N-1)*factorial(k))


#Example 2.6
if __name__ == '__main__':
     #Funtional verification

    print((fun_combination(10,2)*fun_combination(15,3)
    + fun_combination(10,3)*fun_combination(15,2)
    + fun_combination(10,4)*fun_combination(15,1)
    + fun_combination(10,5))/fun_combination(25,5))
    

    


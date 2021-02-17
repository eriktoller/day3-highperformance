# Program to multiply two matrices using nested loops
import numpy as np

N = 250

def main():
    X = np.random.randint(1,100,size=(N,N))
    Y = np.random.randint(1,100,size=(N,N+1))
    
    result = np.matmul(X, Y)
    
    for r in result:
        print(r)
    

main()
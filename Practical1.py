import numpy as np

def main():
    while True:
        user = input("Is the molecule linear? Y/N ")
        if user.upper() == "Y":
            n = linear("How many carbons long is the polyene? ")
            M = linmatrix(n)
            break
        elif user.upper() == "N":
            n = nonlinear("Is the molecule a: 1. Cyclic Polyene, 2. Platonic Solid or 3. Napthalene? ")
            if n == 1:
                M = cyclicmatrix(n)
            elif n ==2:
                M = 
            break
        else:
            print("Please give a valid response.")
    
    print(get_evals(M))


def linear(n):
    while True:
        try:
            length = int(input(n))
        except ValueError:
            print("Please enter a valid integer.")
            pass
        
        if length % 2 == 0:
            return length
        else:
            print("Please enter an even integer.")
            

def nonlinear(n):
    while True:
        n = int(input(n))
        match n:
            case 1 | 2 | 3:
                return n
            case _:
                print("Please enter an integer 1, 2 or 3.")

def linmatrix(length):
    M = np.zeros((length, length))
    row = M.shape[0]
    for i in range(row-1):
        M[i, i+1] = 1
        M[i+1, i] = 1
    return M

def nonlinmatrix(n):
    while True:
        try:
            length = int(input(n))
        except ValueError:
            print("Please enter a valid integer.")
            pass
        break
    M = linmatrix(length)
    M[0,-1] = 1
    M[-1, 0] = 1
    return M

def get_evals(M):
    evals, evecs = np.linalg.eig(M)
    return np.sort(evals)

if __name__ == "__main__":
    main()
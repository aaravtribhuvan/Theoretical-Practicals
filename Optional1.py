import numpy as np

def main():
    # Gets input from the user of the type of molecule/length and decides which matrix to use
    while True:
        user = input("Is the molecule linear? Y/N ")
        if user.upper() == "Y":
            n = length("How many carbons long is the polyene? ")
            M = linmatrix(n)
            break
        elif user.upper() == "N":
            type = nonlinear("Is the molecule a: 1. Cyclic Polyene, 2. Platonic Solid or 3. Napthalene? ")
            if type == "1" :
                n = length("How many carbons are in the cyclic polyene? ")
                M = cyclicmatrix(n)
            elif type == "2" :
                M = platonic("Is it a: 1. Tetrahedron, 2. Cube or 3. Dodecahedron? ")
            else:
                M = napthalene()
            break
        else:
            print("Please give a valid response.")
    #The correect matrix for the molecule specified by the user is then retrieved

    print("Matrix:")
    print(M)
    rounded_evals = get_evals(M)
    print("\nEnergies:")
    for i in rounded_evals:
        print("α + ", i ," β")
    
    deg = degeneracies(rounded_evals)
    print("\n Degeneracies:")
    for i in deg:
        print(i , " : " , deg[i])
    #The information about the matrix and the calculated energies/degeneracies are then printed for the user

# For a linear molecule it ensures it is an even number
def length(n):
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

# Used to input what the non-linear molecule is        
def nonlinear(type):
    while True:
        n = (input(type))
        match n:
            case "1" | "2" | "3":
                return n
            case _:
                print("Please enter a valid response 1, 2 or 3.")
                
# All of the pontential matrices needed for the molecules that the user can specify
def linmatrix(length):
    M = np.zeros((length, length))
    row = M.shape[0]
    for i in range(row-1):
        M[i, i+1] = M[i+1, i] = 1
    return M

def cyclicmatrix(n):
    M = linmatrix(n)
    M[0,-1] = M[-1, 0] = 1
    return M

def platonic(type):
    type = nonlinear(type)
    match type:
        case 1:
            M = tetrahedron()
            return M
        case 2:
            M = cube()
            return M
        case 3:
            M = dodecahedron()
            return M

def tetrahedron():
    M = np.ones((4, 4)) - np.eye(4)
    return M

def cube():
    edges = [
        (0,1),(1,2),(2,3),(3,0),
        (4,5),(5,6),(6,7),(7,4),
        (0,4),(1,5),(2,6),(3,7)
    ]
    M = np.zeros((8, 8))
    for i, j in edges:
        M[i, j] = M[j, i] = 1
    return M

def dodecahedron():
    edges = [
        (0,1),(1,2),(2,3),(3,4),(4,0),
        (0,5),(1,6),(2,7),(3,8),(4,9),
        (5,10),(6,11),(7,12),(8,13),(9,14),
        (10,15),(11,16),(12,17),(13,18),(14,19),
        (15,5),(16,6),(17,7),(18,8),(19,9)
    ]
    M = np.zeros((20, 20))
    for i, j in edges:
        M[i, j] = M[j, i] = 1
    return M

def napthalene():
    edges = [
        (0,1),(1,2),(2,3),(3,4),(4,5),(5,0),
        (5,6),(6,7),(7,8),(8,9),(9,0)
    ]
    
    M = np.zeros((10, 10))
    for i, j in edges:
        M[i, j] = M[j, i] = 1
    return M

# Once the matrix is chosen the energies are calculated
def get_evals(M):
    evals, evecs = np.linalg.eig(M)
    evals = np.sort(evals)
    evals_rounded = ['%.6f' % eval for eval in evals]
    return evals_rounded

# Used to count the number of degenerate orbitals
def degeneracies(evals):
    deg = {}
    for i in evals:
        if i in deg:
            deg[i] += 1
        else:
            deg[i] = 1
    return deg


if __name__ == "__main__":
    main()
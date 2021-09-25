import random


def generate_matrix(m, n, d=(1, 100)):
    matrix = []
    for i in range(m):
        m_n = []
        for j in range(n):
            m_n.append(random.randint(*d))
        matrix.append(m_n)
    return matrix

def calculate(m, n):
    matrix = []
    if len(m) == len(n[0]):
        for i in range(len(m)):
            m_n = []
            for j in range(len(n)):
                m_n.append(m[i][j]*n[j][i])
            matrix.append(m_n)
    return matrix

def show(m):
    print(" * "*100)
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j], end=" ")
        print()
    print()

m = [
    [1, 2, 3],
    [3, 2, 1],
    [1, 2, 3],
    [3, 2, 1],
]
n = [
    [1, 2, 3, 1],
    [3, 2, 1, 1],
    [1, 2, 3, 1]
]


M = 20000
N = 10000
m = generate_matrix(M, N, d=(100000, 1000000))
n = generate_matrix(N, M, d=(100000, 1000000))
m_n = calculate(m, n)

show(m)
show(n)
show(m_n)

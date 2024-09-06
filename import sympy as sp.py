import sympy as sp

# Define symbols
s, b, J, K, X, L, R = sp.symbols('s b J K X L R')

# Define matrices A, B, C, and D
A = sp.Matrix([[0, 1, 0], 
               [0, -b/J, K/J], 
               [0, -X/L, -R/L]])
B = sp.Matrix([[0], 
               [0], 
               [1/L]])
C = sp.Matrix([[1, 0, 0]])
D = sp.Matrix([[0]])

# Identity matrix of the same size as A
I = sp.eye(A.shape[0])

# Calculate the transfer function H(s) = C*(sI - A)^(-1)*B + D
H_s = C * (s*I - A).inv() * B + D
print(H_s)
print(H_s.simplify())

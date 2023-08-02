A = [[2, 1, -5], [3, 7, 0], [6, 4, 8]]

dp = A[0][0] + A[1][1] + A[2][2]

print("Diagonal principal: ", dp)

soma_A = A[0][0] + A[0][1] + A[0][2]
soma_A += A[1][0] + A[1][1] + A[1][2]
soma_A += A[2][0] + A[2][1] + A[2][2]
print("Soma matriz: ", soma_A)

dp = 0
soma_A = 0
lin = len(A)
col = len(A[0])

for i in range(lin):
    for j in range(col):
        if i == j:
            dp += A[i][j]
        soma_A += A[i][j]
print("Diagonal principal: ", dp)
print("Soma matriz: ", soma_A)
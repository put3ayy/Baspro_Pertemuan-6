A = [
    [1, 2, 3, 4, 5],
    [2, 3, 1, 5, 4],
    [1, 1, 1, 2, 1],
    [0, 1, 5, 3, 1],
    [5, 3, 2, 0, 0]
]

B = [
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [2, 0, 1, 0, 1],
    [3, 5, 2, 0, 0],
    [1, 1, 1, 1, 3]
]

hasil = []

for i in range(5): #baris
    baris = []
    for j in range(5): #kolom
        total = 0
        for k in range(5): #menghitung hasil perkalian
            total += A[i][k] * B[k][j]
        baris.append(total)
    hasil.append(baris)

print("Hasil perkalian matrix A x B : ")
for baris in hasil:
    print(baris)
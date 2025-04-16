# Perkalian matrix 5x5 dengan matrix 5x5

## INPUT
### 1. Matrix A dan B sudah didefinisikan di dalam program
```python
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
### 2. Program akan menghitung hasil perkalian matrix A dengan matrix B
hasil = []

for i in range(5):          // i = indeks untuk baris matrix A
    baris = []
    for j in range(5):      // j = indeks untuk kolom matrix B
        total = 0
        for k in range(5):   // k = indeks untuk perkalian elemen baris A dan kolom B
            total += A[i][k] * B[k][j]
        baris.append(total)
    hasil.append(baris)
    
### 3. Hasilnya akan ditampilkan di layar output
print("Hasil perkalian matrix A x B : ")
for baris in hasil:
    print(baris)        // mencetak setiap baris hasil perkalian matrix

## OUTPUT
Hasil perkalian matrix A x B :
[31, 32, 22, 10, 22]
[33, 40, 25, 13, 21]
[13, 15, 10, 5, 8]
[24, 19, 14, 2, 8]
[16, 14, 18, 18, 22]

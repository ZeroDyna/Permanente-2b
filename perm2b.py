def insertionSort(A):
    for j in range(1,len(A)) :
        key = A[j]
        i = j-1
        while i >= 0 and key < A[i]:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
    return A

A= ['1','2','4','6','8','5','3','7']
insertionSort(A)
print ("Una vez ordenado")
for j in range (len(A)):
    print (A[j])
    #complejidad 3n^2 + 4n + 1= O(N^2)
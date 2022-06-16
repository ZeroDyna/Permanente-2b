# Permanente-2b
Se implemento los algoritmos insertion sort y bubble sort en python por medio de funciones, ambos algoritmos realizan la mismas funciones en un tiempo similar.

## Archivo perm2b

1.Se implemento el algoritmo insertion sort para este archivo del cual la complejidad es O(N^2)

    ```
    def insertionSort(A):
    for j in range(1,len(A)) :
        key = A[j]
        i = j-1
        while i >= 0 and key < A[i]:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
    return A 
    ```
    
2. ![_O(N^2)_ (1)](https://user-images.githubusercontent.com/93954219/173974633-63b213d1-59d6-48b4-8680-2a9761103a56.png)

3. ![n vs  Tiempo en segundos](https://user-images.githubusercontent.com/93954219/173974347-56085545-682a-417b-842b-e11c035dc92e.png)

##Archivo perm2b 2

1.Se implemento el algoritmo Bubble sort para este archivo, su complejidaad es O(N^2)

    ```
    def bubbleSort(L):
    n = len(L)

    for i in range(n-1):      
        for j in range(0, n-i-1):           
            if L[j] > L[j + 1]:
                swapped = True
                L[j], L[j + 1] = L[j + 1], L[j]         
        if not swapped:
            return
     ```

2.  ![_O(N^2)_](https://user-images.githubusercontent.com/93954219/173974730-b8a05bb6-291a-4010-9ddf-0dd29f911d5f.png)

4.  ![n vs  Tiempo](https://user-images.githubusercontent.com/93954219/173974893-5dc0d92b-e2ec-4b61-bde7-b9eb0ceb4344.png)


